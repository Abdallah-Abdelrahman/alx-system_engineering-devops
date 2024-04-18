# reduce the number of failing rquest in nginx server
exec {'sed -i "s/15/65535/g" /etc/default/nginx': path => '/bin'}
