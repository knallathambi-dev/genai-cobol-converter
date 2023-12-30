import sys
from cob2py_app.service.base_codegen import BaseCodegen
from cob2py_app.service.openai_codegen import OpenaiCodegen
from cob2py_app.service.google_codegen import GoogleCodegen
from cob2py_app.config import cfg
import os
import yaml
from loguru import logger
from datetime import datetime

logger.remove()
logger.add(sys.stdout, level="INFO")

def run_playbook(config_path: str):
    logger.info('Load playbook config from {}', config_path)
    curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
    out_base_dir = os.path.join(
        cfg.output_dir, f'Run_{curr_time}'
    )    
    os.makedirs(out_base_dir, exist_ok=True)
    logger.info('Output artifacts would be stored in {}', out_base_dir)

    with open(config_path) as fp:
        config = yaml.safe_load(fp)    
    providers = config['genai_providers']
    cobol_artifacts = config['cobol_artifacts']
    for provider in providers:
        codegen: BaseCodegen
        if provider['name'] == 'openai':
            codegen = OpenaiCodegen(
                model=provider['model'], temperature=provider['temperature']
            )
        elif provider['name'] == 'google':
            codegen = GoogleCodegen(
                model=provider['model'], temperature=provider['temperature']
            )
        else:
            raise Exception(f'Unknown GenAI provider {provider["name"]}')
        for cobol_aritifact in cobol_artifacts:
            codegen.run_pipeline(
                cobol_aritifact['path'],
                os.path.join(out_base_dir, provider['name']),
                cobol_aritifact['category']
            )

if __name__ == '__main__':
    config_path = sys.argv[1]
    assert config_path is not None
    run_playbook(config_path)
