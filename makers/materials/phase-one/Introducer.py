class Introducer:
    def __init__(self, name):
        self.name = name

    def announce(self):
        return f"I am {self.name}!"
    
    def introduce(self, name):
        return f"Hello {name}, " + self.announce()
        

introducer = Introducer("Kay")

print(introducer.announce())
# Should print: "I am Kay!"

print(introducer.introduce("Fred"))
# Should print: "Hello Fred, I am Kay!"