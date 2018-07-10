class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestConfig(Config):
    """
    Testing configurations
    """

    TESTING =True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgresql:123456@localhost:5432/test_db'
    DEBUG = True
    


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}