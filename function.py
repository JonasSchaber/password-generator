#Python-Code hier
print("Hallo Welt!")

import secrets
import string

chars = string.digits + string.ascii_letters + string.punctuation
print(''.join(secrets.choice(chars) for _ in range(40)))
