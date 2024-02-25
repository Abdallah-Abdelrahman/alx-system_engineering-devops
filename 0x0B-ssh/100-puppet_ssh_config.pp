# ssh configuration file
file {'/etc/ssh':
  ensure => directory
}
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
	    ${file('/etc/ssh/ssh_config')}\n
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
",
  owner   => 'root',
  group   => 'root',
  mode    => '0644'
}
