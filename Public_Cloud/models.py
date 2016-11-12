from django.db import models
class Users(models.Model):
		password = models.CharField(max_length=50)
		user_name = models.CharField(max_length=50,unique=True)
		user_email = models.CharField(max_length=100)
class Files(models.Model):
	 file_name = models.CharField(max_length=50)
	 #owner_name = models.ForeignKey(Users,to_field='user_name')
	 owner_name = models.CharField(max_length=50,default='admin')
