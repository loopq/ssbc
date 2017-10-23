from django.conf.urls import include, url

urlpatterns = [
    url(r'^json_log$', 'top.views.json_log', name='top_log'),
    url(r'^$', 'top.views.index', name='top_index'),
    url(r'^json_index$', 'top.views.jsonindex', name='top_json_index'),
    url(r'^json_hash_index$', 'top.views.json_hash_index', name='json_hash_index'),
    url(r'^json_keyword_index$', 'top.views.json_keyword_index', name='json_keyword_index'),
]
