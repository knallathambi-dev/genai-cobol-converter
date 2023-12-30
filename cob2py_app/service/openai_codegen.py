import os

from pathlib import Path
from cob2py_app.config import cfg
from cob2py_app.helpers.cobol_utils import format_cobol_source
from openai import OpenAI
from loguru import logger
from typing import List
from yaml import safe_load
import jinja2
import timeit
import json
from cob2py_app.helpers.markdown_utils import get_code_from_markdown
from datetime import datetime
from cob2py_app.helpers.dev_utils import format_file, lint_code
from cob2py_app.service.base_codegen import BaseCodegen


class OpenaiCodegen(BaseCodegen):
    def __init__(self, model="gpt-4", temperature=0.2):
        super().__init__()
        self.model = model
        self.temperature = temperature
        self.environment = jinja2.Environment()
        self.client = OpenAI(api_key=cfg.openai_api_key, organization=cfg.openai_org_id)
        logger.info("Created OpenAI client")
        with open(cfg.prompts_path) as f:
            self.prompts_collection = safe_load(f)
        logger.info(
            "Prompts loaded from {}", cfg.prompts_path
        )

    def execute_prompt(self, messages: List):
        start_time = timeit.default_timer()
        logger.info("Model={}. Executing Prompt", self.model)
        logger.debug(messages)
        chat_completion = self.client.chat.completions.create(
            messages=messages, model=self.model, temperature=self.temperature
        )
        logger.info("Elapsed time ==> {} seconds", round(timeit.default_timer() - start_time, 2))
        logger.info(chat_completion.usage)
        logger.info(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content
    
    def convert_to_python(self, cobol_program_name:str, cobol_source: str, out_dir: str, prompt_key='cobbat_conv'):
        logger.info("Generate Python code for COBOL program {}", cobol_program_name)
        system_message = self.prompts_collection[prompt_key]["system_message"]
        template = self.environment.from_string(
            self.prompts_collection[prompt_key]["user_message"]
        )
        user_message = template.render(cobol_code=cobol_source)
        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": user_message,
            },
        ]
        logger.debug('Prompt ==> {}', messages)
        with open(os.path.join(out_dir, f'{cobol_program_name}__conv_prompt.txt'), 'w') as fp:
            json.dump(messages, fp, indent=2)

        result = self.execute_prompt(messages)
        with open(os.path.join(out_dir, f'{cobol_program_name}__conv_response.txt'), 'w') as fp:
            fp.write(result)
        return result

    def document_code(self, cobol_program_name:str, cobol_source: str, out_dir: str):
        logger.info("Generate Documentation for COBOL program {}", cobol_program_name)
        system_message = self.prompts_collection["cobol_documentation"]["system_message"]
        template = self.environment.from_string(
            self.prompts_collection["cobol_documentation"]["user_message"]
        )
        user_message = template.render(cobol_code=cobol_source)
        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": user_message,
            },
        ]
        logger.debug('Prompt ==> {}', messages)
        with open(os.path.join(out_dir, f'{cobol_program_name}__documentation_prompt.txt'), 'w') as fp:
            json.dump(messages, fp, indent=2)

        result = self.execute_prompt(messages)
        with open(os.path.join(out_dir, f'{cobol_program_name}__documentation.md'), 'w') as fp:
            fp.write(result)

    def critic_generated_code(self, cobol_program_name:str, cobol_code: str, python_code: str, out_dir: str):
        logger.info("Generate review report for Python code generated from COBOL program {}", cobol_program_name)
        system_message = self.prompts_collection["code_critic"]["system_message"]
        template = self.environment.from_string(
            self.prompts_collection["code_critic"]["user_message"]
        )
        user_message = template.render(cobol_code=cobol_code, python_code=python_code)
        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": user_message,
            },
        ]
        logger.debug('Prompt ==> {}', messages)
        with open(os.path.join(out_dir, f'{cobol_program_name}__critic_prompt.txt'), 'w') as fp:
            json.dump(messages, fp, indent=2)

        result = self.execute_prompt(messages)
        with open(os.path.join(out_dir, f'{cobol_program_name}__critic_response.txt'), 'w') as fp:
            fp.write(result)

    def run_pipeline(self, cobol_file_path: str, out_base_dir: str, prompt_key='cobbat_conv'):
        cobol_program_name = os.path.basename(cobol_file_path).split(".")[0]        
        out_dir = os.path.join(out_base_dir, cobol_program_name)
        os.makedirs(out_dir, exist_ok=True)
        cobol_source = format_cobol_source(cobol_file_path)
        conversion_result = self.convert_to_python(
            cobol_program_name, cobol_source, out_dir, prompt_key
        )
        python_code_blocks = get_code_from_markdown([conversion_result])
        logger.info("Extracted Python code blocks ==> {}", python_code_blocks)
        for index, python_block in enumerate(python_code_blocks):
            python_filepath = os.path.join(out_dir, f'{cobol_program_name}__conv_python_{index + 1}.py')
            with open(python_filepath, 'w') as fp:
                fp.write(python_block)
            self.critic_generated_code(
                cobol_program_name, cobol_source, python_block, out_dir
            )
            logger.info("Running formatter (Black) on {}", python_filepath)
            format_file(Path(python_filepath))
            logger.info("Running linter (pylint) on {}", python_filepath)
            lint_code(Path(python_filepath))
        self.document_code(
            cobol_program_name, cobol_source, out_dir
        )
        
if __name__ == '__main__':
    curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
    out_base_dir = os.path.join(
        cfg.output_dir, f'OpenAI_{curr_time}'
    )
    os.makedirs(out_base_dir, exist_ok=True)
    openai_obj = OpenaiCodegen()
    openai_obj.run_pipeline(
        './resources/cobol_source/COBBAT/PINVRPT.cbl',
        out_base_dir
    )
