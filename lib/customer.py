# initialize the customers by thier given name and family name/ first and last names
# combine both the first name and last name to get their full names
# Return a list of all customer instances
from review import Review
class Customer:
    all_customers = []
 
    def __init__(self, name, family_name):
        self.given_name = name
        self.last_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    # def given_name(self):
    #     return self.first_name

    def  family_name(self): 
         return self.last_name
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def all_reviews(self, restaurant, rating):
        review = (restaurant, rating)
        self.reviews.append(review)

    def reviewed_restaurants(self):
        #  using set compression to get unique restaurants
        return(list({review.get_restaurant() for review in Review.all_reviews if review.customer == self}))
        return list({restaurant for restaurant, _ in self.reviews})

    # return the total num of reviews a customer has authorized
    def num_reviews(self):
        return len(self.reviews)
       
    @classmethod
    def all(cls):
        return cls.all_customers
    
    #  given a string of a **full name**, returns the **first customer** whose full name matches
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
            else:
                return None
    
    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name() == name:
                matching_customers.append(customer)
            return matching_customers


        


    


