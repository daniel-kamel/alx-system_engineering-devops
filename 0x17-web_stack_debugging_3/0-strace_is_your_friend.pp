# Solution for 0x17-web_stack_debugging_3 project

exec { 'fix-wordpress':
  command => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/:/usr/bin/:/usr/local/sbin/:/sbin/:/usr/sbin/',
}
