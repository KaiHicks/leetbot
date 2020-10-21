import json
import logging
from argparse import ArgumentParser

if __name__ == '__main__':
	arg_parser = ArgumentParser(description='Start the Leetbot')
	arg_parser.add_argument('config_path', type=str, metavar='config',
		help='Path to a .json file containing the settings')
	arg_parser.add_argument('secrets_path', type=str, metavar='secret',
		help='Path to a .secret.json file containing the secret information ' 
			'such as the discord auth token')
	
	args = arg_parser.parse_args()
	
	
	try:
		with open(args.config_path) as cf:
			config = json.load(cf)
	except FileNotFoundError:
		logging.error(f'File \'{args.config_path}\' not found!')
		exit()
	except json.decoder.JSONDecodeError:
		logging.error(f'File \'{args.config_path}\' is not a valid JSON file!')
		exit()
	try:
		with open(args.secrets_path) as sf:
			secrets = json.load(sf)
	except FileNotFoundError:
		logging.error(f'File \'{args.secrets_path}\' not found!')
		exit()
	except json.decoder.JSONDecodeError:
		logging.error(f'File \'{args.secrets_path}\' is not a valid JSON file!')
		exit()