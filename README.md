# RPMPackageBuilder
An RPM package builder.

### Requirements ###

Note: Some of these packages are installed by default on RHEL, CentOS and Fedora.

- gcc
- rpm-build
- rpm-devel
- rpmlint
- make
- python
- bash
- coreutils
- diffutils
- patch
- rpmdevtools

### Instructions ####

To create an RPM package from the spec file please execute the "create_rpm_package.sh" script. Below is an example on how to execute the script. A built RPM package will be saved in your current working directory.

- $ ./create_rpm_package.sh

A pre-built package is available on the releases, taged "v1.0".