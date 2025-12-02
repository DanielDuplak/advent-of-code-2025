

with open("01/input.txt", "r") as file:
    lines = file.readlines()
    lines = [code.strip() for code in lines]
    codes = [(code[0:1], int(code[1:])) for code in lines]

def part1(codes):
    curr = 50
    count = 0
    for code in codes:
        direction, value = code
        if direction == "R":
            curr = (curr + value) % 100
        elif direction == "L":
            curr = (curr - value) % 100
        if curr == 0:
            count += 1
    return count

print("Part 1:", part1(codes))

def part2(codes):
    curr = 50
    count = 0
    for code in codes:
        for _ in range(code[1]):
            if code[0] == "R":
                curr = (curr + 1) % 100
            else: 
                curr = (curr - 1) % 100
            if curr == 0:
                count += 1
        
    return count

print("Part 2:", part2(codes))
