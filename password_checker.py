has_uppercase = False
has_lowercase = False
has_digit = False
while has_lowercase == False or has_digit == False or has_uppercase == False :
  has_uppercase = False
  has_lowercase = False
  has_digit = False
  password = input("enter the password :")
  for charachter in password :
      if charachter.isupper():
        has_uppercase = True
      elif charachter.islower():
        has_lowercase = True
      elif charachter.isdigit():
        has_digit = True


  if has_uppercase and has_digit and has_lowercase :
    print("the password is valid")
  else:print("the password needs to contain an uppercase , lowercase and a digit. Try again :")