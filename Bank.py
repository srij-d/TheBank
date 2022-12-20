import sys
import os

print("".center(90, "="))
print(" WELCOME TOO S-S BANK ".center(90, "~"))
print("".center(90, "="))
print("\n")
option = input("Options:\n\n1 ~ Create Account\n\n2 ~ Login\n\n")
f = open("BankAccounts.txt", "r+")
fi = "BankAccounts.txt"
listtoappend = []
listtofind = []
end = 0
accountline = []
data = []

#################################### ~~ Creating account ~~ ####################################

if option == "1":
    name = input("Create a username:\n")
    DOB = input("Enter your Date of Birth:\n")
    password = input("Create a password:\n")
    repassword = input("Enter your password for confirmation:\n")
    while repassword != password:
        print("Your Password did not match what you confirmed.\n")
        password = input("Create a password:\n")
        repassword = input("Enter your password for confirmation:\n")
    while name == password:
        print("Your password cannot be the same as your username")
        password = input("Create a password:\n")
        repassword = input("Enter your password for confirmation:\n")
    firstmoney = input("Deposit money:\n£")
    if firstmoney == "":
        firstmoney = 0
    loan = '0'
    listtoappend.append(name)
    listtoappend.append(DOB)
    listtoappend.append(password)
    listtoappend.append(firstmoney)
    listtoappend.append(loan)
    fakelist = []
    for line in f.readlines():
        fakelist = line.replace("[", "").replace("'", "").replace(",", "").replace("]", "").split(" ")
        if name == fakelist[0]:
            print("Sorry, this username already exists")
            sys.exit()
    f.write(str(listtoappend))
    f.write(str("\n"))
    print("Thank you for making an account with S-S Bank")
    f.close()
    sys.exit()

#################################### ~~ Login for account ~~ ####################################

elif option == "2":
    name = input("Enter your username:\n")
    DOB = input("Enter your Date of Birth:\n")
    password = input("Enter your password:\n")
    listtofind.append(name)
    listtofind.append(DOB)
    listtofind.append(password)
    fakelist = []
    if os.stat(fi).st_size != 0:
        for line in f.readlines():
            fakelist = line.replace("[", "").replace("'", "").replace(",", "").replace("]", "").split(" ")
            if name == fakelist[0] and fakelist[1] == DOB and fakelist[2] == password:
                print("Opening Account")
                end = end + 1
                accountline = line.replace("[", "").replace("'", "").replace(",", "").replace("]", "").split(" ")
                break
        if end == 0:
            print("This account does not exist")
            sys.exit()
    else:
        print("This account does not exist")
        sys.exit()
else:
  print("That command does not exist")
  sys.exit()

f.close()

#################################### ~~ Withdrawal ~~ ####################################

f = open("BankAccounts.txt", "r+")

option1 = input("What would you like to do in your account?\n1 ~ Withdrawal\n2 ~ Deposit\n3 ~ Loan\n4 ~ Delete Account\n\n")

if option1 == "1":
    new = accountline[4].strip("\n")
    new = accountline[4]
    print("\nBalance: £", accountline[3])
    withdraw = int(input("Withdraw:\n£"))
    e = int(accountline[3]) - withdraw
    accountline[3] = str(e)
    data.append(accountline)
    print("Current Balance: £", accountline[3])
    fr = open("BankAccounts.txt", "r+")
    fa = open("BankAccounts.txt", "a")
    frl = fr.readline()
    while frl != "":
        if accountline[2] and accountline[1] and accountline[0] in frl:
            z = 1
        else:
            p = frl.replace("[", "").replace("'", "").replace(",", "").replace("]", "").split(" ")
            data.append(p)
        frl = fr.readline()
    for i in data:
        l = i[4].strip("\n")
        h = i
        h.remove(h[4])
        h.insert(4,l)
        position = data.index(i)
        data.remove(i)
        data.insert(position,h)
    fr.truncate(0)
    fr.close()
    for j in data:
        fa.write(str(j)+"\n")
    fa.close()

#################################### ~~ Deposits ~~ ####################################

elif option1 == "2":
    newline = accountline[4].strip("\n")
    newline = accountline[4]
    print("\nBalance: £", accountline[3])
    deposit = int(input("Deposit:\n£"))
    e = int(accountline[3]) + deposit
    accountline[3] = str(e)
    data.append(accountline)
    print("Current Balance: £", accountline[3])
    fr = open("BankAccounts.txt", "r+")
    fa = open("BankAccounts.txt", "a")
    frl = fr.readline()
    while frl != "":
        if accountline[2] and accountline[1] and accountline[0] in frl:
            z = 1
        else:
            p = frl.replace("[", "").replace("'", "").replace(",", "").replace("]", "").split(" ")
            data.append(p)
        frl = fr.readline()
    for i in data:
        l = i[4].strip("\n")
        h = i
        h.remove(h[4])
        h.insert(4, l)
        position = data.index(i)
        data.remove(i)
        data.insert(position, h)
    fr.truncate(0)
    fr.close()
    for j in data:
        fa.write(str(j) + "\n")
    fa.close()

#################################### ~~ Loans ~~ ####################################

elif option1 == "3":
    n = accountline[4].strip("\n")
    n = accountline[4]
    print("\nBalance: £", accountline[3])
    loan = int(input("Loan:\n£"))
    e = int(accountline[4]) + loan
    accountline[4] = str(e)
    data.append(accountline)
    print("Current amount for loan: £", accountline[4])
    print("\nYou will have to pay us back in 6 months (with interest) ")
    fr = open("BankAccounts.txt", "r+")
    fa = open("BankAccounts.txt", "a")
    frl = fr.readline()
    while frl != "":
        if accountline[2] and accountline[1] and accountline[0] in frl:
            z = 1
        else:
            p = frl.replace("[", "").replace("'", "").replace(",", "").replace("]", "").split(" ")
            data.append(p)
        frl = fr.readline()
    for i in data:
        l = i[4].strip("\n")
        h = i
        h.remove(h[4])
        h.insert(4, l)
        position = data.index(i)
        data.remove(i)
        data.insert(position, h)
    fr.truncate(0)
    fr.close()
    for j in data:
        fa.write(str(j) + "\n")
    fa.close()

#################################### ~~ Deleting account ~~ ####################################

elif option1 == "4":
  rusure = input("Are you sure you want to terminate your account? You will not be able to get it back after termination(Y/N):\n").lower()
  if rusure == "y":
    with open("BankAccounts.txt",'r') as file:
        lines = file.readlines()
    
    with open("BankAccounts.txt",'w') as file:
      for line in lines:
    
        if line.find(name) != -1:
          pass
        else:
          file.write(line)
    print("ACCOUNT DELETED")
  elif rusure == "n":
    print("Account termination has been cancelled")
f.close()
