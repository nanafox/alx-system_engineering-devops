# This manifest is configures the SSH client to use the SSH key for the user

$config = "IdentityFile ~/.ssh/school
PubKeyAuthentication yes
PasswordAuthentication no
"

file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => $config,
}
