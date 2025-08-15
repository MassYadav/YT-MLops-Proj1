from src.logger import logging
from src.exception import MyException  # ✅ Now this will work
import sys

# Logging test
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

# Exception test
try:
    a = 1 + 'Z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e

# Pipeline test
from src.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()
