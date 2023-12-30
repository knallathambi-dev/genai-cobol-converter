from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv()

class Config:
    openai_api_key = os.getenv('OPENAI_API_KEY')
    assert openai_api_key is not None
    openai_org_id = os.getenv('OPENAI_ORG_ID')
    assert openai_org_id is not None
    google_api_key = os.getenv('GOOGLE_API_KEY')
    assert google_api_key is not None
    work_dir = os.getenv('WORK_DIR')
    os.makedirs(work_dir, exist_ok=True)
    prompts_path = os.getenv('PROMPTS_PATH')
    assert os.path.exists(prompts_path) is True
    output_dir = os.getenv('OUTPUT_DIR')
    os.makedirs(work_dir, exist_ok=True)

cfg = Config()

if __name__ == "__main__":
    logger.info('Loading configuration')
    help(cfg)
