s1 = "Test"
s2 = 'String'

s3 = "This is Vineet's notebook"
s4 = 'Vineet said, "Thanks"'

print(s1, s2, s3, s4, sep="\n")


s5 = "This is " \
"not a " \
"multiline " \
"string"

print(s5)

s6 = "This is \
not a \
multiline \
string"

print(s6)


s7 = """This is 
infact  a 
multiline 
string"""

print(s7)

s8 = '''This is 
infact  a 
multiline 
string'''

print(s8)


s9 = "First""Second"
print(s9)

path = r"c:\User\ramakant\newfile.txt"
print(path)


topic = "Python"
duration = 5
s10 = f"We are in a {topic} training for {duration} days"
print(s10)

s11 = "We are in a %s training for %d days"
print(s11%(topic, duration))

s12 = "We are in a {} training for {} days"
print(s12.format(topic, duration))



print("=" * 45)
s13 = s12.format(topic, duration)
print(s13)
print(s13[3:6])
print(s13[3:])
print(s13[:6])
print(s13[:])
print(s13[-1])
print(s13[-6:-1])
print(s13[-6:6])
print(s13[-6:], s13[:6], sep='')
# print(s13[Start : End : Step])
print(s13[5 : -6: 2])

s14 = "0123456789"
print(s14[::2])
print(s14[1::2])
print(s14[::-1])

