

from .models import birthday_data
from .serializers import birthdayserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.



class birthdayAPI(APIView):
    def get(self,request,userid=None,format=None):
        userid = userid
        stu = birthday_data.objects.filter(user_id=userid)
        # stu = birthday_data.objects.all()
        serializer = birthdayserializer(stu,many=True)
        print(serializer.data)
        return Response(serializer.data)   

    def post(self,request,userid=None,format=None):
        serializer=birthdayserializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            print(serializer.data)
            res = {'msg' : 'Data created'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def put(self,request,userid=None,pk=None,format=None):
        userid=userid
        id=pk
        print(id)
        stu = birthday_data.objects.get(id=id,user_id=userid)
        serializer = birthdayserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            res = {'msg' : 'Data updated'}
            return Response(res,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,userid=None,pk=None,format=None):
        userid=userid
        id=pk
        stu = birthday_data.objects.get(id=id,user_id=userid)
        stu.delete()
        res = {'msg' : 'Data Deleted'}
        return Response(res,status=status.HTTP_200_OK)



# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request,pk=None):
#     if request.method=="GET":
#         id=pk
#         if id is not None:
#             stu = student.objects.get(id=id)
#             print(stu)
#             serializer = studentserializer(stu)
#             print(serializer.data)
#             return Response(serializer.data)
#         stu = student.objects.all()
#         serializer = studentserializer(stu,many=True)
#         print(serializer.data)
#         return Response(serializer.data)

#     if request.method=="POST":
#         serializer=studentserializer(data=request.data)
#         if serializer.is_valid():
            
#             serializer.save()
#             print(serializer.data)
#             res = {'msg' : 'Data created'}
#             return Response(res,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method=="PUT":
#         id=pk
#         stu = student.objects.get(id=id)
#         serializer = studentserializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             res = {'msg' : 'Data updated'}
#             return Response(res,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method=="DELETE":
#         id=pk
#         stu = student.objects.get(id=id)
#         stu.delete()
#         res = {'msg' : 'Data Deleted'}
#         return Response(res,status=status.HTTP_200_OK)