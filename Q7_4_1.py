name = 'out_test.txt'
f = 'Hello out_test.txt'
with open(name, 'w') as n:
    n.write(f)

with open(name, 'r') as n:
    for line in n:
        print(line, end="")
