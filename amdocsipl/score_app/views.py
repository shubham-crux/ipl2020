# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from . import models


# from . import models
# from django.urls import reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    context_object_name = 'index'
    template_name = 'index.html'


@login_required
def user_logout(reqeust):
    logout(reqeust)
    return HttpResponseRedirect(reverse('index'))


class MatchDetailsView(ListView):
    context_object_name = 'matches_detail'
    model = models.Matches
    template_name = 'match_details.html'


class MatchRulesView(ListView):
    context_object_name = 'match_rules'
    model = models.Rankings
    template_name = 'match_rules.html'


class MatchPlayersView(ListView):
    context_object_name = 'match_players'
    model = models.Players
    template_name = 'match_players.html'