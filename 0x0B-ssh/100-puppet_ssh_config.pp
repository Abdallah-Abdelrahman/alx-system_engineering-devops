# ssh configuration file
file { '/ssh/ssh_config':
  content => "
	Host *
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
",
  owner   => 'root',
  group   => 'root',
  mode    => '0644'
}
