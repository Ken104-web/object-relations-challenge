# initialize the customers by thier given name and family name/ first and last names
# combine both the first name and last name to get their full names
# Return a list of all customer instances
from lib.restaurant import Restaurant
class Customer:
    all_customers = []

    def __init__(self, name, family_name):
        self.first_name = name
        self.last_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.first_name

    def  family_name(self): 
         return self.last_name
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def all_reviews(self, restaurant, rating):
        review = (restaurant, rating)
        self.reviews.append(review)

    def reviewed_restaurants(self):
        #  using set compression to get unique restaurants
        return list({restaurant for restaurant, _ in self.reviews})


    @classmethod
    def all(cls):
        return cls.all_customers

    


