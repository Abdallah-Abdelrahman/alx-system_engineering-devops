# We’d like you to automate the task of creating a custom HTTP header response, but with Puppet.


exec {'update': command => '/usr/bin/apt-get update'}

# Ensure Nginx is installed
package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

# Define the custom response header
$header = "\n\tadd_header X-Served-By \$hostname;\n"

# Add the custom header to the Nginx configuration
file_line { 'nginx_header':
  path    => '/etc/nginx/sites-available/default',
  line    => $header,
  match   => '^\\s*add_header',
  after   => 'server {',
  require => Package['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['nginx_header'],
}
