# coding=utf-8
import json
import logging.config
import os

import CommunicationHandlerInterface
import ServerMediator


class HelloWorld(CommunicationHandlerInterface.CommunicationHandlerInterface):
    pass


def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == '__main__':
    setup_logging()
    chi = HelloWorld(ServerMediator.ServerMediator)
    chi.connect("127.0.0.1",9666)
