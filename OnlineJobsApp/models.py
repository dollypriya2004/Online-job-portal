from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    k = [
        ('0','Guest'),
        ('1','Recruiter'),
        ('2','Applicant'),
    ]
    g = [
        ('0','--- Select Your Gender ---'),
		('1','Male'),
		('2','Female'),
    ]
    d = [
        ('0','General'),
        ('1','Super'),
    ]
    uid = models.CharField(max_length=12)
    mobile = models.CharField(max_length=10,null=False,blank=False)
    pfimg = models.ImageField(upload_to='Profiles/',default='apl.png')
    email = models.EmailField(max_length=254)
    gender = models.CharField(choices=g,default='0',max_length=5)
    role_type = models.CharField(choices=k,max_length=5,default='0')
    desg = models.CharField(choices=d,max_length=5,default='0')
    
class Application(models.Model):
    y = [
        ('vp','Verification Pending'),
        ('v','Verified'),
        ('s','Selected'),
        ('d','Declined'),
    ]
    ap_status = models.CharField(choices=y,default='vp',max_length=10)
    app_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='Attachments/')
    desc = models.CharField(max_length=200,blank=False)
    ab = models.ForeignKey(User,on_delete=models.CASCADE,related_name="App ID+")
    job = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Job ID+")

    
class job(models.Model):
    j = [
        ('o','Opened'),
        ('c','Closed'),
    ]
    j_title = models.CharField(max_length=20)
    end_date = models.DateTimeField()
    p_date = models.DateTimeField(auto_now_add=True)
    requirements =models.TextField()
    j_status=models.CharField(choices=j,default='o',max_length=5)
    salary = models.IntegerField(default=3)
    description = models.CharField(max_length=500,blank=False)
    jb = models.ForeignKey(User,on_delete=models.CASCADE)

class ApProfile(models.Model):
    d=[
        ('0','--Choose your degree '),
        ('1','B-tech'),
        ('2','M-tech'),
        ('3','MBA'),
        ('4','PG'),
    ]
    dob = models.DateTimeField()
    degree = models.CharField(choices=d,max_length=10)
    college = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    astatus = models.BooleanField(default=False)
    ac = models.OneToOneField(User,on_delete=models.CASCADE)
    cert = models.FileField(upload_to='Attachments/',default='valid.png')

class RcProfile(models.Model):
    dob = models.DateTimeField()
    c_name=models.CharField(max_length=20,default=None)
    est_year = models.CharField(max_length=4)
    Owner = models.CharField(max_length=20)
    rstatus = models.BooleanField(default=False)
    rc = models.OneToOneField(User,on_delete=models.CASCADE)
    cert = models.FileField(upload_to='Attachments/',default='proof.png')
    