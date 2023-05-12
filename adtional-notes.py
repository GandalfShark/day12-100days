
condit = False

if condit:
    x = 1
else:
    x = 2
print(x)
# example from: https://www.youtube.com/watch?v=C-gEQdGVXbk
# above refactored as a Ternary Condition
x = 10 if condit else 10_000
# set x = 10 if condit = true else set x = 10,000
# you can use _ instead of commas when writing numbers
print(f'{x:,}\n')
# print the numeric formated var using , as a seperator to make it more readable
# using something else like print(f'{x:%}') gives a percent, but $ throws an error
# the , or % is a format code for the object int

names = ['Leo', 'Mikey', 'Don', 'Raph']
dex = 1
for turtle in names:
    print(dex, turtle)
    dex += 1
print('-----------')

# now using enumerate instead
for index, turtle_name in enumerate(names, start=1):
    print(index, turtle_name)

