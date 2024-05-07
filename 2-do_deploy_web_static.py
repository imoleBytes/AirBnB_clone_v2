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


# def do_deploy(archive_path):
#     """deploy archive to remote hosts"""
#     if not os.path.exists(archive_path):
#         return False
#     put(archive_path, '/tmp/')
#     filename_ext = archive_path.split('/')[-1]
#     filename = filename_ext.split('.')[0]

#     new_full_path = f"/data/web_static/releases/{filename}"

#     run(f"sudo mkdir -p {new_full_path}")
#     with cd("/tmp/"):
#         sudo(f"tar -xvzf {filename_ext} -C {new_full_path}")
#         sudo(f"rm {filename_ext}")
#     sudo(f"sudo mv {new_full_path}/web_static/* {new_full_path}")
#     sudo(f"rm -rf {new_full_path}/web_static")
#     sudo("rm -rf /data/web_static/current")
#     sudo(f"sudo ln -s {new_full_path} /data/web_static/current")

#     print("New version deployed!")
#     return True


def do_deploy(archive_path):
    """This function distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    # upload the archive file to /tmp/ of the servers

    try:  # to check if any error occur
        file_name_with_ext = os.path.basename(archive_path)
        file_name_without_ext = file_name_with_ext.split('.')[0]
        new_path_to_dir = f"/data/web_static/releases/{file_name_without_ext}"
        symbolic_link = "/data/web_static/current"

        put(archive_path, "/tmp/", use_sudo=True)
        run(f"sudo mkdir -p {new_path_to_dir}")

        with cd("/tmp/"):
            run(f"sudo tar -xvzf {file_name_with_ext} -C {new_path_to_dir}")
            sudo(f"rm {file_name_with_ext}")
        with cd(f"{new_path_to_dir}/"):
            sudo(f"mv web_static/* .")
            sudo(f"rm -rf web_static")
        if os.path.exists(symbolic_link):
            sudo(f"rm {symbolic_link}")
        sudo(f"ln -s {new_path_to_dir} {symbolic_link}")

        sudo("service nginx restart")
        print("New version deployed!")

        return True
    except Exception:
        return False  # returns False if any error occurs
