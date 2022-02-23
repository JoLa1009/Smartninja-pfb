# homework 1.1: The mood checker

mood=input("How are you feeling today? ")
print()
if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Chin up! Everything will be fine soon for sure!")
elif mood =="excited":
    print("Try to calm down!")
elif mood == "relaxed":
    print("Great! Keep it up!")
else:
    print("I don't recognize this mood.")