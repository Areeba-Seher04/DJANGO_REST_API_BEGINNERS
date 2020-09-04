# DJANGO_REST_API_BEGINNERS
CRUD OPERATIONS

## End Points

### Get list of all posts (GET request)

http://127.0.0.1:8000/api/posts/

### Detail of post (GET request)

http://127.0.0.1:8000/api/posts/1/

### Create post (Post request)

http://127.0.0.1:8000/api/posts/create/
#### fields 
title (required) 

content (required) 

author (pk, required)

### Update post (PATCH request)

http://127.0.0.1:8000/api/posts/1/update/ 
#### fields 
title

content

author 


### Delete post (DELETE request)

http://127.0.0.1:8000/api/posts/2/delete/

### Author Detail (GET request)

http://127.0.0.1:8000/api/posts/author/1
