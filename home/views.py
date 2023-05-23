from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serialIzer import TodoSerializer
from .models import ToDo

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
