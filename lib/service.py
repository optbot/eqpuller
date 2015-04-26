"""
.. Copyright (c) 2015 Marshall Farrier, Robert Rodrigues, Mark Scappini
   license http://opensource.org/licenses/MIT

Equity puller service main
==========================
"""
import argparse
import logging

import pymongo

logger = logging.getLogger('eqpuller')

def equities():
    _ret = [
            'ddd',
            'ge',
            'nflx',
            'scty',
            'spwr',
            'tsla',
            ]
    return _ret;

if __name__ == '__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('--logpath', required=True)
    _parser.add_argument('--logfmt', required=True)
    _args = _parser.parse_args()
    _handler = logging.FileHandler(_args.logpath)
    _formatter = logging.Formatter(_args.logfmt)
    _handler.setFormatter(_formatter)
    logger.addHandler(_handler)
    logger.setLevel(logging.INFO)
    logger.info(equities())
    logger.warn('hander works!')
    logger.info('formatter works!')
