def helloWho(who):
    return "hello " + who

list = []
print(helloWho("kyeongrok"))
print(list)

list.append(helloWho("kyeongrok"))
print(list)

list.append(helloWho("hhhh"))
print(list)

list = []
list.append(30)
list.append(40)