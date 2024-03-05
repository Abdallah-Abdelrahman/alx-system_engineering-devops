# We’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

$header = "add_header X-Served-By \$hostname;"

# Ensure Nginx is installed
package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

file_line {'default':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server {',
  line    => $header,
  require => Package['nginx'],
}

service {'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
