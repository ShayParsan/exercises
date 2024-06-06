def group_movies_by_year(movies):
    movies_by_year = {}
    for movie in movies:
        if movie.year in movies_by_year:
            movies_by_year[movie.year].append(movie.title)
        else:
            movies_by_year[movie.year] = [movie.title]
    return movies_by_year