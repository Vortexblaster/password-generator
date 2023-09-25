from passwordvalidate import *


pass_count = 0
fail_count = 0
character_position_total = []
password_total = []

for i in range(100000):
    password = generate(10)

    if validate(password) == "Secure":
        pass_count += 1
    else: fail_count += 1

print("     Passed: %d      Failed: %d" %(pass_count, fail_count))
# Add your own tests and calls to validate() and generate() here
