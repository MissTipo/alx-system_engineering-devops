#!/usr/bin/env ruby
# regular expression that matches a 10 digit phone number
puts ARGV[0].scan(/^\d{10}$/).join
