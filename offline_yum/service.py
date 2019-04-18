from offline_yum.models import YumPackages
from django.conf import settings
from shell_helper import exec_shell

import os


def pack(packages: YumPackages):
    # make work dir
    root = settings["WORK_DIR"]
    install_root = os.path.join(root, "yum_empty_root")
    repo_root = os.path.join(root, "yum", packages.name)
    exec_shell("mkdir -p %s" % install_root)
    exec_shell("mkdir -p %s" % repo_root)

    # download packages
    exec_shell("yum install --downloadonly --installroot=%s --releasever=%s --downloaddir=%s %s" % (
        install_root, packages.releasever, repo_root, packages.packages))

    # create repo
    exec_shell("createrepo --database %s" % repo_root)

    # check missing dependencies
    # create configure file