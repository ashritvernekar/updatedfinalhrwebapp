from asyncore import read
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from hrp.models import basicinfo,consultant,skills,education

class consultantserializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = consultant
        fields=[
            'company_name',
            'HR_name',
            'HR_number',
            'basic_consultant'
           
        ]
    
class skillsserializer(serializers.ModelSerializer):
    class Meta:
        model = skills
        fields = [
            'name',
            'basic_skills'
        ]

class educationserializer(serializers.ModelSerializer):
    class Meta:
        model = education
        fields=[
            'course_name',
            'university_name',
            'percentage',
            'year_of_passing',
            'basic_education'
        ]

class basicinfoserializer(serializers.ModelSerializer):
    
    basic_consultant =consultantserializer(read_only=True)
    basic_skills=skillsserializer(many=True,read_only=True)
    basic_education=educationserializer(many=True,read_only=True)
    class Meta:
        model = basicinfo
        fields=[
        'cid',
        'name',
        'contact',
        'basic_skills',
        'email',
        'qualifications',
        'basic_education',
        'ctc',
        'total_experience',
        'exp_level',
        'applied_for',
        'exp_ctc',
        'resume_received_date',
        'notice_period',
        'resume_received_by',
        'current_location',
        'present_address',
        'permanent_address',
        'interviewed_date',
        'interviewed_by',
        'interview_status',
        'date_of_joining',
        'designated_as',
        'client_name',
        'ready_to_relocate',
        'call_or_interview_remarks',
        'basic_consultant',
        'file'
        ]
   
