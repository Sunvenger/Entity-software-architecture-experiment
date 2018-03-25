from Core.Classes.Entity.Entity import *
en = []
for i in range(20):
    en.append(Entity())

print(Entity.count)
while len(en) > 0:
    print(en.pop())
    print(Entity.count)