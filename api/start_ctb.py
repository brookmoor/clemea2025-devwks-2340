import code
import ctb

banner = "CTB Python API Shell. Type in the following to get started: \n \
    (use the managerip, username, password from the lab environment) \n \
    `>>> import ctb` \n \
    `>>> response = ctb.login(manager_ip, username, password)` \n \
    `>>> print (response.cookies)` \n"

code.interact(banner=banner, local=locals())
