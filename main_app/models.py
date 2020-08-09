from django.db import models

state_choices = [
    ('Andhra_Pradesh','Andhra_Pradesh'),
    ('Arunachar_Pradesh','Arunachar_Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chattisgarh','Chattisgarh'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Haryana'),
    ('Himachar_Pradesh','Himachar_Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya_Pradesh','Madhya_Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil_Nadu','Tamil_Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar_Pradesh','Uttar_Pradesh'),
    ('West_Bengal','West_Bengal'),
]



# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField(default='')
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    query = models.CharField(max_length=600)

class Donor_details(models.Model):
    donor_id = models.AutoField
    donor_name = models.CharField(max_length=100)
    donor_bloodgroup = models.CharField(max_length=10)
    donor_address = models.CharField(max_length=500)
    donor_state = models.CharField(max_length=50)
    donor_district = models.CharField(max_length=50)
    donor_city = models.CharField(max_length=50)
    donor_pincode = models.IntegerField(default=0)
    donor_phone_number = models.IntegerField(default=0)
    donor_email_id = models.CharField(max_length=50)
    donor_profile_pic = models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.donor_name

class Blood_DATA(models.Model):
    State = models.CharField(max_length=20,choices=state_choices)
    District = models.CharField(max_length=20)
    BloodBank_Name = models.CharField(max_length=100)
    A_Positive_Blood = models.IntegerField(default=0)
    A_Negative_Blood = models.IntegerField(default=0)
    B_Positive_Blood = models.IntegerField(default=0)
    B_Negative_Blood = models.IntegerField(default=0)
    AB_Positive_Blood = models.IntegerField(default=0)
    AB_Negative_Blood = models.IntegerField(default=0)
    O_Positive_Blood = models.IntegerField(default=0)
    O_Negative_Blood = models.IntegerField(default=0)
    Last_Updated = models.DateTimeField()

    def __str__(self):
        return self.BloodBank_Name


