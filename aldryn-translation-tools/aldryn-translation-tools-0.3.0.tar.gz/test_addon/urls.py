from django.conf.urls import url

from .views import SimpleDetailView, SimpleListView, SimpleRootView, UntranslatedDetailView


app_name = 'simple'

urlpatterns = [
    url(r'^empty-view', SimpleRootView.as_view(), name='simple-root'),
    url(r'^simple/$', SimpleListView.as_view(), name='simple-list'),

    # NOTE: We are allowing access by slug and pk here.
    url(r'^simple/(?P<pk>\d+)/$', SimpleDetailView.as_view(),
        name='simple-detail'),
    url(r'^simple/(?P<slug>\w[-\w]*)/$', SimpleDetailView.as_view(),
        name='simple-detail'),

    url(r'^untranslated/(?P<pk>\d+)/$', UntranslatedDetailView.as_view(),
        name='untranslated-detail'),
    url(r'^untranslated/(?P<slug>\w[-\w]*)/$', UntranslatedDetailView.as_view(),
        name='untranslated-detail'),
]
