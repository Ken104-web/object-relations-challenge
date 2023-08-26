# initialized with a customer, restaurant and a rating(a num)
# return rating for a restaurant
# returns all reviews

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def give_rating(self):
        return self.rating
    
    @classmethod
    def all_ratings(cls):
        return cls.all_reviews


