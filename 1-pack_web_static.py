#!/usr/bin/python3
"""
Fabric script to generate a .tgz compressed archive with the contents of
the web_static folder using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Creates a .tgz file with the contents of the web_static folder
    """

    timestamp = datetime.utcnow().strftime("%y%m%d%H%M%S")
    local("mkdir -p versions")
    filename = "versions/web_static_" + timestamp + ".tgz"

    try:
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except Exception:
        return None
