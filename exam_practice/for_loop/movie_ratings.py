movie_amount = int(input())

max_rating = -10.00
min_rating = 10.00
high_rating_movie = None
low_rating_movie = None
average_rating = 0

for movie in range(movie_amount):
    movie_name = input()
    rating = float(input())

    if rating >= max_rating:
        max_rating = rating
        high_rating_movie = movie_name
    elif rating <= min_rating:
        min_rating = rating
        low_rating_movie = movie_name

    average_rating += rating

print(f"{high_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{low_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating / movie_amount:.1f}")
