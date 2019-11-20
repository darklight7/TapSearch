from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializer import SnippetSerializer
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
import json

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        print(serializer)
        return Response(serializer.data)

    def put(self, request, format=None):
        #snippet = self.get_object(pk)
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,format=None):
        serializer = SnippetSerializer(data=request.data)
        # print(request.data['title'])
        # print(request.data['code'])
        # print(request.data)
        data = {}
        func = {}
        if serializer.is_valid():
            serializer.save()
            func = self.abc(request.data['code'], str(request.data['title']))
            return Response(func, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        snippet = Snippet.objects.all()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def abc(self, contents, word): #content is paragraph , word is word to be searched
        iindex = {}            # it will become a dictionary inside a dictionary
        contents=contents.split("\n")
     #   print("_______________")
     #   print(len(contents))
    #    for i in contents:
      #      print(i,"\n")
     #   print("_______________")
        for i in range(len(contents)):
            for j in contents[i].strip().replace("."," ").replace(","," ").lower().split(" "):
                if (len(j) > 0):
                    if j not in iindex:
                        iindex[j] = {i: 1}
                        # print(iindex[j][i])
                    else:
                        if (i not in iindex[j]):
                            iindex[j][i] = 1
                        else:
                            iindex[j][i] += 1
        print("\n")

        #print(iindex)
       # print(type(word))
        ii =iindex[word]
        sorted_x = sorted(ii.items(), key=lambda kv: kv[1])
       # print(sorted_x)
        lis=[]
        for i in range(len(sorted_x) - 1, -1, -1):
            lis.append([sorted_x[i][0],contents[sorted_x[i][0]]])
        print (lis)
        return lis


'''
@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
       # print(request.data['title'])
       # print(request.data['code'])
       # print(request.data)
        data = {}
        func = {}
        if serializer.is_valid():
            serializer.save()
            func = abc(request.data['code'], str(request.data['title']))
            return Response(func, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
