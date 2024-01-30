#!/usr/bin/env ruby

# Use the match method with the regular expression
match_data = ARGV[0].match(/hbt{2,5}n/)

# Check if a match is found
if match_data
  puts "Match found: #{match_data[0]}"
else
  puts "No match found."
end
