# Creates a custom HTTP header response
exec { 'configure_nginx':
  command  => 'apt-get -y update; \
               apt-get -y install nginx; \
               sed -i "/listen 80 default_server;/a add_header X-Served-By \"$::hostname\";" /etc/nginx/sites-available/default; \
               service nginx restart',
  provider => shell,
  path     => '/usr/bin:/bin',  # Add necessary paths
  unless   => 'grep -q "X-Served-By" /etc/nginx/sites-available/default',
}

