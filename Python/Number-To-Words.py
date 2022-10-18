# Works from Zero til One Thousand!
def InWords(num):
    # We must define all unique numbers
    TillFifteen = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                  9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen"}
    # Multiples of ten to add before unique numbers
    # For Example TWENTY four, THIRTY four, SEVENTY four
    MultiplesOfTen = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
                      90: "ninty", 100: "one hundred"}

    if type(num) != int:
        return "Invalid Input"
    else:
        if num < 20:
            try:
                # Try Unique List
                return (TillFifteen[num])
            except KeyError:
                # sixTeen till nineTeen are returned by using
                # last digit added with added keyword teen
                # example: sixteen , seventeen, eighteen
                return (TillFifteen[int(str(num)[1])] + "teen")
        elif num % 10 == 0 and not (num > 100):
            # If number is exact multiple of ten
            # Fetch it from the MultiplesOfTen dictionary
            return (MultiplesOfTen[num])

        elif num < 100:
            # From 21 and above, First number represent multiple of ten
            # rest of number is handled in above code (Recursive Call)
            multiple_of_ten = MultiplesOfTen[int(str(num)[0] + "0")]
            return (multiple_of_ten + " " + InWords(int(str(num)[1:])))


        elif num < 1000:
            # From one hundred and above First number represents
            # unique number with added statement ' hundred and '
            # For Example : Three hundred and four, Six hundred and four
            # rest of number is handled in above code (Recursive Call)
            unique_number = TillFifteen[int(str(num)[0])]
            return (unique_number + " hundred and " + InWords(int(str(num)[1:])))

        else:
            # TODO
            return "One Thousand! (or above)"

print(InWords(int(input("Enter Any number:"))))

'''
Expected Outputs:

Enter Any number:5
five

Enter Any number:78
seventy eight

Enter Any number:235
two hundred and thirty five
'''
