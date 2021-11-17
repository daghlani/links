from flask import Flask, render_template
from utils.conf_reader import cfg
from utils.decorators import auth_required
from markupsafe import escape
import os

app = Flask(__name__)



@app.route("/")
@auth_required
def index(cfg_file=cfg):
	context = cfg_file['targets']
	return render_template(
		'index.html', lists=context, cml=str.title
		)

@app.route("/2/")
@auth_required
def index2(cfg_file=cfg):
	context = cfg_file['targets']
	return render_template(
		'index2.html', lists=context, cml=str.title
		)

if __name__ == "__main__":
	extra_files= [i.strip(' ') for i in os.environ.get('LINKS_EXTRA_FILES', 'config/config.yml').split(',')]
	extra_files.append('config/config.yml')
	app.run(
		host=os.environ.get('LINKS_HOST', '0.0.0.0'),
		port=os.environ.get('LINKS_PORT', 8001),
		use_reloader = True, 
		debug = os.environ.get('LINKS_DEBUG_MODE', False), 
		extra_files= extra_files
		)
