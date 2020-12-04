f = open("input.txt", "r")
input_values = f.read().split("\n\n")

def precheck_passports():
    correct_passports = 0
    passports = []

    for passport in input_values:
        passport = passport.replace("\n", " ")

        passport_fieldvalue = passport.split(" ")
        fields = []
        field_count = 0

        for field in passport_fieldvalue:
            fields.append(field.split(":")[0])

        field_count = len(fields)

        if field_count == 8:
            correct_passports += 1
            passports.append(passport)
        elif field_count == 7 and 'cid' not in fields:
            correct_passports += 1
            passports.append(passport)
        else:
            continue

    print("Correct passports: " + str(correct_passports))

    return passports

def validate_passport(passports):
    validated_passports = 0

    for passport in passports:
        passport_fieldvalue = passport.split(" ")
        fields = []
        correct_data = 0

        for data in passport_fieldvalue:
            field = data.split(":")[0]
            value = data.split(":")[1]

            fields.append(field)

            if field == "byr":
                byr = int(value)

                if value.isdigit() == False:
                    break
                elif byr < 1920 or byr > 2002:
                    break
            elif field == "iyr":
                iyr = int(value)

                if value.isdigit() == False:
                    break
                elif iyr < 2010 or iyr > 2020:
                    break
            elif field == "eyr":
                eyr = int(value)

                if value.isdigit() == False:
                    break
                elif eyr < 2020 or eyr > 2030:
                    break
            elif field == "hgt":
                ident = value[-2:]
                hgt = int(value[:-2])

                if ident == "cm":
                    if hgt < 150 or hgt > 193:
                        break
                elif ident == "in":
                    if hgt < 59 or hgt > 76:
                        break
                else:
                    break
            elif field == "hcl":
                chars = set('0123456789abcdef')
                hcl = value[1:len(value)]

                if value.startswith("#") == False:
                    break
                elif any(c not in '0123456789abcdef' for c in hcl):
                    break
                elif(len(hcl) < 6 or len(hcl) > 6):
                    break
            elif field == "ecl":
                allowed_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

                if value not in allowed_values:
                    break
            elif field == "pid":
                if len(value) < 9 or len(value) > 9:
                    break
                elif value.isdigit() == False:
                    break
            elif field == "cid":
                continue
                
            correct_data += 1
        
        if correct_data == 7:
            validated_passports += 1

    print(validated_passports)


passports = precheck_passports()
validate_passport(passports)