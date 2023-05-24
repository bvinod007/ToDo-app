from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serialIzer import TodoSerializer, TimingTodoSerializer
from .models import ToDo, TimingTodo
from rest_framework import viewsets

# Create your views here.
@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'This is your home get request!'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'This is your home POST request!'
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': 'This is your home PATCH request!'
        })
    else:
        return Response({
            'status': 400,
            'message': 'This is yan invalid request!'
        })

@api_view(['GET'])
def get_todos(request):
    todo_objs = ToDo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)
    return Response({
        'status': True,
        'message': 'Success got todo objs',
        "data": serializer.data
    })

@csrf_exempt
@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Success todo post',
                "data": serializer.data
            })

        return Response({
            'status': False,
            'message': 'Invalid data',
            'data':  serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'something went wrong'
    })

@csrf_exempt
@api_view(['PATCH'])
def patch_todo(request):
    try:
        if request.method == 'PATCH':
            data = request.data
            if not data.get('uuid'):
                return Response({
                    'status': False,
                    'message': 'please provide uuid'
                })
            obj = ToDo.objects.get(uuid=data.get('uuid'))
            serializer = TodoSerializer(obj, data = data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': serializer.data
                })

            return Response({
                'status': True,
                'message': 'invalid data',
                'data': serializer.errors
            })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'something went wrong'
    })

@csrf_exempt
@api_view(['DELETE'])
def delete_todo(request, uuid):
    try:
        # print(uuid)
        # if not ToDo.objects.get('uuid'):
        #     return Response({
        #         'status': False,
        #         'message': 'please provide uuid'
        #     })
        data = ToDo.objects.get(pk=uuid)
        print(data)
        data.delete()
            
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Something went wrong!'
    })

class TodoViews(APIView):
    def get(self, request):
        todo_objs = ToDo.objects.all()
        serializer = TodoSerializer(todo_objs, many=True)
        return Response({
            'status': True,
            'message': 'Success got todo objs',
            "data": serializer.data
        })
    
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Success todo post',
                    "data": serializer.data
                })

            return Response({
                'status': False,
                'message': 'Invalid data',
                'data':  serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'something went wrong'
        })
    def delete(request, uuid):
        try:
            if not ToDo.objects.get('uuid'):
                return Response({
                    'status': False,
                    'message': 'please provide uuid'
                })

            data = ToDo.objects.get(uuid=uuid)
            data.delete()
            
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong!'
        })

    
class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

    @action(detail= False, methods=['get'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'status': True,
            'message': 'Success data',
            'data': serializer.data
        })

    @action(detail=False, methods=['post'])
    def add_timing_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'success operation',
                    'data': serializer.data
                })
            
            return Response({
                'status': False,
                'message': 'Invalid data',
                'data': serializer.data
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })
