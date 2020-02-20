import re
names = 'Duran y More, Miss. Asuncion'
name = re.search(r'[.]\s\w+',str(names)).group()[2:]
print(name)