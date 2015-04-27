"""
.. Copyright (c) 2015 Marshall Farrier, Robert Rodrigues, Mark Scappini
   license http://opensource.org/licenses/MIT

Equity puller service main
==========================
"""
import argparse
import logging

from pymongo import MongoClient
from pymongo.errors import BulkWriteError

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

def updatedb(client, rows):
    _dbname = 'optionsMkt'
    _collname = 'equities'
    _db = client[_dbname] 
    _coll = _db[_collname]
    _bulk = _coll.initialize_unordered_bulk_op()
    _n_toinsert = 0
    logger.info('updating active equities')
    for _row in rows:
        _symbol = _row['symbol']
        if _coll.find_one({'symbol': {'$in': [_symbol.lower(), _symbol.upper()]}}) is not None:
            logger.info("equity {} already present".format(_symbol))
        else:
            _bulk.insert(_row)
            _n_toinsert += 1
            logger.debug("equity {} queued for insert into {}.{}".format(_row['symbol'], _dbname, _collname))
    if _n_toinsert > 0:
        try:
            _result = _bulk.execute()
        except BulkWriteError:
            logger.exception("error writing to database")
            raise
        else:
            logger.info("{} records inserted into {}.{}".format(_result['nInserted'], _dbname, _collname))
    else:
        logger.info("no new equities to insert")

def eqpuller(dbconn):
    _rows = rows()
    _client = MongoClient(dbconn)
    logger.info('db connection opened')
    updatedb(_client, _rows)
    _client.close()
    logger.info('db connection closed')

if __name__ == '__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('--logpath', required=True)
    _parser.add_argument('--logfmt', required=True)
    _parser.add_argument('--dbconn', required=True)
    _args = _parser.parse_args()
    _handler = logging.FileHandler(_args.logpath)
    _formatter = logging.Formatter(_args.logfmt)
    _handler.setFormatter(_formatter)
    logger.addHandler(_handler)
    logger.setLevel(logging.INFO)
    eqpuller(_args.dbconn)
