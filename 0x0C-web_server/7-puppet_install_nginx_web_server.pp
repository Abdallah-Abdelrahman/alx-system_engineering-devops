# installed nginx and configure it according to
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page) using curl,
# it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”
# Your answer file should be a Puppet manifest containing commands to automatically,
# configure an Ubuntu machine to respect above requirements

package {'nginx': ensure => installed}

file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hellow World!',
  require => Package['nginx'],
}

file {'/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "server {

	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
	error_page 404 /404.html;
        location = /404.html {
		root /var/www/html;
                internal;
        }

 }",
  require => Package['nginx'],
}

firewall { '100 allow http':
  ensure  => present,
  action  => accept,
  proto   => 'tcp',
  port    => '80',
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}
