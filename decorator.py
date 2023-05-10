def dec(fun):
    def wrapper():
        fun()
        print("alexa")
        fun()
    return wrapper
@dec
def Hi():
        print("Hi")
Hi()