#!/bin/bash

# Enable SSH password authentication
echo "Enable SSH password authentication"
sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sed -i 's/^PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
systemctl restart ssh

# Set Root password
echo "Set root password"
echo "Username: root"  # Assuming root user
echo "Password: $1"    # Assuming the password is passed as the first argument
echo -e "$1\n$1" | passwd root >/dev/null 2>&1

