#1.define a class name as NewTicket
#2.has 3 cv theater_name, ticket_price, gst_rate
#3.define an initializer and create 3iv ticket_id, customer_name, seat_no
#4. define a class method name as increment_gst which should accept hike as a parameter and increment the  classvariable gst_rate
#5.define an instance methodname as display_ticket
#define static method as validate_age which takes any age as a parameter and returns a boolean value if greater than 18 = allowed


class NewTicket:
    theater_name="pvr"
    ticket_price=800
    gst_rate=12

    def __init__(self,ticket_id,customer_name,seat_no):
        self.ticket_id=ticket_id
        self.customer_name=customer_name
        self.seat_no=seat_no

    @classmethod    
    def increment_gst(cls,hike):
        cls.gst_rate += hike

    def display_ticket(self):
        print("Ticket ID:", self.ticket_id)
        print("Customer Name:", self.customer_name)
        print("Seat No:", self.seat_no)
        print("Theater Name:", NewTicket.theater_name)
        print("Ticket Price:", NewTicket.ticket_price)
        print("GST Rate:", NewTicket.gst_rate)

    @staticmethod
    def valid_age(age):
        return age > 18     

t1 = NewTicket(101, "Manasvi", "A12")

t1.display_ticket()

NewTicket.increment_gst(3)
print("Updated GST:", NewTicket.gst_rate)

print(NewTicket.valid_age(20))  
print(NewTicket.valid_age(16)) 
        
