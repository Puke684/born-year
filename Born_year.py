import time
print('i can "guess" the year you were born yes yes, just answer my questions!!')
time.sleep(1)

year = input('What is the current year??\n>')
time.sleep(1)

age = input('How old are you? or How old are you turning this year?\n>')
time.sleep(1)

year = int(year)
age = int(age)

born = year - age

print(f'you were born in {born}!!')