#https://cs50.harvard.edu/python/psets/0/einstein/
#https://www.w3schools.com/python/ref_exception_valueerror.asp

try:
    m = int(input("what is your mass (in kilograms)? "))
    c = 300000000 #speed of light (m/s)
    E = m * c**2
    print(E)

except ValueError:
    print("Only Integers Accepted")
except:
    print("An Error Occured")




