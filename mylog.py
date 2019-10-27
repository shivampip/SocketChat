import logging
from colorlog import ColoredFormatter

#######################################################################################################

LOG_LEVEL_ROOT= logging.DEBUG      # Shoud be lowest bcz it's parent of both handler
LOG_LEVEL_STREAM= logging.DEBUG    # For printing
LOG_LEVEL_FILE= logging.DEBUG       # For storing in file


LOGFORMAT_STREAM= "%(log_color)s%(message)s%(reset)s"
LOGFORMAT_FILE= "%(asctime)s , %(module)s, %(funcName)s, %(levelname)s, %(levelno)s, %(message)s, %(pathname)s, %(processName)s, %(relativeCreated)d "


#LOGFORMAT_STREAM= "%(log_color)s%(levelname)s %(module)s %(funcName)s  %(message)s%(reset)s"
#LOGFORMAT_FILE= "%(asctime)s , %(module)s, %(funcName)s, %(levelname)s, %(levelno)s, %(message)s, %(pathname)s, %(processName)s, %(relativeCreated)d "


LOG_FILE_PATH= "hilog.csv"
#LOG_LEVEL_ROOT= logging.DEBUG      # Shoud be lowest bcz it's parent of both handler
#LOG_LEVEL_STREAM= logging.DEBUG    # For printing
#LOG_LEVEL_FILE= logging.INFO       # For storing in file
#
#LOGFORMAT_STREAM= "%(log_color)s%(levelname)s %(module)s %(funcName)s  %(message)s%(reset)s"
#LOGFORMAT_FILE= "%(asctime)s , %(module)s, %(funcName)s, %(levelname)s, %(levelno)s, %(message)s, %(pathname)s, %(processName)s, %(relativeCreated)d "
#
#LOG_FILE_PATH= "hilog.csv"

#######################################################################################################

## Root Logger
logger= logging.getLogger("mylog")
logger.setLevel(LOG_LEVEL_ROOT)


## Stream Logger
stream_formatter = ColoredFormatter(
    LOGFORMAT_STREAM,
    log_colors={
		'DEBUG':    'cyan,bold',
		'INFO':     'green,bold',
		'WARNING':  'yellow,bold',
		'ERROR':    'red,bold',
		'CRITICAL': 'red,bg_white',
	})
stream_handler = logging.StreamHandler()
stream_handler.setLevel(LOG_LEVEL_STREAM)
stream_handler.setFormatter(stream_formatter)


## File Logger
file_formatter= logging.Formatter(LOGFORMAT_FILE)
file_handler= logging.FileHandler(LOG_FILE_PATH, mode= 'a')

## Create new log file when existing reach certain size limit
#file_handler= logging.handlers.RotatingFileHandler(LOG_FILE_PATH, maxBytes=500, backupCount=2)

## Create new log file at every certain interval
#file_handler= logging.handlers.TimedRotatingFileHandler(LOG_FILE_PATH, when='M', interval=1)
#file_handler = logging.handlers.TimedRotatingFileHandler(LOG_FILE_PATH, when = 'midnight', backupCount = 30)


file_handler.setFormatter(file_formatter)
file_handler.setLevel(LOG_LEVEL_FILE)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


#from logging.handlers import SocketHandler
#socket_handler = SocketHandler('127.0.0.1', 19996)  # default listening address
#logger.addHandler(socket_handler)



logger.debug("Logging Started")
	



#######################################################################################################

# Logging counter
# https://stackoverflow.com/questions/13695181/pass-a-counter-to-every-python-logging-method

# Log Viewer
# https://github.com/Busimus/cutelog