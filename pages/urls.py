from django.urls import path
from pages import views
urlpatterns = [
    path("", views.home, name='home'),
    path("", views.add_animal, name='add_animal'),
    path("", views.animal_details, name='animal_details'),
    path("", views.clear_fence, name='clear_fence'),
    path("", views.feed_animal, name='feed_animal'),
    path("", views.guardian_deatils, name='guardian_details'),
    path("", views.guardians, name='guardians'),
    path("", views.rm_animal, name='rm_animal'),

]