class house:
    def __init__(self,color,floor):
        self.color=color
        self.floor=floor

    def bedroom(self):
        print(f"The color of the walls of your bedroom will be {self.color}")

    def kitchen(self):
        print(f"The color of the walls of  your kitchen is{self.color}")
        print(f"The floor of your kitchen is{self.floor}")
obj1=house("off-white","files")
obj1.bedroom()
obj1.kitchen()