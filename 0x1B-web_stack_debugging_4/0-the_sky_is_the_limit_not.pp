# Puppet code
exec { 'change-limit':
    command  => "sed -i 's/-n 15/-n 7000/g' /etc/default/nginx",
    provider => shell,
}
exec { 'restart':
    command  => '/etc/init.d/nginx restart',
    provider => shell,
}
