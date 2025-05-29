movies = [
    ("Fight Club", "David Finchar", 1999, "$63 million" )
]

title = input("Ttile: ")
director = input("Director: ")
release = input("Release year: ")
budget = input("Movie budget: ")

new_movies = title, director, release, budget

print(f"{new_movies[0]} ({new_movies[2]})")

movies.append(new_movies)

print(movies[0])
print(movies[1])

movies.pop(0)