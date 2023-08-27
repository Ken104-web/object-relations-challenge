# should be initialized with a name as a string 
from review import Review
class Restaurant:
    #  store all restaurant instances
    all_reviews = []
    
    def __init__(self, name = ''):
        self._name = name
        # store reviews for a specific restaurant instance
        self.reviews = []
        Restaurant.all_reviews.append(self)

    def given_name(self):
        return self._name
# Returns a list of all reviews for that restaurant
    def get_reviews(self):
        return self.reviews
    
    # create an instance in for adding a review to the list of existing reviews 
    def add_review(self, review):
        self.reviews.append(review)

    # return a unique list of all customers reviews for a specific restaurant
    def customer(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer)
        return list(unique_customers)
    