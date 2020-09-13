from django.contrib import admin
from score_app.models import Matches, Players, Rankings, Wins, Leaders
# Register your models here.


admin.site.register(Matches)
admin.site.register(Players)
admin.site.register(Rankings)
admin.site.register(Wins)
admin.site.register(Leaders)