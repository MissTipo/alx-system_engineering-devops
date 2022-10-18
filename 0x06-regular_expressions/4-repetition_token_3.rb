#!/usr/bin/env ruby
# A regular expression that will match hbttttn
puts ARGV[0].scan(/hbt{0,4}n/).join
