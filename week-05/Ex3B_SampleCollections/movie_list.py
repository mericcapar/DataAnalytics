favorite_movies = ["Interstellar", "Babam ve Oglum", "Saving Private Ryan",
                   "G.O.R.A.", "Recep Ivedik"]

print(f"The list favorite_movies includes my top {len(favorite_movies)} "
      f"favorite movies")
print(favorite_movies)

# a) sorted() returns a new sorted list AND IT DOES NOT CHANGE THE ORIGINAL LIST
print(sorted(favorite_movies))

# b) .sort() sorts the list itself
favorite_movies.sort()
print(favorite_movies)
# .sort() changes the original list, so it stays sorted from now on.

# Add one more movie
favorite_movies.append("Recep Ivedik 2")
print(f"The list favorite_movies includes my top {len(favorite_movies)} "
      f"favorite movies")
print(favorite_movies)