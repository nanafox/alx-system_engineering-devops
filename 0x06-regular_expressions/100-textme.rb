#!/usr/bin/env ruby
# This script extracts the sender, receiver and flags from TextMe log file

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
