from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import ForeignKey
from django.utils import timezone
from django.db import models

# Create your models here.

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telephone = models.TextField(max_length=25)
    jabatan = models.CharField(max_length=50)
    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telephone = models.CharField(max_length=50)
    nomor_absen = models.IntegerField()
    nilai_ratarata = models.IntegerField()
    def __str__(self):
        return self.nama_lengkap

class Mata_Pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=50)
    jadwal_dimulai = models.CharField(max_length=50)
    jadwal_berakhir = models.CharField(max_length=50)
    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telephone = models.CharField(max_length=50)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=50)
    banyak_soal = models.IntegerField()
    bobot_nilai = models.IntegerField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_challenge

class Live_Code(models.Model):
    nama_live_code = models.CharField(max_length=50)
    banyak_soal = models.IntegerField()
    bobot_nilai = models.IntegerField()
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_live_code
