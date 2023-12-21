import re
email = input('whats your email? ')

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0_-9]+\.EDU",email) :
  print('valid')
else:
  print('Invalid')
