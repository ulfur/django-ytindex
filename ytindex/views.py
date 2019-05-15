from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from .indexing import Index

def default(request):
    return HttpResponseRedirect(reverse('search', kwargs={'query':'', 'index':settings.YTCI_SETTINGS['default']}))

def clean_hit( hit ):
    captions = [ dict( (*caption['_source'].items(), ('score', caption['_score'])) ) for caption in hit['inner_hits']['captions']['hits']['hits']]
    return dict( (*hit['_source'].items(), ('score', hit['_score']), ('captions',captions)) )

def search(request, index, query):
    idx = Index(**settings.YTCI_SETTINGS[index]['elastic'])
    r = idx.match_phrase(query)
    results = [ clean_hit(hit) for hit in r['hits']['hits'] ]
    ctx = {'results':results, 'query': query, 'index':index}
    return JsonResponse(ctx)
