#!/usr/bin/env ruby

# Check if the argument matches the pattern /hbt{2,5}n/
match_result = ARGV[0].match(/hbt{2,5}n/)

# Output the match result
puts match_result ? "Match found: #{match_result[0]}" : "No match found"

