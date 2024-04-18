# fix 'holberton' user limit
exec {'sed -i "s/\d+/65535/g" /etc/security/limit.conf': path => '/bin'}
