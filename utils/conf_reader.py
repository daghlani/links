import configparser
import yaml
import json

# ----------------------------------------------------------------------------------------------------------------------
def yml_reader(file_addr: str):
	with open(file_addr) as file:
		target_list = yaml.load(file, Loader=yaml.FullLoader)
		return target_list

cfg = yml_reader('config/config.yml')