# spacetagram

Search and save your favorite NASA photos

A simple search web app, utilizing NASA's image API (https://api.nasa.gov)

Uses Django to store favorited status in a persistent storage. See it live on https://spacetagram.xyz. When the user
searches for images, the red heart underneath will indicate that they or someone else using the app had favorited the
photo.

Uses poetry, but also contains a requiremnts.txt, with an additional app need, whitenoise
(http://whitenoise.evans.io/en/stable/) for serving static files.
