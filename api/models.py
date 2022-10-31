from django.db import models
   

class Branch(models.Model):
    branchID = models.AutoField(primary_key=True)
    branch_phone = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.branchID)

class Employee(models.Model):
    eID = models.AutoField(primary_key=True)
    branchID = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 200)
    employee_phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    rank = models.CharField(max_length=30)
    DOB = models.DateField()
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.eID)


class Customer(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    cID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    drivers_license = models.CharField(max_length=30)
    email = models.EmailField(max_length = 200)
    customer_phone = models.CharField(max_length=30)
    DOB = models.DateField()
    gold_member = models.BooleanField(choices=BOOL_CHOICES)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    street_number = models.CharField(max_length=30)
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.cID)


class CarType(models.Model):
    typeID = models.AutoField(primary_key=True)
    description = models.TextField(blank = True)
    daily_cost = models.DecimalField(max_digits=6, decimal_places=2)
    weekly_cost = models.DecimalField(max_digits=6, decimal_places=2)
    monthly_cost = models.DecimalField(max_digits=6, decimal_places=2)
    late_fee = models.DecimalField(max_digits=6, decimal_places=2)
    change_branch_fee = models.DecimalField(max_digits=6, decimal_places=2)


class Car(models.Model):
    carID = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    license_plate = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    mileage = models.CharField(max_length=30)
    car_type = models.ForeignKey(CarType,on_delete=models.CASCADE,null=True)
    branchID = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return str(self.license_plate)

class Rental(models.Model):
    rentalID = models.AutoField(primary_key=True)
    date_from = models.DateField()
    date_to = models.DateField()
    date_returned = models.DateField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    license_plate = models.ForeignKey(Car,on_delete=models.CASCADE,null=True)
    #gold_member = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    eID = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    cID = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    
