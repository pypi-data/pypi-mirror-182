from .engines import mysqlDefault
from .engines import mysqlDocker
from .engines import mongoDocker

# Entry Function


def start(config):
    DB_ENGINE = config.DB_ENGINE
    MsqModule = ''

    if (DB_ENGINE == 'mysql'):
        MsqModule = mysqlDefault
    elif (DB_ENGINE == 'mysqlDocker'):
        MsqModule = mysqlDocker
    elif (DB_ENGINE == 'mongoDocker'):
        MsqModule = mongoDocker
    else:
        MsqModule = mysqlDefault

    MsqModule.start(config)


# Example Call Below ***-----------***-----------***-----------***-----------***
class Config:
    DB_ENGINE = 'mysql'
    STAGE_STORAGE_PATH = '/home/un4/Reponere/Drive' + '/mysqlBackup/'
    GIT_PATH = 'GIT_PATH_HERE'
    USERNAME = 'un4'
    GIT_NAME = 'GIT_NAME_HERE'
    GIT_EMAIL = 'GIT_EMAIL_HERE'
    INTERVAL = 60*15  # seconds


# config = Config()
# dbbkp.main.start(config)
# NOTE: Run As/With sudo
