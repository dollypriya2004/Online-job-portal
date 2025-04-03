from django.urls import path 
from . import views 
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.home,name="home"),
    path('abt/',views.about,name="about"),
    path('cnt/',views.contact,name="contact"),
    path('hlp/',views.help,name="help"),
    path('fdb/',views.feedback,name="feedback"),
    path('reg/',views.register,name="rg"),
    path('lgn/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
    path('lgot/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
    path('rlst/',views.recruiterlist,name="rlst"),
    path('aplst/',views.applicantlist,name="aplst"),
    path('rpfle/',views.rc_profile,name="rpf"),
    path('apfle/',views.ap_profile,name="apf"),
    path('urpfle/',views.updrc_profile,name="urpf"),
    path('uapfle/',views.updap_profile,name="uapf"),
    path('chge/',views.chngpwd,name="cge"),
    path('aurcpfle/<int:h>/',views.aurc_profile,name="aurcpfle"),
    path('jlst/',views.joblist,name="jlst"),
    path('pj/',views.postjob,name="pj"),
    path('ujlst/<int:h>/',views.upjob,name="uj"),
    path('dlt/<int:h>/',views.delete,name="dlt"),
    path('apdlt/<int:h>/',views.deleteapp,name="apdlt"),
    path('jbdlt/<int:h>/',views.deletejob,name="jbdlt"),
    path('rap/<int:h>/',views.rapplications,name="rap"),
    path('ajlst/',views.ajoblist,name="ajlst"),
    path('apl/',views.appliedlist,name="apl"),
    path('app/<int:h>/',views.application,name="app"),
    path('uapp/<int:h>/',views.uapplication,name="uapp"),
    path('apls/',views.applications,name="apls"),
    path('uasp/<int:h>/',views.uaspr,name="uaspr"),
    path('ruaps/<int:h>/',views.ruapstatus,name="ruaps"),
]
