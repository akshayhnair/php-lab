n = int(input("Enter Total number of elements in list : "))
lists = []
for i in range(n):
    v = int(input("Enter a number :"))
    lists.append(v)

t = [each for each in lists if each > 0]
print(t)
for i in lists:
     if i>0:
        print(i)