def directors_count(db):
    # TO-DO: use 'db' to execute an SQL query against the database.
    # Return directors count in database.

    request = 'SELECT COUNT(*) FROM directors;'
    results = db.execute(request)
    return int(results.fetchone()[0])

def sorted_directors(db):
    # TO-DO: return a list of directors' names sorted alphabetically

    request = 'SELECT name FROM directors ORDER BY name'
    results = db.execute(request)
    sql_list = results.fetchall()
    directors_list = [val for sublist in sql_list for val in sublist]
    return directors_list

def love_movies(db):
    # TO-DO: return a list of love movies' names

    request = 'SELECT title FROM movies WHERE title LIKE "%love%" ORDER BY title'
    results = db.execute(request)
    love_movies_list = [val for sublist in results.fetchall() for val in sublist]
    return love_movies_list

def directors_with_name(db, name):
    # TO-DO: count number of director with this name

    results = db.execute('SELECT COUNT(*) FROM directors WHERE name LIKE ?', (f"%{name}%",))
    return int(results.fetchone()[0])

def long_movies(db, min_length):
    # TO-DO: return a list of movies' names
    # verifying: minutes > min_length, sorted by length (ascending)

    request = '''\
SELECT title FROM movies
WHERE minutes > ?
ORDER BY minutes ASC
    '''
    results = db.execute(request, (min_length,))
    results = [val for sublist in results.fetchall() for val in sublist]
    return results