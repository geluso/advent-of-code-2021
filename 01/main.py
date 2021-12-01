def part1(lines):
  increases = 0
  index = 1
  while index < len(lines):
    last_reading = int(lines[index - 1])
    this_reading = int(lines[index])
    if this_reading > last_reading:
      increases += 1
    index += 1
  return increases

def part2(lines):
  increases = -1
  prev_sum = 0

  index = 2
  while index < len(lines):
    reading_last = int(lines[index - 2])
    reading_prev = int(lines[index - 1])
    reading_this = int(lines[index])

    this_sum = reading_last + reading_prev + reading_this
    if this_sum > prev_sum:
      increases += 1
    prev_sum = this_sum
    index += 1
  return increases
  
sample_lines = [
  199,
  200,
  208,
  210,
  200,
  207,
  240,
  269,
  260,
  263
]

print(part1(sample_lines))

lines = open("./input").readlines()
print(part1(lines))

print(part2(sample_lines))

lines = open("./input").readlines()
print(part2(lines))
