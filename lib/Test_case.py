# Importing the necessary classes from your code
from restaurant import Restaurant
from customer import Customer
from review import Review

# Creating instances of Customer
customer1 = Customer("Kenneth", "Mwangi")
customer2 = Customer("Lliy", "Nyamvula")

# Creating an instance of Restaurant
restaurant1 = Restaurant("Delicious Eats")

# Creating an instance of Review
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)

# Testing methods
print("Customer 1's Full Name:", customer1.full_name())
print("Customer 2's Last Name:", customer2.family_name())
print("Restaurant Name:", restaurant1.given_name())
print("Review 1 Rating:", review1.give_rating())
print("Review 2 Customer:", review2.get_customer().full_name())
print("Review 1:", review1)

# Getting all reviews
all_reviews = Review.all_ratings()
print("All Reviews:")
for review in all_reviews:
    print(review)
