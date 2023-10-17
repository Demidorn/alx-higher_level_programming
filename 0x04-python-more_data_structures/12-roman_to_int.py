#!/usr/bin/python3
def convert(letter):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for key in roman:
        if letter == key:
            return roman[key]


def roman_to_int(roman_string):

    if roman_string is None:
        return 0

    if not isinstance(roman_string, str):
        return 0
    sum = 0
    prev = 0
    for idx in range(0, len(roman_string)):
        val1, val2 = 0, 0
        val1 = convert(roman_string[idx])
        if prev == 0:
            if idx + 1 < len(roman_string):
                val2 = convert(roman_string[idx + 1])
                if val2 > val1:
                    prev = val1
                else:
                    sum = sum + val1
            else:
                sum = sum + val1
                break

        else:
            sum = sum + val1 - prev
            prev = 0

    return sum
