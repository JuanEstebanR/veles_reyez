from .views.user_views import UserRegistrationView, UserLoginView
from .views.queries_view import (QueriesAPIView,
                                 MyQueriesAPIView,
                                 CommentCreateAPIView)
from .views.bigquery_view import (Top25TermsAPIView, InternationalTopTermsAPIView,
                                  InternationalTopOneTermsAPIView)
from django.urls import path

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('my_queries/<str:username>/', MyQueriesAPIView.as_view(), name='my_queries'),
    path('query_create/<str:username>/', MyQueriesAPIView.as_view(), name='query_create'),
    path('community_queries/', QueriesAPIView.as_view(), name='community_queries'),
    path('query_comment/<int:pk>/', CommentCreateAPIView.as_view(), name='query_comment'),
    path('top_25_terms/', Top25TermsAPIView.as_view(), name='top_25_terms'),
    path('international_top_terms/', InternationalTopTermsAPIView.as_view(),
         name='International_top_terms'),
    path('international_top_one_terms/', InternationalTopOneTermsAPIView.as_view(),
         name='International_top_one_terms'),
]

