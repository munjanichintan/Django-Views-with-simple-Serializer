from .models import Student
from rest_framework import serializers


# Validators

def start_with_c(value):
	if value[0].lower() != 'c':
		raise serializers.ValidationError('Name should be start with C')

class StudentSerializer(serializers.Serializer):
	# id = serializers.IntegerField()
	name = serializers.CharField(max_length=100, validators=[start_with_c])
	roll = serializers.IntegerField()
	city = serializers.CharField(max_length=100)

	def create(self, validate_data):
		return Student.objects.create(**validate_data)

	def update(self, instance, validate_data):
		instance.name = validate_data.get('name', instance.name)
		instance.roll = validate_data.get('roll', instance.roll)
		instance.city = validate_data.get('city', instance.city)
		instance.save()
		return instance


	# Field Level Validation for roll field

	def validate_roll(self, value):
		if value >= 200:
			raise serializers.ValidationError('Seat Full')
		return value

	# Object Level Validation

	def validate(self, data):
		name = data.get('name')
		city = data.get('city')
		if name.lower() == 'chintan' and city.lower() != 'surat':
			raise serializers.ValidationError('City must be Surat')
		return data