import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
lower_chars = 0
upper_chars = 0
special_chars = 0
min_length = False
max_length = False

for char in password:
    if char.islower():
        lower_chars += 1
    elif char.isupper():
        upper_chars += 1
    elif char in "$#@":
        special_chars += 1

if len(password) >= 6:
    min_length = True
if len(password) <= 16:
    max_length = True

if lower_chars and upper_chars and special_chars and min_length and max_length:
    is_valid = True

print(is_valid)
