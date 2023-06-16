# Create your tasks here
# from demoapp.models import Widget
from __future__ import absolute_import, unicode_literals
import datetime
from celery import shared_task
from Tenant.models.interview import Interview
from datetime import date
from Tenant.api.serializers import InterviewSerializer
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import logging
import sys

logger = logging.getLogger(__name__)

# Configure logger to use a StreamHandler
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.setLevel(logging.DEBUG)
# console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(console_formatter)
# logger.addHandler(console_handler)

@shared_task
def check_interview(request):
   response_data=[]
   interviews = Interview.objects.all()
   serializers = InterviewSerializer(interviews, many=True)
   for interview in serializers.data:
      interview_date_str = interview["date"]
      interview_date_time = datetime.strptime(interview_date_str, '%Y-%m-%d').date()
      days_left = (interview_date_time - date.today()).days

      if days_left < 10:
            response_data.append(interview)
   if len(response_data)>0:    
    logger.info(response_data)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'realtime_data',
            {
                'type': 'realtime_data',
                'data': response_data
            }
        ) 
   else:
      return Response({
            "success": True,
            "message": "no interviews within 10 days",
        }, status=status.HTTP_200_OK) 
      




 