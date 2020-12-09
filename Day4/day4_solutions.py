import re


def day4_part1():
    with open("day4_input.txt") as f:
        valid_passports = 0
        passport_fields = []
        for line in f:
            passport_fields += re.findall(r"\w{3}(?=:)", line)
            if not line.strip():
                if len(passport_fields) == 8:
                    valid_passports += 1
                elif len(passport_fields) == 7 and 'cid' not in passport_fields:
                    valid_passports += 1
                passport_fields = []
                continue
        if len(passport_fields) == 8:
            valid_passports += 1
        elif len(passport_fields) == 7 and 'cid' not in passport_fields:
            valid_passports += 1
        return valid_passports


def is_passport_valid(passport):
    try:
        if len(passport.keys()) >= 7:
            if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and len(passport['ecl']) == 3:
                if 1920 <= int(passport['byr']) <= 2002:
                    if 2010 <= int(passport['iyr']) <= 2020:
                        if 2020 <= int(passport['eyr']) <= 2030:
                            if re.match(r"#[\da-z]{6} *", passport['hcl']) is not None:
                                if re.match(r"^\d{9}(?!\d)", passport['pid']) is not None:
                                    height = re.match(r"(?P<height>\d+)(?P<unit>[a-z]+)", passport['hgt'])
                                    if height is not None:
                                        if height.group('unit') == 'cm' and 150 <= int(height.group('height')) <= 193:
                                            return True
                                        elif height.group('unit') == 'in' and 59 <= int(height.group('height')) <= 76:
                                            return True
    except (KeyError, ValueError):
        return False
    return False


def day4_part2():
    with open("day4_input.txt") as f:
        valid_passports = 0
        passport = {}
        for line in f:
            for match in re.findall(r"\w{3}:[^ \n]*", line):
                key, val = match.split(":")
                passport[key] = val
            if not line.strip():
                if is_passport_valid(passport):
                    valid_passports += 1
                passport = {}
        if is_passport_valid(passport):
            valid_passports += 1
        return valid_passports


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Number of valid passports: {day4_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f"Number of valid passports: {day4_part2()}")
