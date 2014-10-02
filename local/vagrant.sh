#!/bin/bash

# If we haven't already applied the devkit, do it now
DEVKIT=/etc/puppet/modules/devkit
if [ ! -d $DEVKIT ]; then
  echo "Running devkit puppet module"
  git clone https://github.com/LandRegistry/infrastructure-puppet-devkit $DEVKIT
  puppet apply $DEVKIT/tests/optional.pp
fi

## Bash profile setup
echo "Configuring user environment"
bash_profile=/home/vagrant/.bash_profile
cat <<EOF > ${bash_profile}
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=/home/vagrant/.venv

export PATH=/vagrant/local/bin:${PATH}

cd /vagrant
/vagrant/local/bin/app-start
EOF
chown vagrant:vagrant /home/vagrant
