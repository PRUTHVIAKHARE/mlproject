import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"
os.makedirs(os.path.join(os.getcwd(), 'logs'), exist_ok=True)
LOG_FILE_PATH = os.path.join(os.getcwd(), LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] {%(lineno)d} %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

