# creates a a file in /tmp
package {'install_flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => pip3,
  command  => '/usr/bin/pip3',
}
