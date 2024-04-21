# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => 'present',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

file_line { 'ssh_identity_file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}

file_line { 'ssh_password_authentication':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}
