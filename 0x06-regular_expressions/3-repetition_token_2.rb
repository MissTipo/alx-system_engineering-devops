#!/usr/bin/env ruby
# A regular expression that will match hbttttn
puts ARGV[0].scan(/hbt{1,4}n/).join
