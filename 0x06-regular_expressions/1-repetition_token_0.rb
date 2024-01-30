#!/usr/bin/env ruby
# This script matches lines containing 2 to 5 't' in the string starting
# with 'hb' and ending with 'n'

puts ARGV[0].scan(/hbt{2,5}n/).join
