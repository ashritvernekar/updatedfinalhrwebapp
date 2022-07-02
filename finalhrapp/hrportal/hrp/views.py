'''from json import JSONEncoder
import json
import profile
from urllib import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import action

from hrp.models import basicinfo
from hrp.serializers import basicinfoserializer
from rest_framework.views import APIView



# Create your views here.
@csrf_exempt
def basicinfoApi(request,id=0):
    if request.method=='GET':
        Basicinfo =basicinfo.objects.all()
        Basicinfo_serializer=basicinfoserializer(Basicinfo, many=True)
        return JsonResponse(Basicinfo_serializer.data, safe=False)
    elif request.method=='POST':
        Basicinfo_data = JSONParser().parse(request)
        Basicinfo_serializer = basicinfoserializer(data=Basicinfo_data , many=True)
        if Basicinfo_serializer.is_valid():
            Basicinfo_serializer.save()
            return JsonResponse("updated succefully", safe=False)
        return JsonResponse("Failed to update",safe=False)

    elif request.method == 'PUT':
        Basicinfo_data=JSONParser().parse(request)
        Basicinfo = basicinfo.objects.get(candidateid=Basicinfo_data['candidateid'])
        Basicinfo_serializer=basicinfoserializer(Basicinfo, data=Basicinfo_data)
        if Basicinfo_serializer.is_valid():
            Basicinfo_serializer.save()
            return JsonResponse("Updated succesfully!!",safe=False)
        return JsonResponse("Failed to update",safe=False)

    elif request.method == 'DELETE':
        Basicinfo=basicinfo.objects.get(candidateid=id)
        Basicinfo.delete()
        return JsonResponse("Deleted succefully!!",safe=False)'''

'''class profiles(APIView):
    def post(self,request):
        serializer_data = basicinfoserializer(data=request.data, many=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse({'message':'done'})
        return JsonResponse("failed",safe=False)

    def get(self,request):
        data = basicinfo.objects.all()
        serializer=basicinfoserializer(data,many=True)
        return JsonResponse(serializer.data,safe=True)'''

#from requests import delete
from asyncio import constants
from distutils.log import error
from email import parser
import email
from operator import indexOf
from sys import modules


from requests import request
#from yaml import parse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import basicinfoserializer,consultantserializer,skillsserializer,educationserializer
from hrp.models import basicinfo,consultant,skills
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from django.http import QueryDict


class Searchapi(APIView):
    parser_classes =(MultiPartParser, FormParser, JSONParser)

    def get(self, request, *args, **kwargs):
        searchval = request.query_params['search']
        filteredval = basicinfo.objects.filter(skills__contains=searchval)
        
        serializer=basicinfoserializer(filteredval,many=True)
        return Response(serializer.data)


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, *args, **kwargs):
        
        data=request.data
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)  
        consultant_name=query_dict.pop("consultancy_company_name")
        consultant_hr_name=query_dict.pop("consultancy_hr_name")
        consultant_contact=query_dict.pop("consultancy_hr_contact_number")
        tenth=query_dict.pop("tenth")
        twelth=query_dict.pop("twelve")
        diploma=query_dict.pop("diploma")
        graduation=query_dict.pop("graduation")
        pg=query_dict.pop("pg")
        phd=query_dict.pop("phd")
        location=query_dict.pop("current_work_location")
        other_location=query_dict.pop("other_current_work_location")
        

        skill=query_dict.pop("skills")
        sl=skill[0].split(",")
        tenth_details=tenth[0].split(",")
        twelth_details=twelth[0].split(",")
        diploma_details=diploma[0].split(",")
        graduation_details=graduation[0].split(",")
        pg_details=pg[0].split(",")
        phd_details=phd[0].split(",")
        list_data=[]
        list_data.append(tenth_details)
        list_data.append(twelth_details)
        list_data.append(diploma_details)
        list_data.append(graduation_details)
        list_data.append(pg_details)
        list_data.append(phd_details)
        

     



        file_serializer = basicinfoserializer(data=request.data)
        consultant_data={
            "company_name":consultant_name[0],
            "HR_name":consultant_hr_name[0],
            "HR_number":consultant_contact[0],
            }
        
        
        if file_serializer.is_valid():
            file_serializer.save()
            Bid=basicinfo.objects.last()
            consultant_serializer =consultantserializer(data=consultant_data)
            if consultant_serializer.is_valid(): 
                consultant_serializer.save()
                Cid=consultant.objects.last()
                consultant.objects.filter(id=Cid.id).update(basic_consultant=Bid.cid)
        
            
            for i in sl:
                d={}
                d["basic_skills"]=Bid.cid
                d["name"]=i
                skills_serializer=skillsserializer(data=d)
                if skills_serializer.is_valid():
                    skills_serializer.save()
            
            for i in list_data:
                
                d2={
                    "course_name":i[0],
                    "university_name":i[1],
                    "percentage":i[2],
                    "year_of_passing":i[3],
                    "basic_education":Bid.cid
                }
                education_serializer=educationserializer(data=d2)
                if education_serializer.is_valid():
                    education_serializer.save()
       

            if location[0]=="OTHER":
                basicinfo.objects.filter(cid=Bid.cid).update(current_location=other_location[0])
            else:
                basicinfo.objects.filter(cid=Bid.cid).update(current_location=location[0]) 
                
            return Response("updated", status=status.HTTP_201_CREATED)
        else:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request, *args, **kwargs):
        data = basicinfo.objects.all()
        serializer=basicinfoserializer(data,many=True)
        return Response(serializer.data)

    def put(self,request, *args, **kwargs):
        Basicinfo = basicinfo.objects.get(cid=request.data['cid'])
        Basicinfo_serializer=basicinfoserializer(Basicinfo, data=request.data)
        if Basicinfo_serializer.is_valid():
            Basicinfo_serializer.save()
            return Response("Updated succesfully!!")
        return Response("Failed to update")

    def delete(self,request ,id , *args, **kwargs):
        Basicinfo=basicinfo.objects.get(candidateid=id)
        Basicinfo.delete()
        return Response("Deleted succefully!!")

class BasicviewSet(APIView):
    def post(self,request , *args, **kwargs):
        data=request.data
        '''p=data.dict()
        s=p.pop("name")'''
        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)
        
        consultant_name=query_dict.pop("consultancy_company_name")
        consultant_hr_name=query_dict.pop("consultancy_hr_name")
        consultant_contact=query_dict.pop("consultancy_hr_contact_number")
        tenth=query_dict.pop("tenth")
        twelth=query_dict.pop("twelve")
        diploma=query_dict.pop("diploma")
        graduation=query_dict.pop("graduation")
        pg=query_dict.pop("pg")
        phd=query_dict.pop("phd")
        location=query_dict.pop("current_work_location")
        other_location=query_dict.pop("other_current_work_location")
        a=query_dict.pop("name")
        
        return Response(a)
    """consultantx=query_dict.pop("consultant")
        
        sp=consultantx[0].split(",")
        consultant_name=sp[0]
        consultant_hrname=sp[1]
        consultant_contact=int(sp[2]) """
