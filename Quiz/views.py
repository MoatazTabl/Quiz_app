from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import QuesModel
from .serializers import QuestionSerializer

# Create your views here.


#request 
#post -save to databse
#get - disply

def index(request):
    if request.method=='POST':
        post=QuesModel()
        post.question=request.POST.get('question')
        post.op1=request.POST.get('cho1')
        post.op2=request.POST.get('cho2')
        post.op3=request.POST.get('cho3')
        post.op4=request.POST.get('cho4')
        post.ans=request.POST.get('ans')
        post.save()

    return render(request,"index.html")

def output(request):
    data=QuesModel.objects.all().order_by('question')
    response={
        'Question':list(data.values('question','op1','op2','op3','op4','ans')),
        
    }
    return JsonResponse(response)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def beauty_output(request):
    get=QuesModel.objects.all()
    serializer=QuestionSerializer(get,many=True)
    return Response(serializer.data)