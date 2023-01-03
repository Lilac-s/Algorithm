from itertools import permutations

# print("hello world")
x = 10
y = 4
print(x + y)
start = "hello world"
print(start)
print(len(start))
print(start[0:5], start[-1], start.split(" "))
hello = "hello"
world = "world"
print(hello + " " + world)

abc = list(range(10))
abc.append(10)
abc.insert(3, "네번째 자리")
del abc[3]
print(abc)

mydi = {
    "youji" : "hi",
    "hello" : "world"
}
print(mydi.keys())
print(list(mydi.keys()))
print("world" in list(mydi.keys()))

# == : 같다, != : 다르다, > : 크다, < : 작다, >= : 크거나 같다, <= : 작거나 같다

if len(mydi) > 3:
    print("3보다 길대")
elif len(mydi) == 2:
    print("2래")
else:
    print("2보다 짧대")

for key in list(mydi.keys()):
    print(key)

for i in range(len(start)):
    print(i)

for key, item in mydi.items():
    print(key, item)

tmp = 1
while tmp < 6:
    print(tmp)
    tmp += 1

def python_the_best(k):
    print(k, "파이썬 최고..")

python_the_best("편리한")

"""
abs()	dict ()	help ()	min ()	setattr()
all()	dir()	hex()	next()	slice()
any()	divmod()	id()	object()	sorted()
ascii()	enumerate()	input()	oct()	staticmethod()
bin()	eval()	int()	open()	str()
bool()	exec()	isinstance()	ord()	sum()
bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()
callable()	format()	len()	property()	type()
chr()	frozenset()	list()	range()	vars()
classmethod()	getattr()	locals()	repr()	zip()
compile()	globals()	map()	reversed()	import()
complex()	hasattr()	max()	round()	
delattr()	hash()	memoryview()	set()	
"""

items = ["hi", "hello", "mouse"]
# print(list(map(''.join, permutations(items))))

permu = []

for i in range(1, len(items)+1):
    permu.append(list(map(''.join, permutations(items, i))))

print(permu)

text = "himynameishellomouser"

for i in items:
    text = text.replace(i, "0")

print(text)