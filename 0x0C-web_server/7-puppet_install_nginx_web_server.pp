# Install Nginx
package { 'nginx':
  ensure => installed,
  provider => 'apt',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => "
http {
    server {
        listen 80;
        server_name localhost;

        location / {
            return 200 'Hello World!';
        }

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }
}
",
  require => Package['nginx'],
}

# Enable the default site
nginx::resource::site { 'default':
  ensure => enabled,
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure => running,
  enable => true,
  restart => true,
  require => Nginx::Resource::Site['default'],
}
