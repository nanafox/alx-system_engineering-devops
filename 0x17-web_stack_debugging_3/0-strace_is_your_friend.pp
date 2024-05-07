# this manifest fixes a misconfiguration that caused server error 500

$settings_file='/var/www/html/wp-settings.php'
file { $settings_file:
  ensure => file,
}

exec {'fix typo in settings config':
  path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
  command => "sed -i s/phpp/php/g ${settings_file}",
  require => File[$settings_file],
}
