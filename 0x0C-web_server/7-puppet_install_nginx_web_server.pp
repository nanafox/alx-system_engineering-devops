# A manifest that configures an Nginx web server with the following:
# - A root page that displays "Hello World!"
# - A redirection page that redirects to https://lzcorp-landing-page.vercel.app/
# - A 404 page that displays "Ceci n'est pas une page"

$nginx_package_name = 'nginx'
$nginx_service_name = 'nginx'
$root_dir = '/usr/share/nginx/html'
$config_file = '/etc/nginx/sites-available/default'
$server_config = @(END)
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;
    root /var/www/html;

    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }

    location /redirect {
        return 301 https://lzcorp-landing-page.vercel.app/;
    }
}
END

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

package { $nginx_package_name:
  ensure  => installed,
  require => Exec['apt-get update'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package[$nginx_package_name],
}

file { "${root_dir}/404.html":
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  require => Package[$nginx_package_name],
}

file { $config_file:
  ensure  => present,
  content => $server_config,
  require => Package[$nginx_package_name],
}

exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
  path    => ['/usr/bin', '/usr/sbin'],
  require => File[$config_file],
}

service { $nginx_service_name:
  ensure  => running,
  enable  => true,
  require => Exec['nginx-restart'],
}
