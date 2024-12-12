import logging
import os
from datetime import datetime
from exception import CustomException
import sys

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # Log to file
        logging.StreamHandler()             # Log to console
    ]

)
logging.info("This is a test log message.")
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        
        logging.error("An exception occurred", exc_info=True)  
        raise CustomException(e,sys)

        