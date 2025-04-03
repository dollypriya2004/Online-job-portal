from .models import User,Application,ApProfile,RcProfile,job
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms 

class AusForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
    class Meta:
        model = User
        fields = ["username","uid","role_type"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Applicant Name",
                "required":"true",
            }),
            "uid":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Unique Id",
                "required":"true",
            }),
            "role_type":forms.Select(attrs={
                "class":"form-control",
            }),
        }
class UserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","uid","role_type","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Unique Id",
			}),
        "role_type":forms.Select(attrs={
            "class":"form-control my-2",
        }),
        "email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mailid",
			}),
		}
  
class UspForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","mobile","gender","pfimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"mobile":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
       
class ApprForm(forms.ModelForm):
    class Meta:
        model = ApProfile
        fields = ["degree","college","address","dob","cert"]
        widgets ={
            "degree":forms.Select(attrs={
                "class":"form-control my-2",
            }),
            "college":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"College Name",
            }),
            "address":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Address",
            }),
            "dob":forms.DateInput(attrs={
            "class":"form-control my-2",
            "type":"date",
        }),
        }
        
  
class RcprForm(forms.ModelForm):
    class Meta:
        model = RcProfile
        fields = ["c_name","est_year","Owner","dob","cert"]
        widgets ={
            "c_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Company Name",
            }),
            "est_year":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Established Year",
            }),
            "Owner":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Owner Name",
            }),
            "dob":forms.DateInput(attrs={
            "class":"form-control my-2",
            "type":"date",
        }),
        }       

class ArcprForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["desg"]
        widgets={
            "desg":forms.Select(attrs={
                "class":"form-control my-2",
            }),
        }
class asprForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["desg"]
        widgets={
            "desg":forms.Select(attrs={
                "class":"form-control my-2",
            })
        }
class AppForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["resume"]
        widgets ={}
        
class UaplForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["resume"]
        widgets = {
           
        }
               
class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ["j_title","end_date","requirements","salary","description"]
        widgets ={
            "j_title":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Job title",
            }),
            "end_date":forms.DateInput(attrs={
                "class":"form-control my-2",
                "type":"date",
                "placeholder":"Deadline",
            }),
            "requirements":forms.Textarea(attrs={
                "class":"form-control my-2",
                "rows":3,
                "placeholder":"Requirements",
            }),
            "salary":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "min":3,
                "max":20,
                "placeholder":"Salary",
            }),
            "description":forms.Textarea(attrs={
                "class":"form-control my-2",
                "rows" : 5,
                "placeholder":"Job Description",
            }),
        }
        
  
class RUpaplForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["desc","ap_status"]
        widgets ={
            "ap_status":forms.Select(attrs={
                "class":"form-control my-2",
            }),
            "desc":forms.Textarea(attrs={
                "class":"form-control my-2",
                "rows":3,
            }),
        } 
        
class UpjoForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ["j_status","j_title","end_date","requirements","salary","description"]
        widgets = {
            "j_status":forms.Select(attrs={
                "class":"form-control my-2",
            }),
            "j_title":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Job title",
            }),
            "end_date":forms.DateInput(attrs={
                "class":"form-control my-2",
                "type":"date",
                "placeholder":"Deadline",
            }),
            "requirements":forms.Textarea(attrs={
                "class":"form-control my-2",
                "rows":3,
                "placeholder":"Requirements",
            }),
            "salary":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "min":3,
                "max":20,
                "placeholder":"Salary",
            }),
            "description":forms.Textarea(attrs={
                "class":"form-control my-2",
                "rows" : 5,
                "placeholder":"Job Description",
            }),
        }
             
class ChgPwdForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Old Password"}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"New Password"}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = "__all__" 