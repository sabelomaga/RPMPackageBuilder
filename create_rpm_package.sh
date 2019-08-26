#!/bin/bash

if [ ! -d "~/rpmbuild" ] 
then
    rpmdev-setuptree
    rpmbuild -ba file-installer.spec
    mv ~/rpmbuild/RPMS/x86_64/file-installer-1-1.x86_64.rpm .
else
   rpmbuild -ba file-installer.spec
   mv ~/rpmbuild/RPMS/x86_64/file-installer-1-1.x86_64.rpm .
fi