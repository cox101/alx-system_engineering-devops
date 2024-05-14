# Fix problem of high amount files opened

file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton hard nofile 65535\nholberton soft nofile 65535",
}

service { 'puppet':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/security/limits.d/holberton.conf'],
}
