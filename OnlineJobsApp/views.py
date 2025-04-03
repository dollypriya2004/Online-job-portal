from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User,RcProfile,Application,ApProfile,job
from .forms import AusForm,UserForm,UspForm,AppForm,RcprForm,ApprForm,ChgPwdForm,RUpaplForm,UpjoForm,JobForm,ArcprForm,asprForm,UaplForm
from django.core.mail import send_mail 
from django.conf import settings
# Create your views here.
def home(request):
    return render(request,'html/home.html')

def about(request):
    return render(request,'html/about.html')

def contact(request):
    return render(request,'html/contact.html')

def help(request):
    return render(request,'html/help.html')

def feedback(request):
    return render(request,'html/feedback.html')

def register(request):
    if request.method == "POST":
        f = UserForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,"User Created Successfully")
            subject = "Welcome to Online Jobs Portal "
            email_from = settings.EMAIL_HOST_USER
            username = request.POST['username']
            role_type = request.POST['role_type']
            message = f"Congratulations {username} for registering into online jobs portal."
            if role_type == 1:
                message+="As you are registered as recuiter , inorder to proceed to your usual activities you need to complete your profile.Hope you will enjoy our service."
            elif role_type == 2:
                message+="You found the right way to make yourself visible to the top comanies in current generation..\nGo ahead and complete your profile..\n   So many jobs are waiting for you"
            receiver = request.POST['email']
            b=send_mail(subject,message,email_from,[receiver])
            if b==1:
                messages.success(request,"Mail Sent Successfully")
            else:
                messages.warning(request,"Mail not sent")
            return redirect('/lgn')
    else:
        f = UserForm()
        return render(request,'html/Register.html',{'g':f})


def recruiterlist(request):
    p = User.objects.all()
    c=[]
    for i in p:
        if i.role_type == "1":
            c.append(i)
    n,m={},{}
    if request.method == "POST":
        s = AusForm(request.POST)
        if s.is_valid():
            s.save()
            messages.success(request,'Recruiter Created Successfully')
            return redirect('/rlst')
        else:
            n[s]=s.errors
    for j in n.values():
        for v in j.items():
            m[v[0]]=v[1]
    s = AusForm()
    return render(request,'html/Recruiterlist.html',{'w':s,'p':m.items(),'k':c})

def applicantlist(request):
    p = User.objects.all()
    c=[]
    for i in p:
        if i.role_type == "2":
            c.append(i)
    n,m={},{}
    if request.method == "POST":
        s = AusForm(request.POST)
        if s.is_valid():
            s.save()
            messages.success(request,'Applicant Created Successfully')
            return redirect('/aplst')
        else:
            n[s]=s.errors
    for j in n.values():
        for v in j.items():
            m[v[0]]=v[1]
    s = AusForm()
    return render(request,'html/Applicantlist.html',{'w':s,'p':m.items(),'k':c})

def rc_profile(request):
    return render(request,'html/rc_profile.html')
    
def ap_profile(request):
    return render(request,'html/ap_profile.html')
    
def updrc_profile(request):
    k = User.objects.get(id=request.user.id)
    t = RcProfile.objects.all()
    m = []
    for i in t:
        m.append(i.rc_id)
    if request.user.id not in m:
        if request.method == "POST":
            h = UspForm(request.POST,request.FILES,instance=k)
            y = RcprForm(request.POST)
            if h.is_valid() and y.is_valid():
                h.save()
                b = y.save(commit=False)
                b.rc_id=request.user.id
                b.desg = '0'
                b.rstatus=1
                b.save()
                messages.success(request,"Recruiter Profile Updated..")
                subject = "Update of your profile on Online Jobs Portal "
                email_from = settings.EMAIL_HOST_USER
                username = k.username
                message = f"Congratulations {username} for updating your profile on online jobs portal.\n"
                message+="As you have updated your profile,now you can proceed with your recruitments by posting jobs.Hope you will enjoy our service."
                receiver = k.email
                b=send_mail(subject,message,email_from,[receiver])
                return redirect('/rpfle')
        y = RcprForm()
        h = UspForm(instance=k)
        return render(request,'html/urc_profile.html',{'e':h,'t':y})
    else:
            p = RcProfile.objects.get(rc_id=request.user.id)
            if request.method == "POST":
                h = UspForm(request.POST,request.FILES,instance=k)
                y = RcprForm(request.POST,instance=p)
                if h.is_valid() and y.is_valid():
                    h.save()
                    y.save()
                    messages.success(request,"Recruiter Profile Updated..")
                    subject = "Update of your profile on Online Jobs Portal "
                    email_from = settings.EMAIL_HOST_USER
                    username = k.username
                    message = f"Congratulations {username} for updating your profile on online jobs portal.\n"
                    message+="As you have updated your profile,now you can proceed with your recruitments by posting jobs.Hope you will enjoy our service."
                    receiver = k.email
                    b=send_mail(subject,message,email_from,[receiver])
                    return redirect('/rpfle')
            y = RcprForm(instance=p)
            h = UspForm(instance=k)
            return render(request,'html/urc_profile.html',{'e':h,'t':y})
	
