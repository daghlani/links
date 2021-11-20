from flask import Flask, render_template
from utils.conf_reader import config
from utils.decorators import auth_required
from utils.htpasswd import HtpasswdFile
from markupsafe import escape
from optparse import OptionParser
import sys
import os

app = Flask(__name__)
HTfile = HtpasswdFile(config.config_list['global']['HTPASS_FILE_ADDRESS'])
pass_file = HTfile.filename


@app.route("/")
@auth_required(htpasswd_obj=HTfile, enable=config.config_list['global']['BASIC_AUTH'])
def index(cfg_file=config.target_list):
    context = cfg_file
    return render_template(
        'index.html', lists=context, cml=str.title
    )


@app.route("/2/")
@auth_required(htpasswd_obj=HTfile)
def index2(cfg_file=config.target_list):
    context = cfg_file
    return render_template(
        'index2.html', lists=context, cml=str.title
    )


def main():
    """%prog htpasswd -u | -d username password
    Create or update | delete an user"""
    parser = OptionParser(usage=main.__doc__)
    parser.add_option('-u', action='store_true', dest='update', default=False, help='Create or update a user.')
    parser.add_option('-d', action='store_true', dest='delete_user', default=False, help='Remove the given user')

    def syntax_error(msg):
        """Utility function for displaying fatal error messages with usage
        help.
        """
        sys.stderr.write("Syntax error: " + msg)
        sys.stderr.write(parser.get_usage())
        sys.exit(1)

    options, args = parser.parse_args()
    if options.update:
        if len(args) != 3:
            syntax_error("Incorrect number of arguments.\n")
        HTfile.update(args[1], args[2])
        HTfile.save()
        sys.exit()

    if options.delete_user:
        HTfile.delete(username=args[1])
        HTfile.save()
        sys.exit()


if __name__ == "__main__":
    # Get extra file from environ variable.
    extra_files = [i.strip(' ') for i in os.environ.get('LINKS_EXTRA_FILES', 'config/config.yml').split(',')]
    # add config file to extra files
    extra_files.append('config/config.yml')
    extra_files.append(pass_file)
    if len(sys.argv) > 1:
        if sys.argv[1] == 'htpasswd':
            main()
        else:
            print('usage: python app.py htpasswd -u <username> <password>')
    else:
        app.run(
            host=os.environ.get('LINKS_HOST', config.config_list['global']['LINKS_HOST']),
            port=os.environ.get('LINKS_PORT', config.config_list['global']['LINKS_PORT']),
            use_reloader=True,
            debug=os.environ.get('LINKS_DEBUG_MODE', config.config_list['global']['LINKS_DEBUG_MODE']),
            extra_files=extra_files
        )
