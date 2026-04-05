text = input("Input: ")

result = ""

for vowels in text:
    if vowels.lower() not in "aeiou":
        result += vowels

print("Output:", result)