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

    new_full_path = f"/data/web_static/releases/{filename}"

    run(f"sudo mkdir -p {new_full_path}")
    with cd("/tmp/"):
        sudo(f"tar -xvzf {filename_ext} -C {new_full_path}")
        sudo(f"rm {filename_ext}")
    sudo(f"sudo mv {new_full_path}/web_static/* {new_full_path}")
    sudo(f"rm -rf {new_full_path}/web_static")
    sudo("rm -rf /data/web_static/current")
    sudo(f"sudo ln -s {new_full_path} /data/web_static/current")

    print("New version deployed!")
    return True


def deploy():
    path_to_archive = do_pack()

    if path_to_archive is None:
        return False
    return do_deploy(path_to_archive)
