from django.shortcuts import render,redirect
from .models import Context, List,Task
from .forms import ContextForm, ListForm, TaskForm
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from .serializer import ContextSerializer,ListSerializer,TaskSerializer
# def create_task(request):
#     if request.method == "POST":
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect( / task)
        
#         except:
#                pass

#     else:
#         form = TaskForm()
        
#     return render(request, "index.html", {'form': form})
    
# def get_task(request):
#     tasks = Task.objects.all()
#     return render(request, "get_task.html", {"tasks":tasks})

# @csrf_exempt
# def list_list(request):
#     if request.method=='GET':
#         list = List.objects.all()
#         serializer = ListSerializer(list, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ListSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.error, status=400)
        
# @csrf_exempt
# def list_detail(request, pk):
#     """
#     Retrieve, update or delete a code list.
#     """
#     try:
#         list = List.objects.get(pk=pk)
#     except List.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ListSerializer(list)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ListSerializer(list, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         list.delete()
#         return HttpResponse(status=204)

# @csrf_exempt
# def create_task(request):
#     data = JSONParser().parse(request)
#     # print(data)
#     # print(data['context']['id'])
#     # context = get_object_or_404(Context, id=data['context']['id'])
#     context_id = data['context']['id']
#     print(id)
#     context = Context.objects.get(pk=context_id)
#     list_id = data['list']['id']
#     list = List.objects.get(pk=list_id)
#     print(context)
#     print
#     # print( get_object_or_404(Context, id=request.POST.get['context']))
#     # context = get_object_or_404(Context, id=request.POST.get('id'),context_name=request.POST.get('context_name'))
#     # print(context)
#     return HttpResponse(request)
    

# @csrf_exempt
# def list_task(request):
#     if request.method=='GET':
#         list = Task.objects.all()
#         serializer = TaskSerializer(list, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     # elif request.method == 'POST':
#     #     data = JSONParser().parse(request)
#     #     print(data)
#     #     serializer = TaskSerializer(data=data)
#     #     context_data = validated_data.pop('context')
#     #     list_data = validated_data.pop('list')

#     #     print(serializer.is_valid())
#     #     if serializer.is_valid():
#     #         Task.objects.create()
#     #         # pass
#     #         # serializer.save()
#     #         # list_list = request.pop('list')
#     #         # list_context = request.pop('context')

#     #         return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.error, status=400)

# @csrf_exempt
# def task_detail(request, pk):
#     """
#     Retrieve, update or delete a code list.
#     """
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(task, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         task.delete()
#         return HttpResponse(status=204)


# @csrf_exempt
# def context_list(request):
#     if request.method=='GET':
#         context = Context.objects.all()
#         serializer = ContextSerializer(context, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         print(data)
#         serializer = ContextSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.error, status=400)

# @csrf_exempt
# def context_detail(request, pk):
#     """
#     Retrieve, update or delete a code list.
#     """
#     try:
#         context = Context.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ContextSerializer(context)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ContextSerializer(context, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         context.delete()
#         return HttpResponse(status=204)
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ListView(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer = ListSerializer
    
class ContextView(viewsets.ModelViewSet):
    queryset = Context.objects.all()
    serializer = ContextSerializer