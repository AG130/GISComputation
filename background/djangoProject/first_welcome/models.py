from django.db import models
from django.contrib.auth.models import AbstractUser
import django

class User(AbstractUser):
    username = models.CharField(max_length=20, primary_key=True, db_index=True)
    password = models.CharField(max_length=100, null=False)
    useremail=models.CharField(max_length=100, null=False)

    admin_data = models.DateField(blank=True, default=django.utils.timezone.now)
    is_fzren = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class gis_table(models.Model):
    name = models.CharField(max_length=50)    #姓名
    id_card = models.CharField(max_length=20)   #身份证
    sex = models.CharField(max_length=2)    #性别
    # checkdate = models.CharField(max_length=20)   #检测日期
    checkdate = models.FloatField()   #检测日期

    result = models.CharField(max_length=20)    #结果
    responsibilityman=models.CharField(max_length=20)   #负责人

    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    locate_x=models.CharField(max_length=20)
    locate_y=models.CharField(max_length=20)

    locate_x_float=models.FloatField()
    locate_y_float=models.FloatField()

class positive_line_area(models.Model):
    center_lng=models.FloatField()
    center_lat=models.FloatField()
    center_radius=models.FloatField()
    line_points=models.CharField(max_length=500)

class positive_line(models.Model):
    line_id=models.CharField(max_length=20)
    people_name=models.CharField(max_length=20)
    people_id_card=models.FloatField()
    time=models.CharField(max_length=20)
    line_info=models.CharField(max_length=20)
    locate_x_float = models.FloatField()
    locate_y_float=models.FloatField()

class positive_info(models.Model):
    line_id=models.CharField(max_length=20)
    people_name=models.CharField(max_length=20)
    people_id_card=models.FloatField()
    time=models.CharField(max_length=20)
    line_info=models.CharField(max_length=20)

class check_point(models.Model):
    point_id=models.CharField(max_length=20)
    point_name=models.CharField(max_length=20)
    poind_address=models.CharField(max_length=100)
    locate_x_float = models.FloatField()
    locate_y_float=models.FloatField()


