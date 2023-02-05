class Parking_garage():

    current_ticket = {
         "paid": True,
    }

    def __init__(self, capacity, price):
        self.price = price
        self.capacity = capacity

    def takeTicket(self):

        if self.capacity <= 0:
            print("There are no more open spaces please come back later")
            return

        self.capacity -= 1
        self.current_ticket['paid'] = False

    def payForParking(self):
        
        print(f"Your ticket is {self.price}$")
        paid_amount = int(input("Please pay your ticket: "))
        while paid_amount < 5:
             paid_amount += int(input("You didnt pay enough, please pay more: "))
        change = paid_amount - self.price
        print("Your ticket has been paid and you have 15 minutes to leave")
        if change > 0:
            print(f"Your change is ${change}")
        self.current_ticket['paid'] = True

    def leaveGarage(self):

        if self.current_ticket['paid']:
            print("Thank you have a nice day!")
            self.capacity += 1            
        else:           
            Parking_garage.payForParking(self)
        pass

    def findParking(self):
       
        while True:
            user_choice = input("Would you like to park? ").lower()
            if user_choice == 'yes' or 'y':
                self.takeTicket()
            if self.current_ticket['paid'] == False:
                self.payForParking()
                self.leaveGarage()
            else:
                self.leaveGarage()
        



park1 = Parking_garage(50, 5)

park1.findParking()
