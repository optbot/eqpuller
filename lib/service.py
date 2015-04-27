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

def rows():
    _symbols = [
            'DDD',
            'FSLR',
            'GE',
            'GILD',
            'JUNO',
            'NFLX',
            'SCTY',
            'SPWR',
            'SSYS',
            'TSLA',
            'WATT',
            ]
    _companies = [
            '3D Systems Corporation',
            'First Solar, Inc.',
            'General Electric Company',
            'Gilead Sciences Inc.',
            'Juno Therapeutics Inc.',
            'Netflix, Inc.',
            'SolarCity Corporation',
            'SunPower Corporation',
            'Stratasys Ltd.',
            'Tesla Motors, Inc.',
            'Energous Corporation',
            ]
    _exchanges = [
            'NYSE',
            'NASDAQ',
            'NYSE',
            'NASDAQ',
            'NASDAQ',
            'NASDAQ',
            'NASDAQ',
            'NASDAQ',
            'NASDAQ',
            'NASDAQ',
            'NASDAQ',
            ]
    _ret = []
    for i in range(len(_symbols)):
        _ret.append({"symbol": _symbols[i], 
            "company_name": _companies[i], "exchange": _exchanges[i],
            "active": True}) 
    return _ret;

def eqpuller():
    _rows = rows()
    for _row in _rows:
        print(_row)

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
    eqpuller()
