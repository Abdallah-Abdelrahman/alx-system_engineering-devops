# fix 'holberton' user limit
exec {'sed -i "/holberton hard/s/5/65535" /etc/security/limit.conf': path => '/bin':/usr/local/bin'}
exec {'sed -i /holberton soft/s/4/65535 /etc/security/limit.conf': path => '/bin':/usr/local/bin'}
