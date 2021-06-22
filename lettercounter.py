print("Welcome to the Letter Counter App")
name = input("\nWhat is your name?: ").title().strip()
if name == "Nurin":
    name = "Bubbalington"
print("Hello " + name + "!")
print("I will count the number of times a specific letter appears in your message")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count: ")

#standarize the letters
message = message.lower()
letter = letter.lower()
number = message.count(letter)

print(name + " your message has " + str(number) + " " + letter + "'s in it.")

