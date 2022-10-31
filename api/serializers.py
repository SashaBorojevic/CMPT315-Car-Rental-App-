from rest_framework import serializers
from .models import Branch, Customer, Car, CarType, Employee, Rental


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('branchID', 'branch_phone', 'province', 'city', 'postal_code', 'street_number', 'street_name', 'unit_number')
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('eID', 'branchID', 'first_name', 'last_name', 'email', 'employee_phone', 'password', 'salary', 'rank', 'DOB', 'province', 'city', 'postal_code', 'street_number', 'street_name', 'unit_number' )

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('cID', 'first_name', 'last_name', 'drivers_license', 'email', 'customer_phone', 'DOB', 'gold_member', 'province', 'city', 'postal_code', 'street_number', 'street_name', 'unit_number')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('carID', 'manufacturer', 'model', 'fuel_type', 'colour', 'license_plate', 'status', 'mileage','car_type', 'branchID')

class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ('typeID', 'description', 'daily_cost', 'weekly_cost', 'monthly_cost', 'late_fee', 'change_branch_fee')

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('rentalID', 'date_from', 'date_to', 'date_returned', 'total_cost', 'license_plate', 'eID', 'cID')
    