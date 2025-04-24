class Client:
    def __init__(self):
        self.__code = 4321

    def __account(self):
        print("Account number is 1234")

    def getcode(self):
        return self.__code

person = Client()
#print(person.__code) this will not work

#object._classname__nameattr
print(person._Client__code)
person._Client__account()

