# fix 'holberton' user limit
exec {'sed -i "/holberton \(hard|soft\)/s/[0-9]\+/65535" /etc/security/limit.conf': path => '/bin'}
