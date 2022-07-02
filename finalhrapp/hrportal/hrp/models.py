
from http import client
from pyexpat import model
from re import T
from shutil import _ntuple_diskusage
from telnetlib import Telnet
from tkinter import CASCADE
from tkinter.tix import Tree
from tracemalloc import start
from unicodedata import name
from django.db import models

# Create your models here.
class basicinfo(models.Model):
    cid=models.AutoField(primary_key=True,null=False,unique=True)
    name=models.CharField(max_length=200,null=True)
    contact=models.PositiveBigIntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    qualifications=models.CharField(max_length=200,null=True,blank=True)
    ctc=models.CharField(max_length=50,null=True,blank=True)
    total_experience=models.CharField(max_length=100,blank=True,null=True)
    exp_level=models.CharField(max_length=50,blank=True,null=True)
    applied_for=models.CharField(max_length=100,blank=True,null=True)
    exp_ctc=models.CharField(max_length=100,blank=True,null=True)
    resume_received_date=models.DateField(blank=True,null=True)
    notice_period=models.CharField(max_length=100,blank=True,null=True)
    resume_received_by=models.CharField(max_length=200,blank=True,null=True)
    current_location=models.CharField(max_length=200,blank=True,null=True)
    present_address=models.TextField(blank=True,null=True)
    permanent_address=models.TextField(blank=True,null=True)
    interviewed_date=models.DateField(blank=True,null=True)
    interviewed_by=models.CharField(max_length=200,blank=True,null=True)
    interview_status=models.CharField(max_length=100,blank=True,null=True)
    date_of_joining=models.DateField(blank=True,null=True)
    client_name=models.CharField(max_length=200,blank=True,null=True)
    designated_as=models.CharField(max_length=200,blank=True,null=True)
    ready_to_relocate=models.CharField(max_length=200,blank=True,null=True)
    call_or_interview_remarks=models.CharField(max_length=100,blank=True,null=True)
    file=models.FileField(upload_to='pictures',null=True,blank=True)

    def __str__(self):
        return str(self.name)

""" @property
    def table(self):
        return self.choice_set.all() """

class consultant(models.Model):
    
    company_name=models.CharField(max_length=50,null=True,blank=True)
    HR_name=models.CharField(max_length=100,null=True,blank=True) 
    HR_number=models.PositiveBigIntegerField(blank=True,null=True)
    basic_consultant=models.OneToOneField(basicinfo ,related_name='basic_consultant', on_delete=models.CASCADE ,null=True,blank=True)
    
    
    def __str__(self):
        return str(self.company_name)

class skills(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    basic_skills=models.ForeignKey(basicinfo,related_name='basic_skills',blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) 

class education(models.Model):
    course_name=models.CharField(max_length=50,blank=True,null=True)
    university_name=models.CharField(max_length=300,blank=True,null=True)
    percentage=models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    year_of_passing=models.CharField(max_length=300,blank=True,null=True)
    basic_education=models.ForeignKey(basicinfo,related_name='basic_education',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.course_name)

  




  
