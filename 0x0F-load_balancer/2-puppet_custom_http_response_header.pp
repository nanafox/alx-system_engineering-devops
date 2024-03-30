# This manifest configures an Ubuntu server with the Nginx web server and a
# custom response header `X-Served-By` that contains the hostname of the server
# that served the request.

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
  require => Package['nginx'],
}

package { 'nginx':
  ensure => installed,
}

# add the hostname as the custom header
file { '/etc/nginx/conf.d/custom_response_headers.conf':
  ensure  => file,
  content => "add_header X-Served-By ${::facts['networking']['hostname']};\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# restart the server
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  require   => Package['nginx'],
}
