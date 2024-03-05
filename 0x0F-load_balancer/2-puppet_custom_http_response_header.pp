# We’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec {'update': command => '/usr/bin/apt-get update'}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line { '/etc/nginx/sites-enabled/default':
  line    => "add_header X-Served-By ${hostname};",
  match   => 'add_header',
  after   => 'server {',
  require => Package['nginx'],
}

# restart the service
service { 'nginx':
  ensure    => running,
  enable    => true,
}
