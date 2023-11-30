import sys,datetime,time
print(str(0x1F))

write = sys.stdout.write
write('Do the work')
write('patrick said')
print()

# print("%s" %time.time())
date = datetime.datetime.now()
print(date)
print(date.year)
print(date.strftime("%C"))

birth = datetime.datetime(2001,8,6)
print(date.year - birth.year)
print(birth.strftime("%B"))

print(datetime.date.today())
print(date.today().strftime("%Y-%m"))

this_month = date.today().strftime("%b")
print("We are in",this_month)