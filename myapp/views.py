import django_filters
from rest_framework import viewsets, filters
from .models import User, Blog
from .serializer import UserSerializer, BlogSerializer
import cv2
import numpy as np
from rest_framework.decorators import action
from django.conf import settings 
import os
from PIL import Image
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    @action(detail=True, methods=['get'])
    def predict(self, request, pk=None):
        blog = Blog.objects.get(pk=pk)
        image = blog.image
        image = Image.open(image)
        image = np.array(image)
        pred = image.mean()
        blog.pred = pred
        print('d'*40)
        blog.save()
        return Response(pred, status=status.HTTP_200_OK)