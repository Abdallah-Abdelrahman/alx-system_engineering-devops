# install flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  command  => 'pip3 install',
  provider => 'pip3',
}
