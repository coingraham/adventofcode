import re

from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=4)

example = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

# passports = puzzle.input_data.split("\n")
passports = example.split("\n")


reference = {
    "byr": 0,
    "iyr": 1,
    "eyr": 2,
    "hgt": 3,
    "hcl": 4,
    "ecl": 5,
    "pid": 6,
    "cid": 7
}


def collect_passports(input_data):
    docket = []
    passport = {}
    for line in input_data:
        if line != '':
            for item in line.split(" "):
                field, value = item.split(":")
                passport[field] = value
            continue

        docket.append(passport.copy())
        passport.clear()

    return docket


def validate_passports(docket, strict):
    needed_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0

    for passport in docket:
        if not strict:
            passport_set = set(passport)
            if needed_fields == set(passport):
                valid += 1

    return valid


def check_field(field, value):
    if field == "byr":
        return 1920 <= int(value) <= 2002
    if field == "iyr":
        return 2010 <= int(value) <= 2020
    if field == "eyr":
        return 2020 <= int(value) <= 2030
    if field == "hgt":
        height = value[0:-2]
        if re.search('cm', value):
            return 150 <= int(height) <= 193
        if re.search('in', value):
            return 59 <= int(height) <= 76
        return False
    if field == "hcl":
        return bool(re.search('#[a-f0-9]{6}', value))
    if field == "ecl":
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if field == "pid":
        return bool(re.search('^[0-9]{9}$', value))
    if field == "cid":
        return True


def part_one(passports):
    valid = 0
    template_passport = [False, False, False, False, False, False, False, True]
    current_passport = template_passport.copy()
    for items in passports:
        if items == '':
            if all(current_passport):
                valid += 1

            current_passport = template_passport.copy()
            continue

        records = items.split(" ")
        for record in records:
            field = record.split(":")[0]
            current_passport[reference[field]] = True

    if all(current_passport):
        valid += 1

    return valid


def part_two(passports):
    valid = 0
    template_passport = [False, False, False, False, False, False, False, True]
    current_passport = template_passport.copy()
    for items in passports:
        if items == '':
            if all(current_passport):
                valid += 1

            current_passport = template_passport.copy()
            continue

        records = items.split(" ")
        for record in records:
            field = record.split(":")[0]
            value = record.split(":")[1]
            current_passport[reference[field]] = check_field(field, value)

    if all(current_passport):
        valid += 1

    return valid


docket = collect_passports(passports)
strict = False
print(validate_passports(docket, strict))
# print(part_one(passports))
# print(part_two(passports))
