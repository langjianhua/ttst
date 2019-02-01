from pip._internal.utils.misc import get_installed_distributions
from subprocess import call

for dist in get_installed_distributions():
    print(dist)
    print(dist.project_name)
    call("pip3 install --upgrade  "+dist.project_name,shell=True)