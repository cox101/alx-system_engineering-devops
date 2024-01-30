#!/usr/bin/env ruby

def match_school?(text)
  # Regular expression to match the word "School" case-insensitively
  regex = /School/i

  # Find all matches in the text
  matches = text.scan(regex)

  if matches.empty?
    puts "The text does not contain the word 'School'."
  else
    puts "Matches found: #{matches.join(', ')}"
  end
end

# Check if an argument is provided
if ARGV.empty?
  puts "Please provide a text argument."
else
  # Get the first command line argument
  input_text = ARGV[0]

  # Call the method to match the word "School"
  match_school?(input_text)
end

