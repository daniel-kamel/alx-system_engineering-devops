# Configures Nginx to add a custom header to http response

package { 'nginx':
  name     => 'nginx',
  provider => 'apt',
  ensure   => 'installed',
}


exec { 'insert line':

  command => '/usr/bin/sed -i "49i\add_header X-Served-By $HOSTNAME check;" /etc/nginx/sites-available/default',

}

exec {'start_server':

  command => '/usr/bin/sudo /usr/sbin/service nginx restart',

}
