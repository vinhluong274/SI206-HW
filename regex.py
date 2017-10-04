import re

f = open("regex_sum_38137.txt", "r")
text = f.read()

y = re.findall('[0-9]+', text)

intList = []
for i in y:
    intList.append(int(i))

print(sum(intList))
