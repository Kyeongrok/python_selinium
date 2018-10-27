class people():
    name = "kyeongrok"

    def sayHello(self):
        print("hello")

    def leftHand(self):
        print("i'm left hand")

    def rightHand(self):
        print("i'm right hand")

    def setName(self, name):
        self.name = name

kyeongrok = people()
kyeongrok.setName("iu")

print(kyeongrok.name)

kyeongrok.sayHello()
kyeongrok.leftHand()
kyeongrok.rightHand()