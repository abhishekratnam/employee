import logging
import os
import sys

def logger_init(name):
    logformat ='[%(name)s][%(levelname)s] %(filename)s:%(lineno)d %(message)s'
    logging.basicConfig(format=logformat)
    logger = logging.getLogger(name)
    logLevel = os.getenv('LOG_LEVEL')
    if not logLevel:
        logLevel = 'DEBUG'
    print('Setting log level to {}'.format(logLevel))
    logger.setLevel(logLevel)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logLevel)
    # # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatters to handlers
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger