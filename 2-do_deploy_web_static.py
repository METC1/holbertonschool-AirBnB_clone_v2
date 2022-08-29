#!/usr/bin/python3
"""
Script that distributes an archive based on 1-pack_web_static.py created
to servers usind do_deploy
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['', '']


def do_deploy(archive_path):
    """
    Function that uploads web_staticyyyymmddhhmmss.tgz file to server
    uncompress files and updates symlink and deletes file
    """

    filename = archive_path.split("/")[-1]
    filename_noext = filename.split(".")[0]
    dirname = '/data/web_static/releases/' + filename_noext + '/'

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(dirname))
        run('tar -xzf /tmp/{} -C {}'.format(filename, dirname))
        run('rm /tmp/{}.tgz'.format(filename))
        run('mv {}web_static/* {}'.format(dirname, dirname))
        run('ln -sfn {} /data/web_static/current'.format(dirname))
        return True
    except Exception:
        return False
