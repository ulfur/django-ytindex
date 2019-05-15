=====
ytindex
=====

ytindex is a Django app for managing a searchable index of Youtube videos and
their captions. The app relies on Elasticsearch for the indexing and searching.
The app has no admin, no models and only provides one restful endpoint for
making queries.

Quick start
-----------

1. Add "ytindex" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ytindex',
    ]

2. Include the ytindex URLconf in your project urls.py like this::

    path('yti/', include('ytindex.urls')),

3. Define the channel id of the Youtube channel you want to index and the
   Elasticsearch config you want to use.

   YTCI_SETTINGS = {
       'default':'jrei',
       'jrei': {
           'channel_id': 'UCzQUP1qoWDoEbmsQxvdjxgQ',
           'elastic': {
               'index': 'jre-index',
               'dtype': 'jrei-episode',
               'es_host': 'localhost:9200'
           }
       }
   }

4. Run
    ./manage index_latest [index name eg. jrei]
   to index the latest videos on the channel

5. Visit http://127.0.0.1:8000/yti/search/ to search the index.
