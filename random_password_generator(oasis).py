import random
letters=['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')',"_","+"]
print("welcome to pasword generator")
n_letters=int(input("enter the no of letters"))
n_symbols=int(input("enter the no of symbols you want in the password"))
n_numbers=int(input("enter the no of numbers you want in the password"))

password=""
for i in range(1,n_letters+1):
    a=random.choice(letters)
    password+=a
for i in range(1,n_symbols+1):
    a=random.choice(symbols)
    password+=a
for i in range(1,n_numbers+1):
    a=random.choice(numbers)
    password+=a  
passset=set(password)
password=""
for i in passset:
    password+=i
print(f"your password is {password}")          


