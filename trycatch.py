import sys
import struct
# choice = input("Type sth: ")

# try:
#     ans = eval(choice)+233
# except TypeError:
#     print("Type error")
# except:
#     print("Could not evaluate")
    
print(len(sys.argv))

pattern = ["one","two","three","fifteen"]

for _ in reversed(pattern):
    print(_)

for _ in pattern[::-1]:
    print(_)