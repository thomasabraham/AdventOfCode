from sys import stdin
import re

class Passport:
    def __init__(self):
        self.info = {}
        self.required_fields = [
            "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        self.valid_eye_colours = [
            "amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        
    def add_info(self, line):
        pairs = line.split(" ")
        for pair in pairs:
            key_value = pair.split(":")
            key = key_value[0]
            value = key_value[1]

            if key == "byr":
                self.info[key]=parse_int_between(value, 1920, 2002)

            elif key == "iyr":
                self.info[key]=parse_int_between(value, 2010, 2020)

            elif key == "eyr":
                self.info[key]=parse_int_between(value, 2020, 2030)

            elif key == "hgt":
                if value.endswith("in"):
                    self.info[key]=parse_int_between(value.strip("in"),59,76)
                elif value.endswith("cm"):
                    self.info[key]=parse_int_between(value.strip("cm"),150,193)
                
            elif key == "hcl":
                if re.fullmatch(r"#[\da-f]{6}", value):
                    self.info[key] = value
                
            elif key == "ecl":
                if value in self.valid_eye_colours:
                    self.info[key] = value
                
            elif key == "pid":
                if re.fullmatch(r"\d{9}", value):
                    self.info[key] = value
                
            elif key == "cid":
                self.info[key] = value

    def is_valid(self):
        for field in self.required_fields:
            if self.info.get(field, None) is None:
                return False
        return True
    
def parse_int_between(value, least, most):
    try:
        number = int(value)
        if least <= number and number <= most:
            return number
        else:
            return None
    except ValueError:
        return None
    
passport = Passport()
passport_count = 0
for line in stdin:
    if line == '\n' or line == '':
        if passport.is_valid():
            passport_count += 1
        if line == '\n':
            passport = Passport()
        else:
            break
    else:
        passport.add_info(line.strip("\n"))

print("Number of valid passports are ", passport_count)
