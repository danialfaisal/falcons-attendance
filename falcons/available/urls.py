from django.urls import path
from . import views

app_name = 'available'
urlpatterns = [
    path('', views.index, name='index'),
    path('player/<slug:player_id>/tournaments/', views.player_home, name='player_home'),
    path('player/<int:ass_c_id>/attendance/', views.t_attendance, name='t_attendance'),
    path('player/<int:ass_c_id>/Edit_att/', views.edit_att, name='edit_att'),
    path('player/<int:ass_c_id>/availability/confirm/', views.confirm, name='confirm'),
    path('create', views.create, name='create'),

    # TOURNAMENT
    path('tournament_list/', views.tournament_list, name='tournament_list'),
    path('tournament/create/', views.tournament_new, name='tournament_new'),
    path('tournament/<pk>/edit/', views.tournament_edit, name='tournament_edit'),
    path('tournament/<pk>/delete/', views.tournament_delete, name='tournament_delete'),

    # MATCH
    path('match_list/', views.match_list, name='match_list'),
    path('match/create/', views.match_new, name='match_new'),
    path('match/<pk>/edit/', views.match_edit, name='match_edit'),
    path('match/<pk>/delete/', views.match_delete, name='match_delete'),

    # ASSIGNMENT
    path('assign_list/', views.assign_list, name='assign_list'),
    path('assign/create/', views.assign_new, name='assign_new'),
    path('assign/<int:pk>/edit/', views.assign_edit, name='assign_edit'),
    path('assign/<int:pk>/delete/', views.assign_delete, name='assign_delete'),


    path('tournaments/', views.captain_tournament, name='captain_tournament'),
    path('tournament/<int:assign_id>/matches/', views.captain_match, name='captain_match'),
    path('matches/<int:assign_id>/players/', views.available_player, name='available_player'),
]