#!/usr/bin/env ruby
# This script matches lines with 1 or 2 alphabets within the string "hn"

puts ARGV[0].scan(/h[a-z]{1,2}n/).join
