name = str(input("Enter your name"))
mark = int(input("Enter your mark"))
subject = str(input("Enter your subject"))

if mark > 100:
    print("invalid mark")
elif mark >= 70:
    print(f" congratulations {name}, you obtained grade A in {subject}. Your mark is {mark}.")
elif mark >= 66:
    print(f" wonderful {name}, you obtained grade B in {subject}. Your mark is {mark}.")
elif mark >= 50:
    print(f" fairly done {name}, you obtained grade C in {subject}. Your mark is {mark}.")
elif mark >= 39:
    print(f"You failed {name},you obtained grade D in {subject}. Your mark is {mark}.")
else:
    print(f"You failed {name},you obtained grade D in {subject}. Your mark is {mark}.")