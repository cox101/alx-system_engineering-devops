#!/usr/bin/env ruby

#Output the matches of the word "School" (case-insensitive) from the command line argument

puts ARGV[0].scan(/School/i).join

