from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Captain, Player, Match, Availability, Assign, Tournament
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import redirect


@login_required
def index(request):
    if request.user.is_player:
        return render(request, 'available/p_homepage.html')
    if request.user.is_captain:
        return render(request, 'available/captain_home.html')
    return render(request, 'available/logout.html')


@login_required
def player_home(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'available/player_home.html', {'player': player})



@login_required()
def t_attendance(request, ass_c_id):
    assc = get_object_or_404(Assign, id=ass_c_id)
    ass = assc.tournament
    context = {
        'ass': ass,
        'assc': assc,
    }
    return render(request, 'available/t_attendance.html', context)


@login_required()
def edit_att(request, ass_c_id):
    assc = get_object_or_404(Assign, id=ass_c_id)
    att_list = Availability.objects.filter(assign=assc)
    context = {
        'assc': assc,
        'att_list': att_list,
    }
    return render(request, 'available/t_edit_att.html', context)


@login_required()
def confirm(request, ass_c_id):
    assc = get_object_or_404(Assign, id=ass_c_id)
    cl = assc.tournament
    for i, s in enumerate(cl.match_set.all()):
        status = request.POST[s.id]
        if status == 'present':
            status = 'True'
        else:
            status = 'False'
        if assc.status == 1:
            try:
                a = Availability.objects.get(match=s, assign=assc)
                a.availability = status
                a.save()
            except Availability.DoesNotExist:
                a = Availability(match=s, availability=status, assign=assc)
                a.save()
        else:
            a = Availability(match=s, availability=status, assign=assc)
            a.save()
            assc.status = 1
            assc.save()

    return HttpResponseRedirect(reverse('available:player_home', args=(assc.player_id,)))


@login_required
def create(request):
    if request.user.is_captain:
        return render(request, 'available/create.html')




# EMPLOYEE VIEWS

# TOURNAMENT
def tournament_list(request):
    tournaments = Tournament.objects.filter()
    return render(request, 'available/tournament_list.html',
                 {'tournaments': tournaments})

def tournament_new(request):
   if request.method == "POST":
       form = TournamentForm(request.POST)
       if form.is_valid():
           tournament = form.save(commit=False)
           tournament.created_date = timezone.now()
           tournament.save()
           tournaments = Tournament.objects.filter()
           return render(request, 'available/tournament_list.html',
                         {'tournaments': tournaments})
   else:
       form = TournamentForm()
       # print("Else")
   return render(request, 'available/tournament_new.html', {'form': form})

def tournament_edit(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == "POST":
        # update
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.updated_date = timezone.now()
            tournament.save()
            tournaments = Tournament.objects.filter()
            return render(request, 'available/tournament_list.html',
                          {'tournaments': tournaments})
    else:
        # edit
        form = TournamentForm(instance=tournament)
    return render(request, 'available/tournament_edit.html', {'form': form})

def tournament_delete(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    tournament.delete()
    return redirect('available:tournament_list')





# MATCH
def match_list(request):
    matchs = Match.objects.filter()
    return render(request, 'available/match_list.html',
                 {'matchs': matchs})

def match_new(request):
   if request.method == "POST":
       form = MatchForm(request.POST)
       if form.is_valid():
           match = form.save(commit=False)
           match.created_date = timezone.now()
           match.save()
           matchs = Match.objects.filter()
           return render(request, 'available/match_list.html',
                         {'matchs': matchs})
   else:
       form = MatchForm()
       # print("Else")
   return render(request, 'available/match_new.html', {'form': form})

def match_edit(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == "POST":
        # update
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            match = form.save(commit=False)
            match.updated_date = timezone.now()
            match.save()
            matchs = Match.objects.filter()
            return render(request, 'available/match_list.html',
                          {'matchs': matchs})
    else:
        # edit
        form = MatchForm(instance=match)
    return render(request, 'available/match_edit.html', {'form': form})

def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    match.delete()
    return redirect('available:match_list')





# ASSIGN
def assign_list(request):
    assigns = Assign.objects.filter()
    return render(request, 'available/assign_list.html',
                 {'assigns': assigns})

def assign_new(request):
   if request.method == "POST":
       form = AssignForm(request.POST)
       if form.is_valid():
           assign = form.save(commit=False)
           assign.created_date = timezone.now()
           assign.save()
           assigns = Assign.objects.filter()
           return render(request, 'available/assign_list.html',
                         {'assigns': assigns})
   else:
       form = AssignForm()
       # print("Else")
   return render(request, 'available/assign_new.html', {'form': form})

def assign_edit(request, pk):
    assign = get_object_or_404(Assign, pk=pk)
    if request.method == "POST":
        # update
        form = AssignForm(request.POST, instance=assign)
        if form.is_valid():
            assign = form.save(commit=False)
            assign.updated_date = timezone.now()
            assign.save()
            assigns = Assign.objects.filter()
            return render(request, 'available/assign_list.html',
                          {'assigns': assigns})
    else:
        # edit
        form = AssignForm(instance=assign)
    return render(request, 'available/assign_edit.html', {'form': form})

def assign_delete(request, pk):
    assign = get_object_or_404(Assign, pk=pk)
    assign.delete()
    return redirect('available:assign_list')


def captain_tournament(request):
    tournaments = Tournament.objects.all()
    return render(request, 'available/captain_tournament.html',
                 {'tournaments': tournaments})


@login_required()
def captain_match(request, assign_id):
    a = get_object_or_404(Tournament, id=assign_id)
    return render(request, 'available/captain_match.html', {'a': a})


@login_required()
def available_player(request, some_id):
    a = get_object_or_404(Match, id=some_id)
    b = a.availability_set.filter(availability=True)
    context = {
        'a': a,
        'b': b,
    }

    return render(request, 'available/available_player.html', context)