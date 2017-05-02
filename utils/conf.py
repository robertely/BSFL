import yaml
import logging
logger = logging.getLogger(__name__)


def parse(stream):
    try:
        logging.debug('Parsing conf yaml')
        return yaml.load(stream)
    except yaml.YAMLError as e:
        logging.critical('There was a problem parsing job yaml file')
        logging.critical(e)
        exit(99)


# TODO: lint config
def lint(config):
    pass
