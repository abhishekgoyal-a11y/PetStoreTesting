import yaml

class DefaultsConfig:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DefaultsConfig.__instance is None:
            DefaultsConfig.__instance = DefaultsConfig()

        return DefaultsConfig.__instance

    def __init__(self):
        if DefaultsConfig.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DefaultsConfig.__instance = self
        self.default_values_dict = dict()

    def read_yaml_file(self, yaml_file_path):
        try:
            with open(yaml_file_path) as fp:
                yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
                if not self.default_values_dict:
                    self.default_values_dict.update(yaml_data)
                else:
                    for i, j in yaml_data.items():
                        data = self.default_values_dict.get(i)
                        if data:
                            self.default_values_dict[i].update(yaml_data[i])
                        else:
                            self.default_values_dict[i] = yaml_data[i]
        except Exception as e:
            raise Exception('General error') from e

    def get_config_value(self, key):
        return self.default_values_dict.get(key)