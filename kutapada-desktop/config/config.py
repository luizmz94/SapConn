""" Configuration file """
import json
import os


class Config: # pylint: disable=R0903
    """Main configuration file"""
    #documents_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')
    _file_name = "config.json"

    def __init__(self):
        #full_config_path = os.path.join(Config.documents_path, Config._file_name)
        full_config_path = os.path.join('/Applications/SAP Clients/SAPGUI', Config._file_name)
        with open(full_config_path, "r") as config_file:
            self.config_json = json.load(config_file)

    @property
    def data_file_path(self) -> str:
        """Path for data file"""
#        return '/Volumes/GoogleDrive-103207462413239928181/My Drive/Keepass/connections_data_base.json'
        return self.config_json["data_file_path"]
#        return '/Users/luizcarloszanellamartins/Documents/kutapada/kutapada-desktop/connection/connections_data_base.json'



class ConfigFactory: # pylint: disable=R0903
    """Singleton based factory"""
    _singleton: Config = None

    @staticmethod
    def get_instance() -> Config:
        """Returns singleton instance"""
        if ConfigFactory._singleton is None:
            ConfigFactory._singleton = Config()
        return ConfigFactory._singleton
