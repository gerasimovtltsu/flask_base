class Config:
    SECRET_KEY = 'your-secret-key'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

# Dictionary mapping environment names to configuration classes
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

# Retrieve the configuration class based on the current environment
def get_config(env_name):
    return config_by_name.get(env_name, DevelopmentConfig)
