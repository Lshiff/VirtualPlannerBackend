from django.shortcuts import render
from rest_framework import generics, status
from .serializers import GoalSerializer, WorkSerializer, PostGoalSerializer, PostWorkSerializer
from .models import Goal, Work
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

#How the computer knows what to show on each endpoin

#All goals
class GoalView(generics.ListAPIView):
    queryset = Goal.objects.all()
    def get(self, request, format=None):
        
        serializer_class = GoalSerializer
        queryset = self.get_queryset()
        serializer = GoalSerializer(queryset, many=True)
        cereal = {"data": serializer.data} #cereal is dictionary with {"data": [data]}
        return Response(cereal)


#Weekly goals  
class WeekGoalView(generics.ListAPIView):
    queryset = Goal.objects.filter(goal_type="weekly")
    def get(self, request, format=None):
        serializer_class = GoalSerializer
        queryset = self.get_queryset()
        serializer = GoalSerializer(queryset, many=True)
        cereal = {"data": serializer.data}
        return Response(cereal)
    

#Monthly goals
class MonthGoalView(generics.ListAPIView):
    queryset = Goal.objects.filter(goal_type="monthly")
    def get(self, request, format=None):
        serializer_class = GoalSerializer
        queryset = self.get_queryset()
        serializer = GoalSerializer(queryset, many=True)
        cereal = {"data": serializer.data}
        return Response(cereal)


#All works
class WorkView(generics.ListAPIView):
    queryset = Work.objects.all()
    def get(self, request, format=None):
        serializer_class = WorkSerializer
        queryset = self.get_queryset()
        serializer = WorkSerializer(queryset, many=True)
        cereal = {"data": serializer.data}
        return Response(cereal)

#Daily works
class DayWorkView(generics.ListAPIView):
    queryset = Work.objects.filter(work_type="daily")
    def get(self, request, format=None):
        serializer_class = WorkSerializer
        queryset = self.get_queryset()
        serializer = WorkSerializer(queryset, many=True)
        cereal = {"data": serializer.data}
        return Response(cereal)
      
#Specific daily works
class SpecficDayWorkView(generics.ListAPIView):
    def get_queryset(self, dotw):
        return Work.objects.filter(work_type="daily", due_date__week_day=dotw+1)
    def get(self, request, dotw, format=None):
        serializer_class = WorkSerializer
        queryset = self.get_queryset(dotw)
        serializer = WorkSerializer(queryset, many=True)
        cereal = {"data": serializer.data}
        return Response(cereal)

#After_school works
class After_SchoolWorkView(generics.ListAPIView):
    queryset = Work.objects.filter(work_type="after_school")
    def get(self, request, format=None):
        serializer_class = WorkSerializer
        queryset = self.get_queryset()
        serializer = WorkSerializer(queryset, many=True)
        cereal = {"data": serializer.data}
        return Response(cereal)

#Specific after_school works
class SpecficAfter_SchooWorkView(generics.ListAPIView):
    def get_queryset(self, dotw):
        return Work.objects.filter(work_type="after_school", due_date__week_day=dotw+1)
    def get(self, request, dotw, format=None):
        serializer_class = WorkSerializer
        queryset = self.get_queryset(dotw)
        serializer = WorkSerializer(queryset, many=True)
        cereal = {"data": serializer.data}
        return Response(cereal)

#Post Goal
class PostGoalView(APIView):
    serializer_class = PostGoalSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             text = serializer.data.get('text')
             due_date = serializer.data.get('due_date')
             goal_type = serializer.data.get('goal_type')

             goal = Goal(text=text, due_date=due_date, goal_type=goal_type)
             goal.save()
             
             return Response(GoalSerializer(goal).data)

#Post Work
class PostWorkView(APIView):
    serializer_class = PostWorkSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
             text = serializer.data.get('text')
             due_date = serializer.data.get('due_date')
             work_type = serializer.data.get('work_type')

             work = Work(text=text, due_date=due_date, work_type=work_type)
             work.save()
             
             return Response(WorkSerializer(work).data)