def updap_profile(request):
    k = User.objects.get(id=request.user.id)
    t = ApProfile.objects.all()
    m = []
    for i in t:
        m.append(i.ac_id)
    if request.user.id not in m:
        if request.method == "POST":
            h = UspForm(request.POST,request.FILES,instance=k)
            y = ApprForm(request.POST)
            if h.is_valid() and y.is_valid():
                h.save()
                b = y.save(commit=False)
                b.ac_id=request.user.id
                b.desg='0'
                b.astatus=1
                b.save()
                messages.success(request,"Applicant Profile Updated..")
                subject = "Update of your profile on Online Jobs Portal "
                email_from = settings.EMAIL_HOST_USER
                username = k.username
                message = f"Congratulations {username} for updating your profile on online jobs portal.\n"
                message+="As you have updated your profile,now you can proceed with your job search by applying.Hope you will enjoy our service."
                receiver = k.email
                b=send_mail(subject,message,email_from,[receiver])
                return redirect('/apfle')
        y = ApprForm()
        h = UspForm(instance=k)
        return render(request,'html/uap_profile.html',{'e':h,'t':y})
    else:
            p = ApProfile.objects.get(ac_id=request.user.id)
            if request.method == "POST":
                h = UspForm(request.POST,request.FILES,instance=k)
                y = ApprForm(request.POST,instance=p)
                if h.is_valid() and y.is_valid():
                    h.save()
                    y.save()
                    messages.success("Applicant Profile Updated..")
                    subject = "Update of your profile on Online Jobs Portal "
                    email_from = settings.EMAIL_HOST_USER
                    username = k.username
                    message = f"Congratulations {username} for updating your profile on online jobs portal.\n"
                    message+="As you have updated your profile,now you can proceed with your recruitments by posting jobs.Hope you will enjoy our service."
                    receiver = k.email
                    b=send_mail(subject,message,email_from,[receiver])
                    return redirect('/apfle')
            y = ApprForm(instance=p)
            h = UspForm(instance=k)
            return render(request,'html/uap_profile.html',{'e':h,'t':y})

def aurc_profile(request,h):
    k = User.objects.get(id=h)
    if request.method == "POST":
            y = ArcprForm(request.POST,instance=k)
            if y.is_valid():
                y.save()
                return redirect('/rlst')
    y = ArcprForm(instance=k)
    return render(request,'html/aurc_profile.html',{'t':y})

def delete(request,h):
    k = User.objects.get(id=h)
    p=0
    if k.role_type=='1':
        p=1
    k.delete()
    if p==1:
        return render(request,'html/Recruiterlist.html')
    else:
        return render(request,'html/Applicantlist.html')
def deleteapp(request,h):
    k = Application.objects.get(id=h)
    k.delete()
    p = Application.objects.filter(ab_id=request.user.id)
    return render(request,'html/appliedlist.html',{'h':p})

def deletejob(request,h):
    k = job.objects.get(id=h)
    k.delete()
    p = job.objects.filter(jb_id = request.user.id)
    return render(request,'html/joblist.html',{'h':p})

def joblist(request):
    p = job.objects.filter(jb_id=request.user.id)
    return render(request,'html/joblist.html',{'h':p})

