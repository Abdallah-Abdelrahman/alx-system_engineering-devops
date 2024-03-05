# We’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

$host = $hostname
package {'haproxy': ensure => installed}

file_line {'default':
  ensure  => present,
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'server {',
  line    => "add_header X-Served-By ${host};",
  require => Package['nginx'],
}

service {'nginx':
  ensure => running,
  enable => true,
  rquire => Package['nginx'],
}
