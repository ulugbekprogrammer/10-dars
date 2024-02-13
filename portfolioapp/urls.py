from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('resume/', resume),
    path('portfolio/', portfolio),
    path('blog/', blog),
    path('contact/', contact),
]