#!/usr/bin/python3
"""fabric module"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """tar the web_static contents"""
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{dt}.tgz"

    local("mkdir -p versions/")
    result = local(f"tar -cvzf {file_path} web_static", capture=True)
    if result.succeeded:
        return file_path
    return None