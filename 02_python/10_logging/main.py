import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')

logger.debug('This is a debug message')



""" # create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formater = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formater)
file_h.setFormatter(formater)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error') """