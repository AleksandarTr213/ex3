class Dog:
    def _init_(self,name):
        self.name=name
        self.tricks= []

    def add_trick(self,trick):
        self.tricks.append(trick)
        
    d=Dog("Fido")
    e=Dog("Buddy")
    d.add_trick("roll over")
    e.add_trick("play dead")

    d.tricks
    e.tricks
    