def get_parsed_lines(parse)
  filename = ARGV[0]
  commands = File.readlines(filename).map { |line| parse.call(line) }
end
