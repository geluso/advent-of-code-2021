def part1(lines):
  position = 0
  depth = 0
  for line in lines:
    direction, distance = line.split(" ")
    if direction == "forward":
      position += int(distance)
    elif direction == "down":
      depth += int(distance)
    elif direction == "up":
      depth -= int(distance)
  print(position, depth, position * depth)

def part2(lines):
  position = 0
  depth = 0
  aim = 0
  for line in lines:
    direction, distance = line.split(" ")
    if direction == "forward":
      position += int(distance)
      depth += aim * int(distance)
    elif direction == "down":
      aim += int(distance)
    elif direction == "up":
      aim -= int(distance)
  print(position, depth, position * depth)
  
sample_lines = open("./sample").readlines()
print(part1(sample_lines))

lines = open("./input").readlines()
print(part1(lines))

print(part2(sample_lines))

lines = open("./input").readlines()
print(part2(lines))
