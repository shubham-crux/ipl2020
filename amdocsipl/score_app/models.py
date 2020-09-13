from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


class Matches(models.Model):
    matchname = models.CharField(max_length=256, default="")
    matchdate = models.DateField(default=date.today, blank=True)
    matchday = models.CharField(max_length=20,  blank=True)
    matchtime = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id) + ',' + str(self.matchname) + "," + str(self.matchdate)


class Players(models.Model):
    playername = models.CharField(max_length=100, default="")
    pointsinvested = models.IntegerField(default=0)
    datejoined = models.DateField(default=date.today)

    def __str__(self):
        return str(self.playername)


class Rankings(models.Model):
    rank = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return str(self.rank)


class Wins(models.Model):
    matchdetail = models.ManyToManyField(Matches)
    playerdetail = models.ManyToManyField(Players)
    rankdetail = models.ManyToManyField(Rankings)
    pointswon = models.IntegerField()
    windate = models.DateField(default=date.today)

    def __str__(self):
        for player in self.playerdetail.all():
            return str(player) +","+ str(self.windate)


class Leaders(models.Model):
    distinctplayer = models.ForeignKey('Players', on_delete=models.CASCADE)
    totalpoints = models.IntegerField()


    class Meta:
        ordering = ['-totalpoints']


    def __str__(self):
        return str(self.distinctplayer)