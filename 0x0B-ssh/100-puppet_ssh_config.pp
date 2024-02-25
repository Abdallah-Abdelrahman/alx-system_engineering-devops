# ssh configuration file
file { '/home/ubuntu/.ssh/config':
  content => "
	Host *
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
",
  owner   => 'root',
  group   => 'root',
  mode    => '0644'
}
