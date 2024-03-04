# We’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

package {'haproxy': ensure => installed}

file_line {'/etc/nginx/sites-enabled/default':
  ensure  => present,
  after   => 'server {',
  line    => "add_header X-Served-By \$hostname;",
  require => Package['nginx'],
}

service {'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

