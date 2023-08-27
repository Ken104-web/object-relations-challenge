# should be initialized with a name as a string 
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

    def get_reviews(self, review):
        return self.reviews
    # create an instance in for adding a review to the list of existing reviews for a unique customer
    def add_review(self, review):
        self.reviews.append(review)