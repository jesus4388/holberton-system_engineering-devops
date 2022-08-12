#Using Puppet, create a file in /tmp.
file {'/tmp/school':
  ensure  => 'file',
  path    => '/tmp/school'
  mode    => 'u=rwx,g=r,o=r',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
