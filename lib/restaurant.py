# should be initialized with a name as a string 
class Restaurant:

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
    def customers(self):
        unique_customers = set()
        for review in self.reviews:
            unique_customers.add(review.customer)
        return list(unique_customers)
    
    # return average star rating for a restaurant based on its reviews
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        average_rating = total_ratings / len(self.reviews)
        return average_rating
    