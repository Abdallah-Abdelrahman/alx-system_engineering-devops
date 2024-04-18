# reduce the number of failing rquest in nginx server
exec {'sed -i "s/^/\#/g" /etc/default/nginx': path => '/bin'}
