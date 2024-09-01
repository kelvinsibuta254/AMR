# Post model
## represents a blog post with title, content, author, and created_at fields

# PostSerializer
## Is responsible for serializeing and deserializing the Post Model

# IsAuthorOrReadOnly
## is a custom permission class that allow read only access to anyone, but only allows the author of the post to perform CRUD operations on it

# PostListCreateAPIView
## handles the list and create operations for the Post Model
## it requires token-based authentication (TokenAuthentication) and the IsAuthenticated and IsAuthorOrReadOnly permissions
## when creating a new post the perform_create method is overridden to associate the current user as the author of the post

# PostRetrieveUpdateDestroyAPIView
## handles retrieve, update, and destroy operations for individual Post instances.
## It also requires token-based authentication and the IsAuthenticated and IsAuthorOrReadOnly permissions

# urls.py
## In this file we define the URL patterns for the two views, allowing clients to access the post list and individual post details

# With this setup, only authenticated users can access the API, and the IsAuthorOrReadOnly permission ensures that users can only perform CRUD operations on posts they have authored. This provides a basic level of security and access control for the API