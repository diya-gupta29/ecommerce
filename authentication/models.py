
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
state_list = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chandigarh', 'Chandigarh'),
('Chhattisgarh', 'Chhattisgarh'),
('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'),
('Daman and Diu', 'Daman and Diu'),
('Delhi', 'Delhi'),
('Lakshadweep', 'Lakshadweep'),
('Puducherry', 'Puducherry'),
('Goa', 'Goa'),
('Gujarat', 'Gujarat'),
('Haryana', 'Haryana'),
('Himachal Pradesh', 'Himachal Pradesh'),
('Jammu and Kashmir', 'Jammu and Kashmir'),
('Jharkhand', 'Jharkhand'),
('Karnataka', 'Karnataka'),
('Kerala', 'Kerala'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Maharashtra', 'Maharashtra'),
('Manipur', 'Manipur'),
('Meghalaya', 'Meghalaya'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland'),
('Odisha', 'Odisha'),
('Punjab', 'Punjab'),
('Rajasthan', 'Rajasthan'),
('Sikkim', 'Sikkim'),
('Tamil Nadu', 'Tamil Nadu'),
('Telangana', 'Telangana'),
('Tripura', 'Tripura'),
('Uttar Pradesh', 'Uttar Pradesh'),
('Uttarakhand', 'Uttarakhand'),
('West Bengal', 'West Bengal'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    gender_choice=((u'M',u'Male'),(u'F',u'Female'),(u'O',u'OTHER'))
    gender=models.CharField(max_length=2,choices=gender_choice,default='O')
    phone_number=models.CharField(max_length=12,default='')
    locality = models.CharField(max_length = 300)
    city = models.CharField(max_length = 100)
    zipcode = models.IntegerField()
    state = models.CharField(choices = state_list, max_length = 100)

    def __str__(self):
        return str(self.id)
