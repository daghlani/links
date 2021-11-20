import configparser
import yaml
import json

# ----------------------------------------------------------------------------------------------------------------------


class Config(object):
	def __init__(self, file_addr):
		super(Config, self).__init__()
		self.file_addr = file_addr
		self.target_tag = 'targets'
		self.config_tag = 'configs'
		self.target_list = self.yml_reader(self.target_tag)
		self.config_list = self.yml_reader(self.config_tag)

	def yml_reader(self, item: str):
		with open(self.file_addr) as file:
			yml_list = yaml.load(file, Loader=yaml.FullLoader)
			return yml_list[item]		


config = Config('config/config.yml')
