# offline-installer
pack software media for install offline

## supported package manager system
- yum
- pip
- docker
- coda

## yum

### How it works
First, you need install some yum plugin on the pack host
``` 
yum install yum-plugin-downloadonly yum-utils createrepo
```

For packing all packages and thire dependencies, we need prepare two empty dirs. One to be the yum install root and other one to be the yum repo root
```
mkdir $INSTALL_ROOT
mkdir $REPO_ROOT
```

download them
```
yum install --downloadonly --installroot=$INSTALL_ROOT --releasever=$RELEASEVER --downloaddir=$REPO_ROOT <YOUR PACKAGE HERE>
```

Generate the metadata needed to turn our new pile of RPMs into a YUM repo and clean up the stuff we no longer need.
```
createrepo --database $REPO_ROOT
rm -rf $INSTALL_ROOT
```

Create the repo configure file
```
cat <<EOF > /etc/yum.repos.d/offline.repo
[offline]
name=<any thing you want>
baseurl=file://$REPO_ROOT
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-$RELEASEVER
EOF
```

To check the missing dependencies:
```
repoclosure --repoid=offline
```

Reference: https://unix.stackexchange.com/questions/259640/how-to-use-yum-to-get-all-rpms-required-for-offline-use

