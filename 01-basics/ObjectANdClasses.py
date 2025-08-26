class Marksheet :
    def __init__(self,name,rollno):
         self.username = name
         self.rollno = rollno
         
first = Marksheet("Sourabh",23)
second = Marksheet("Rahul",23)
third = Marksheet("Shroud",23)


print((f"{first.username} if securing position first and his Roll no is {first.rollno}"))