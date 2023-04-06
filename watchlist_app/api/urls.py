
from django.urls import path
from watchlist_app.api import views
from watchlist_app.api import stream_platform_views

urlpatterns = [
    path('list', views.WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', views.WatchListDetailAV.as_view(), name='watch_list_details'),
    
    path('stream-platforms', stream_platform_views.StreamPlatformAV.as_view(), name='stream_platforms'),
    path('stream-platforms/<int:pk>', stream_platform_views.StreamPlatformDetailAV.as_view(), name='stream_platform_details')
]