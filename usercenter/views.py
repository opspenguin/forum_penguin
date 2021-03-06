#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.models import User
from models import ActivateCode
from django.template import RequestContext
import uuid
import datetime
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="GET":
        return render_to_response("usercenter_register.html",{},context_instance=RequestContext(request))
    else:
        username=request.POST['username'].strip()
        email=request.POST['email'].strip()
        password=request.POST['password'].strip()
        re_password=request.POST['re_password'].strip()

        if not username or not email or not password or not re_password:
            messages.add_message(request,messages.ERROR,u"任何字段都不能为空")
            return render_to_response("usercenter_register.html",{},context_instance=RequestContext(request))
        if password != re_password:
            messages.add_message(request,messages.ERROR,u"两次密码不同")
            return render_to_response("usercenter_register.html",{},context_instance=RequestContext(request))
        if User.objects.filter(username=username).count()>0:
            messages.add_message(request,messages.ERROR,u"用户已存在")
            return render_to_response("usercenter_register.html",{},context_instance=RequestContext(request))
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.is_active=False
            user.save()

            new_code=str(uuid.uuid4()).replace("-","")
            expire_time=datetime.datetime.now()+datetime.timedelta(days=2)
            code_record=ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
            code_record.save()

            activate_link="http://%s%s"%(request.get_host(),reverse("usercenter_activate",args=[new_code]))
            send_mail(u"激活邮件",u"激活链接为：%s"%(activate_link),'1004020240@qq.com',[email],fail_silently=False)

        return redirect(reverse("login"))

def activate(request,code):
    query=ActivateCode.objects.filter(code=code,expire_timestamp__gte=datetime.datetime.now())
    if query.count()>0:
        code_record=query[0]
        code_record.owner.is_active=True
        code_record.owner.save()
        return HttpResponse(u"激活成功")
    else:
        return HttpResponse(u"激活失败")