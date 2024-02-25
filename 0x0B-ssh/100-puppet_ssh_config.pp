# ssh configuration file
file { 'config':
  path    => "${facts['user_home']}/.ssh/config",
  content => "
	Host *
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
",
  owner   => 'root',
  mode    => '0644'
}
