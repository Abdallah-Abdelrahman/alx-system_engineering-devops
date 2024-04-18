# fix 'holberton' user limit
exec {'sed -i "s/^/#/g" /etc/security/limit.conf': path => '/bin'}
