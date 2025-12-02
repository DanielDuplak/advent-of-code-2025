
with open('02/input.txt') as f:
    line = f.readline().strip()
    id_ranges = line.split(',')


def part1(id_ranges):
    invalid_ids = set()
    for id_range in id_ranges:
        start, end = map(int, id_range.split('-'))
        for curr_id in range(start, end + 1):
            id_len = len(str(curr_id))
            if id_len % 2 != 0:
                continue
            if str(curr_id)[:id_len // 2] == str(curr_id)[id_len // 2:]:
                invalid_ids.add(curr_id)
    return sum(invalid_ids)

print("Part 1:", part1(id_ranges))

def is_duplicate(string, sub_string):
    string_length = len(string)
    sub_string_length = len(sub_string)
    if string_length == sub_string_length:
        return False
    if string_length % sub_string_length != 0:
        return False
    for i in range(0, string_length, sub_string_length):
        if string[i:i+sub_string_length] != sub_string:
            return False
    return True

def part2(id_ranges):
    invalid_ids = set()
    for id_range in id_ranges:
        start, end = map(int, id_range.split('-'))
        for curr_id in range(start, end + 1):
            for i in range(len(str(curr_id))):
                if is_duplicate(str(curr_id), str(curr_id)[0:i+1]):
                    invalid_ids.add(curr_id)
                    break

    return sum(invalid_ids)

print("Part 2:", part2(id_ranges))

