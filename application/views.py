from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
	def get(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id', None)
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			# json_data = JSONRenderer().render(serializer.data)
			# return HttpResponse(json_data, content_type='application/json')
			return JsonResponse(serializer.data)
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		# json_data = JSONRenderer().render(serializer.data)
		# return HttpResponse(json_data, content_type='application/json')
		return JsonResponse(serializer.data, safe=False)

	def post(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Record Created Successfully'}
			return JsonResponse(res)
		return JsonResponse(serializer.errors)

	def put(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=pythondata, partial=True)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data Updated'}
			return JsonResponse(res)
		return JsonResponse(serializer.errors)

	def delete(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		stu.delete()
		res = {'msg': 'Delete Successfully'}
		return JsonResponse(res)




def student_detail(request, pk):
	stu = Student.objects.get(id=pk)
	serializer = StudentSerializer(stu)
	# json_data = JSONRenderer().render(serializer.data)
	# return HttpResponse(json_data, content_type='application/json')
	return JsonResponse(serializer.data)


@csrf_exempt
def student_info(request):
	if request.method == 'GET':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id', None)
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			# json_data = JSONRenderer().render(serializer.data)
			# return HttpResponse(json_data, content_type='application/json')
			return JsonResponse(serializer.data)
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		# json_data = JSONRenderer().render(serializer.data)
		# return HttpResponse(json_data, content_type='application/json')
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Record Created Successfully'}
			return JsonResponse(res)
		return JsonResponse(serializer.errors)

	if request.method == 'PUT':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=pythondata, partial=True)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data Updated'}
			return JsonResponse(res)
		return JsonResponse(serializer.errors)

	if request.method == 'DELETE':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		stu.delete()
		res = {'msg': 'Delete Successfully'}
		return JsonResponse(res)


@csrf_exempt
def create_student(request):
	if request.method == 'POST':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data Created Successfully'}
			# json_data = JSONRenderer().render(res)
			# return HttpResponse(json_data, content_type='application/json')
			return JsonResponse(res, safe=False)
		# json_data = JSONRenderer().render(serializer.errors)
		# return HttpResponse(json_data, content_type='application/json')
		return JsonResponse(serializer.errors, safe=False)


