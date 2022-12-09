exec {'pkill':
  command => 'pkill killmenow',
   path   => '/usr/local/bin/:/bin/',
}
