import configparser
import os


def read_config(configName = 'configurations.ini'):
    config = configparser.ConfigParser()
    # configParser = configparser.RawConfigParser()  
    # configParser.read(configName)
    my_file = os.path.join('configs', 'configurations.ini')
    config.read(my_file)
    return config
    # foo = config.sections()
    # return config.sections()
    # for key in config['defaults']:  
    #     print(key)
        
    # print(config['defaults']['distvariation'])

# read_config()