from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Activity
from .serializers import ActivitySerializer

class ActivityListView(APIView):
    def get(self, request, day):
        activities = Activity.objects.filter(day=day)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MarkActivityComplete(APIView):
    def post(self, request, activity_id):
        try:
            activity = Activity.objects.get(id=activity_id)
            activity.is_completed = True
            activity.save()
            return Response({'message': 'Activity marked as complete'}, status=status.HTTP_200_OK)
        except Activity.DoesNotExist:
            return Response({'error': 'Activity not found'}, status=status.HTTP_404_NOT_FOUND)

