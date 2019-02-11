from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone
from django.db import models

class Dokter(models.Model):
    nama = models.CharField(max_length=25)
    nomor_telepon = models.CharField(max_length=15)
    bidang = models.CharField(max_length=50)
    jadwal_praktek = models.CharField(max_length=20)
    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length=25)
    nomor_telepon = models.CharField(max_length=15)
    alamat = models.TextField(max_length=255)
    keluhan = models.TextField(max_length=255)
    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length=25)
    total_harga = models.IntegerField()
    kumpulan_obat = models.TextField(max_length=255)

class Obat(models.Model):
    nama = models.CharField(max_length=25)
    kandungan = models.TextField(max_length=255)
    khasiat = models.TextField(max_length=255)
    def __str__(self):
        return self.nama



