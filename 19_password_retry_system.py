# 2 password retry system

attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    if password == "secret":
        print("Access Granted!")
        break
    attempts -= 1
    print(f"{attempts} attempts left")
else:
    print("Access denied!") # output if loop completes without break


