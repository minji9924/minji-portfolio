import json

from django.shortcuts import render
from mainpage.models import Grade
from django.db.models import Count
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GradeSerializer

from django.http import JsonResponse


# Create your views here.

def example(request):
    return render(request, "mainpage/generic.html")


def get_grade(request):

    # GRADE DISTRIBUTION DATA

    aplus = list(Grade.objects.filter(subject_grade='A+').values('semester').annotate(Count('semester')))
    aplus_list = [0, 0, 0, 0, 0, 0, 0]
    for data in aplus:
        aplus_list[data['semester'] - 1] = data['semester__count']

    azero = list(Grade.objects.filter(subject_grade='A').values('semester').annotate(Count('semester')))
    azero_list = [0, 0, 0, 0, 0, 0, 0]
    for data in azero:
        azero_list[data['semester'] - 1] = data['semester__count']

    bplus = list(Grade.objects.filter(subject_grade='B+').values('semester').annotate(Count('semester')))
    bplus_list = [0, 0, 0, 0, 0, 0, 0]
    for data in bplus:
        bplus_list[data['semester'] - 1] = data['semester__count']

    bzero = list(Grade.objects.filter(subject_grade='B').values('semester').annotate(Count('semester')))
    bzero_list = [0, 0, 0, 0, 0, 0, 0]
    for data in bzero:
        bzero_list[data['semester'] - 1] = data['semester__count']

    cplus = list(Grade.objects.filter(subject_grade='C+').values('semester').annotate(Count('semester')))
    cplus_list = [0, 0, 0, 0, 0, 0, 0]
    for data in cplus:
        cplus_list[data['semester'] - 1] = data['semester__count']

    pass_ = list(Grade.objects.filter(subject_grade='P').values('semester').annotate(Count('semester')))
    pass_list = [0, 0, 0, 0, 0, 0, 0]
    for data in pass_:
        pass_list[data['semester'] - 1] = data['semester__count']

    # GPA DATA
    overall_data, major_data = [], []
    overall = Grade.objects.exclude(subject_grade='P').values('subject_name', 'credit', 'gpa')
    major = overall.filter(major='True')
    for i in range(1, 8):
        overall_gpa, overall_num = 0, 0
        major_gpa, major_num = 0, 0
        cur_overall, cur_major = overall.filter(semester=i), major.filter(semester=i)

        for overall_sub in cur_overall:
            overall_cal = overall_sub.get('credit') * overall_sub.get('gpa')
            overall_gpa += overall_cal
            overall_num += overall_sub.get('credit')

        for major_sub in cur_major:
            major_cal = major_sub.get('credit') * major_sub.get('gpa')
            major_gpa += major_cal
            major_num += major_sub.get('credit')

        overall_data.append(round(overall_gpa / overall_num, 2))
        major_data.append(round(major_gpa / major_num, 2))

    return render(request, 'mainpage/index.html',
                  {'aplus_list': aplus_list, 'azero_list': azero_list, 'bplus_list': bplus_list,
                   'bzero_list': bzero_list, 'cplus_list': cplus_list, "pass_list": pass_list,
                   'overall_data': overall_data, 'major_data': major_data})
