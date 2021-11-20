#!/usr/local/bin/python
"""Replacement for htpasswd"""
# Original author: Eli Carter

import os
import sys
# import random
from utils.conf_reader import config

try:
    import crypt
except ImportError:
    try:
        import fcrypt as crypt
    except ImportError:
        sys.stderr.write("Cannot find a crypt module.  "
                         "Possibly http://carey.geek.nz/code/python-fcrypt/\n")
        sys.exit(1)


def salt(user):
    return user[:2]


def crypt_user(user, password):
    return crypt.crypt(password, salt(user))


class HtpasswdFile:
    """A class for manipulating htpasswd files."""

    def __init__(self, filename, create=False):
        self.entries = []
        self.users = []
        self.filename = filename + '.pass' if filename is not None else 'htpasswd.pass'
        if not create:
            if os.path.exists(self.filename):
                self.load()
            else:
                self.save()

    def load(self):
        """Read the htpasswd file into memory."""
        lines = open(self.filename, 'r').readlines()
        self.entries = []
        for line in lines:
            username, pwhash = line.split(':')
            entry = [username, pwhash.rstrip()]
            self.entries.append(entry)
        self.save()

    def save(self):
        """Write the htpasswd file to disk"""
        admin_pass = config.config_list['global']['LINKS_ADMIN_PASS']
        admin_pass = admin_pass if admin_pass is not None else 'LinksAdminPass'
        self.update('admin', os.environ.get('LINKS_ADMIN_PASS', admin_pass))
        open(self.filename, 'w').writelines(["%s:%s\n" % (entry[0], entry[1])
                                             for entry in self.entries])

    def update(self, username, password):
        """Replace the entry for the given user, or add it if new."""
        pwhash = crypt_user(username, password)
        matching_entries = [entry for entry in self.entries
                            if entry[0] == username]
        if matching_entries:
            matching_entries[0][1] = pwhash
        else:
            self.entries.append([username, pwhash])

    def delete(self, username):
        """Remove the entry for the given user."""
        self.entries = [entry for entry in self.entries
                        if entry[0] != username]

    def user_is_valid(self, passed_user, passed_pass):
        self.users = [entry[0] for entry in self.entries]
        if str(passed_user) in str(self.users):
            matching_entries = [entry for entry in self.entries if crypt_user(passed_user, passed_pass) == entry[1]]
            if len(matching_entries) == 1:
                return True
            else:
                return False
        else:
            raise Exception("%s does not exist" % passed_user)

