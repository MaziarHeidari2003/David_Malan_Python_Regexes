import re

url = input('URL: ').strip()
#username = url.removeprefix('https//twtter.com')
"""
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
print(f'Username: {username}')
"""

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z_0-9])$",url,re.IGNORECASE) :
  print(f"Username:",matches.group(1))
