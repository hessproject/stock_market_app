from django.conf.urls import url
from stocks import views

urlpatterns = [
    url(r'^$',
        views.index,
        name='index'),

    url(r'^stocks/historical_pricing/$',
        views.historical_pricing,
        name='historical_pricing'),
]