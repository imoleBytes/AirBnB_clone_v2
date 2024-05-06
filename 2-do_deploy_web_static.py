#!/usr/bin/python3
"""fabric module"""

from fabric.api import local, put, run, sudo, cd, env
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['18.204.7.196', '100.26.212.62']

def do_pack():
    """tar the web_static contents"""
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{dt}.tgz"

    local("mkdir -p versions/")
    result = local(f"tar -cvzf {file_path} web_static", capture=True)
    if result.succeeded:
        return file_path
    return None


def do_deploy(archive_path):
    """deploy archive to remote hosts"""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp/')
    filename_ext = archive_path.split('/')[-1]
    filename = filename_ext.split('.')[0]
    run(f"sudo mkdir -p /data/web_static/releases/{filename}")
    with cd("/tmp/"):
        sudo(f"tar -xvzf {filename_ext} -C /data/web_static/releases/{filename}")
        sudo(f"rm {filename_ext}")
    sudo(f"sudo mv /data/web_static/releases/{filename}/web_static/* /data/web_static/releases/{filename}")
    sudo(f"rm -rf /data/web_static/releases/{filename}/web_static")
    sudo("rm -rf /data/web_static/current")
    sudo(f"sudo ln -s /data/web_static/releases/{filename} /data/web_static/current")


    print("New version deployed!")
    return True
