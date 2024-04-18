# reduce the number of failing rquest in nginx server

# prepend a comment symbol
exec {'sed -i "s/^/#/g" /etc/default/nginx': path => '/bin'}

# restart nginx
exec {'sudo service nginx restart': path => ['/usr/bin/', '/usr/sbin/']}
