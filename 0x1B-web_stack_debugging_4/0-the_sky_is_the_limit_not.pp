file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}

# In your nginx.conf.erb template, replace the line defining worker_processes with:
# worker_processes 7;

