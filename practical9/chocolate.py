def chocolate_bar(money):
    total=int(money)
    price=7
    pieces=int(total/price)
    left=total-int(pieces)*price
    return pieces,left
class chocolatebars:
    def __init__(self, total, left):
        self.total = total
        self.left = left

    def print(self):
        print(f"The amount of chocolate bars you can have: {self.total}, The change left over is: {self.left}")
user_input=input("Enter the money you have:")
pieces, left=chocolate_bar(user_input)
b=chocolatebars(pieces, left)
b.print()