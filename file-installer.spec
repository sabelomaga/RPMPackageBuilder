Name:       file-installer
Version:    1
Release:    1
Summary:    Simple RPM package to install a file in /etc directory
License:    MIT License

%description
This is a simple RPM package that installs a file in /etc directory.

%prep
# Nothing to prep, no source code.

%build
DATE_TIME=$(date)
HOSTNAME=$(hostname)
PRINT_DATE_TIME=$(echo "Installation date/time: $DATE_TIME")
PRINT_HOSTNAME=$(echo "Hostname: $HOSTNAME")
echo $PRINT_DATE_TIME > challenge
echo $PRINT_HOSTNAME >> challenge

%install
mkdir -p %{buildroot}/etc
install -m 664 challenge %{buildroot}/etc/challenge

%files
/etc/challenge

%changelog