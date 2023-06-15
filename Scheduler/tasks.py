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

import logging
import sys

logger = logging.getLogger(__name__)

# Configure logger to use a StreamHandler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

