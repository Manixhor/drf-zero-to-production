

# Create your views here.


from rest_framework.views  import APIView
from rest_framework.response import Response

from .models import Student

#here api's can be created as functions or classes 

class StudentAPI(APIView):
    def post(self,request):
        print(request.data)

        #to save the api 

        new_student = Student(name=request.data['name'],age=request.data['age'])

        new_student.save()


        return Response("Created")