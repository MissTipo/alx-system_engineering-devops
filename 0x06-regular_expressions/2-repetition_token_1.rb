#!/usr/bin/env ruby
#Find the regular expression that will match hbbbtn
puts ARGV[0].scan(/hb{0,3}tn/).join
