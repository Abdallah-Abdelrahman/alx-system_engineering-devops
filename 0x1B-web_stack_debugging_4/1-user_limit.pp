# fix holberton user limit
exec {'sed -i "/holberton \(soft\|hard\)/s/[0-9]\+/65535/" /etc/security/limits.conf': path => '/bin/:/usr/local/bin/'}
