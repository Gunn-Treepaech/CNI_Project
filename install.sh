#!/bin/bash

# Enable SSH password authentication
echo "Enable SSH password authentication"
sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sed -i 's/^PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
systemctl restart ssh

# Set Root password
echo "Set root password"
echo "Username: $1"
echo "Password: $2"
echo -e "$2\n$2" | passwd $1 >/dev/null 2>&1

