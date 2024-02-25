# ssh configuration file
file { 'config':
  path    => '~/.ssh/config',
  content => "
	Host *
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
",
  owner   => 'root',
  mode    => '0644'
}
