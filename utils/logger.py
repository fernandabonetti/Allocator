import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('dracon.log')

file_formatter=logging.Formatter("{'time':'%(asctime)s','message': {'%(message)s'}}")
handler.setFormatter(file_formatter)
logger.addHandler(handler)