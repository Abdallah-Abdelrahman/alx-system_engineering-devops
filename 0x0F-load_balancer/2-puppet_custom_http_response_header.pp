# We’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

package { 'nginx':ensure  => installed}

file_line { '/etc/nginx/sites-available/default':
  path    => '/etc/nginx/sites-available/default',
  line    => "add_header X-Served-By ${hostname};",
  match   => 'add_header',
  after   => 'server {',
  require => Package['nginx'],
}

# restart the service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File_line['/etc/nginx/sites-available/default']
}
