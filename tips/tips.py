def dollars_to_float(dllr):
    return float(dllr[1:])

def percent_to_float(perc):
    return float(perc[:-1]) / 100

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()


#https://www.w3schools.com/python/python_strings_slicing.asp