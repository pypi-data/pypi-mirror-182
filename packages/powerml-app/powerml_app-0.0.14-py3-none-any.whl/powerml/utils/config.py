import config
import os


def get_config(dictionary={}):
    global_config = setup_config(dictionary)
    return global_config


def setup_config(dictionary):
    home = os.path.expanduser("~")
    home_config_path = os.path.join(home, ".powerml/configure.yaml")
    return config.ConfigurationSet(
        config.config_from_dict(dictionary),
        config.config_from_yaml(home_config_path, read_from_file=True),
    )