def ajoblist(request):
    k = job.objects.all()
    p=[]
    for i in k:
        if i.j_status == 'o':
            p.append(i)
    return render(request,'html/ajoblist.html',{'h':p})

def appliedlist(request):
    k = Application.objects.filter(ab_id=request.user.id)
    return render(request,'html/appliedlist.html',{'h':k})

def postjob(request):
    if request.method=="POST":
        d=JobForm(request.POST,request.FILES)
        if d.is_valid():
            w=d.save(commit=False)
            w.jb_id = request.user.id
            w.save()
            if request.user.desg=='1':
                p=User.objects.get(role_type='2')
                for i in p:
                    subject = "New job posted by top company on Online Jobs Portal "
                    email_from = settings.EMAIL_HOST_USER
                    username = i.username
                    message = f"Heyy {username} , grab this brilliant opportunity on your very own online jobs portal.\n"
                    message+="It is if not now then never opportunity comes for you . Take it with both hands and let the result whatever it be.\nHope you will enjoy our service."
                    receiver = k.email
                    b=send_mail(subject,message,email_from,[receiver])
            return redirect('/jlst')
    d=JobForm()
    return render(request,'html/postjob.html',{'z':d})

def upjob(request,h):
    b = job.objects.get(id=h)
    if request.method == "POST":
        g = UpjoForm(request.POST,instance=b)
        if g.is_valid():
            g.save()
            return redirect('/jlst')
    g = UpjoForm(instance=b)
    return render(request,'html/upjob.html',{'v':g}) 

def rapplications(request,h):
    p = Application.objects.filter(job_id = h)
    q = []
    t=User.objects.all()
    for i in p:
        l=[]
        temp=0
        for k in t:
            if k.id==i.ab_id:
                l.append(k)
                l.append(k.username)
                l.append(k.desg)
                l.append(i.app_date)
                l.append(i.resume)
                l.append(i.ap_status)
                l.append(i.id)
                temp=1
        if temp==1:
            q.append(l)
    for i in q:
        print(i[0])
    return render(request,'html/rapplications.html',{'h':q})

def ruapstatus(request,h):
    p = Application.objects.get(id=h)
    k = job.objects.get(id=p.job_id)
    if request.method=="POST":
        g = RUpaplForm(request.POST,instance=p)
        if g.is_valid():
            g.save()
            l=User.objects.get(id=p.ab_id)
            subject = "Update of your application status on Online Jobs Portal "
            email_from = settings.EMAIL_HOST_USER
            username = l.username
            message = f"Heyy {username} ,there is an update on your application on online jobs portal.\n"
            message+="It is better you quickly having a look at it.Hope you will enjoy our service."
            receiver = l.email
            b=send_mail(subject,message,email_from,[receiver])
            return redirect('rap',h=k.jb_id)
    g = RUpaplForm(instance=p)  
    return render(request,'html/ruapstatus.html',{'v':g,'k':k})

def application(request,h):
    if request.method == "POST":
        d = AppForm(request.POST,request.FILES)
        if d.is_valid():
            w = d.save(commit=False)
            w.ab_id = request.user.id
            w.job_id = h
            w.save()
            return redirect('/apls')
    d = AppForm()
    return render(request,'html/application.html',{'z':d})

def applications(request):
    d = Application.objects.filter(ab_id = request.user.id )
    return render(request,'html/appliedlist.html',{'c':d})

def uapplication(request,h):
    d = Application.objects.filter(id=h).first()
    if request.method=="POST":
        y = UaplForm(request.POST,instance=d)
        if y.is_valid():
            y.save()
            return redirect('/apl')
    y = UaplForm(instance=d)
    return render(request,'html/uapplication.html',{'v':y})
    
def uaspr(request,h):
    k = User.objects.get(id=h)
    if request.method == "POST":
            y = asprForm(request.POST,instance=k)
            if y.is_valid():
                y.save()
                return redirect('/apfle')
    y = asprForm(instance=k)
    return render(request,'html/uasprofile.html',{'t':y})

def chngpwd(request):
    if request.method=="POST":
        n = ChgPwdForm(user = request.user,data=request.POST)
        if n.is_valid():
            n.save()
            return redirect('/')
    n = ChgPwdForm(user=request)
    return render(request,'html/changepassword.html',{'h':n})