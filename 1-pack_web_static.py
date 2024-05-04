from fabric.api import local
from datetime import datetime


# time0 =date.timetuple(date.today())
# print(date.today())
# print("time", time0)


# print(dt)

def do_pack():
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir versions", capture=False)
    result = local(f"tar -cvzf versions/web_static_{dt}.tgz web_static", capture=True)
    if result.succeeded:
        return "versions/web_static_{dt}.tgz"
    else:
        return None
