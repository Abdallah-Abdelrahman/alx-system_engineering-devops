# We’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

package {'haproxy': ensure => installed}

file {'/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	add_header X-Served-By ${hostname}
	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}
}
",
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

