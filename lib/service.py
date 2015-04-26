import pymongo

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
    import logging
    logger = logging.getLogger('eqpuller')
    handler = logging.FileHandler('/mnt/disk1/var/log/optbot/eqpuller/service.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s.%(funcName)s :  %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info(equities())
