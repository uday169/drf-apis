
from django.urls import path
from watchlist_app.api import views
from watchlist_app.api import stream_platform_views

urlpatterns = [
    path('list', views.WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', views.WatchListDetailAV.as_view(), name='watch_list_details'),

    path('stream-platforms', stream_platform_views.StreamPlatformAV.as_view(),
         name='stream_platforms'),
    path('stream-platforms/<int:pk>',
         stream_platform_views.StreamPlatformDetailAV.as_view(), name='stream_platform_details'),

    # path('reviews/', views.ReviewList.as_view(), name='review-list'),
    # path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review-create/',
         views.ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/reviews/',
         views.ReviewList.as_view(), name='review-list'),
    path('stream/reviews/<int:pk>',
         views.ReviewDetail.as_view(), name='review-detail')
]
