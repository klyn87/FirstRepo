import pandas as pd
import numpy as np
import os, sys
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info(f"Started, python: {sys.version_info}")
logging.info(f"pd version: {pd.__version__}")
logging.info(f"np version: {np.__version__}")
x = pd.DataFrame({'a':[1,2,3], 'b':['x','y','z']})
logging.info(x)
logging.warning("Done!")
