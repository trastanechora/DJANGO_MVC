from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone
from django.db import models

class Hewan(models.Model):
    nama = models.CharField(max_length=25)
    species = models.CharField(max_length=25)
    berat = models.IntegerField()
    umur = models.CharField(max_length=25)
    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length=25)
    isi_kandang = models.CharField(max_length=25)
    luas_kandang = models.CharField(max_length=25)
    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length=25)
    nomor_telepon = models.CharField(max_length=25)
    jadwal_jaga = models.TextField(max_length=255)
    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length=25)
    nomor_telepon = models.CharField(max_length=25)
    hari_berkunjung = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama



