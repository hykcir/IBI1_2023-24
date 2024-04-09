def chocolate_bar(money):
    total=int(money)
    price=7
    pieces=int(total/price) #make sure the number is an integer
    left=total-int(pieces)*price
    return pieces,left
class chocolatebars:
    def __init__(self, pieces, left):
        self.pieces = pieces # assign the value of "pieces" calculated in advance to the instance variable "pieces"
        self.left = left# same as the upper line

    def print(self):
        print(f"The amount of chocolate bars you can have: {self.pieces}, The change left over is: {self.left}")
user_input=input("Enter the money you have:")
pieces, left=chocolate_bar(user_input)# Create an instance of the chocolatebars class with the calculated pieces and left values
b=chocolatebars(pieces, left)
b.print()