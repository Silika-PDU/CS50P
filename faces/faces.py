#https://www.w3schools.com/python/ref_string_replace.asp
#https://www.w3schools.com/python/python_functions.asp

def face_conv(user_input):
    return user_input.replace(":)", "🙂").replace(":(", "🙁")

def main():
    print(face_conv(input("speak ")))

main()