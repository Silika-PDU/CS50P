question = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

optimized = question.strip().lower()
if optimized == "42" or optimized == "forty-two" or optimized == "forty two":
    print("Yes")
elif question == "69":
    print("nice.")
else:
    print("No")