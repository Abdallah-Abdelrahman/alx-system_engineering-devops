# ssh configuration file
file { 'config':
  path    => '.ssh/config',
  content => "
	Host *
	    Hostname 52.91.118.253
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
",
}
