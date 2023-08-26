# initialized with a customer, restaurant and a rating(a num)
# return rating for a restaurant
# returns all reviews

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def give_rating(self):
        return self.rating
    
    # returning the customer instance for a specific review
    def get_customer(self):
        return self._customer
    # writing the review using __str__ method
    def __str__(self):
        return f"Review for {self._restaurant} by {self._customer}, Rating: {self.rating}"
    
    #  review for restaurant using getter method
    def get_restaurant(self):
        return self._restaurant

    @classmethod
    def all_ratings(cls):
        return cls.all_reviews



