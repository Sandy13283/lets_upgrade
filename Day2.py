#Write a Python program that asks the user to enter their age
#and then prints "You are a minor" if their age is less than 18, 
#"You are an adult" if their age is greater than or equal to 18 and less than 65, 
#and "You are a senior" if their age is 65 or greater

X=int(input("Enter your age : "))
if X<18:
  print(f"hey kiddo {X}\nYou are a minor")
elif X>=18 and X<65:
  print(f"Hey {X}\nYou are an adult")
else:
  print(f"hey {X}\nYou are a senior")
