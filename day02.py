from sys import stdin

class Password:
    def __init__(self, entry):

        splits = entry.split(": ")
        self.password = splits[1].strip("\n")
        rule = splits[0]

        rule_parts = rule.split(" ")
        self.required_letter= rule_parts[1]
        limits = rule_parts[0]

        limit_parts = limits.split("-")
        self.min = int(limit_parts[0])
        self.max = int(limit_parts[1])


    def isValidSledRentalPassword(self):
        count = self.password.count(self.required_letter)

        if self.min <= count and count <= self.max:
            return True
        else:
            return False

    def isValidTobogganPassword(self):
        min_letter = self.password[self.min-1]
        max_letter = self.password[self.max-1]
        if self.required_letter == min_letter and self.required_letter != max_letter:
            return True
        elif self.required_letter != min_letter and self.required_letter == max_letter:
            return True
        else:
            return False

    def __str__(self):
        return "Password { password=%s, required_letter=%s, min=%d, max=%d}"  % (
                self.password, self.required_letter, self.min, self.max)

validSledRentalPasswordCount=0
validTobogganPasswordCount=0

for line in stdin:
    if line == '':
        break
    password = Password(line)
    #print(password)
    if password.isValidSledRentalPassword():
        validSledRentalPasswordCount += 1
    if password.isValidTobogganPassword():
        validTobogganPasswordCount += 1

print("Number of valid SledRental passwords are ", validSledRentalPasswordCount)
print("Number of valid Toboggan passwords are ", validTobogganPasswordCount)

