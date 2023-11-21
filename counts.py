from collections import Counter, namedtuple, defaultdict, OrderedDict,deque

a = "122333444455555"
print(Counter(a))

b = Counter([3,2,2,2,2,2,4,4,4,1,7,7,9]).most_common()
print(b)

#namedtuple

Human = namedtuple('Human',['name','age','height'])
d = Human(name="David",age="22",height=187)
print(d)


dark = deque()
dark.append(3)
dark.appendleft(23)
print(dark)