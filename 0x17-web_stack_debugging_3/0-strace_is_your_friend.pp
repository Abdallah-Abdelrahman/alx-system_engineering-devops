# Fix 500 status error
$powered_by = 'Header set X-Powered-By "PHP/5.5.9-1ubuntu4.21"'
$link = 'Header set Link "<http://127.0.0.1/?rest_route=/>; rel=\"https://api.w.org/\""'
$content_type = 'Header set Content-Type "text/html; charset=UTF-8"'
$index = '<title>Holberton &#8211; Just another WordPress site</title>
    <link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
    <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
    '

file { '/etc/apache2/sites-enabled/000-default.conf':
  ensure  => present,
  content => "
<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	ServerName localhost

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html
	<Directory "/var/www/html">
          ${powered_by}\n
          ${link}\n
          ${content_type}\n
  </Directory>
  ErrorLog \${APACHE_LOG_DIR}/error.log
	CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

",
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => $index,
}

exec {'sudo a2enmod headers': path => '/usr/bin/sudo'}
exec {'service apache2 restart': path => '/usr/sbin/service'}
