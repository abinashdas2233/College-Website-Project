from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from collegeapp.models import *
user=""
#admin section
def registration(request):
    if request.method=="POST":
        i=request.POST.get('id')
        nm=request.POST.get('name')
        add=request.POST.get('address')
        cn=request.POST.get('contactno')
        em=request.POST.get('email')
        rl=request.POST.get('role')
        pw=request.POST.get('password')
        us=userregistration(id=i,name=nm,address=add,contact_no=cn,email_id=em,role=rl,password=pw)
        print(us)
        us.save()


        return render(request,'A_addprofile.html')
from django.shortcuts import render
from .models import dues

def duesform(request):
    if request.method == 'POST':
        i = request.POST.get('id')
        nm = request.POST.get('name')
        br = request.POST.get('branch')
        fe = request.POST.get('fee')
        da = request.POST.get('due_amount')
        cd = request.POST.get('cleared_dues')

        try:
          
            existing_due = dues.objects.get(id=i)
            return render(request, 'loginfail.html')  
        except dues.DoesNotExist:
           
            new_due = dues(id=i, name=nm, branch=br, Fee=fe, due_amount=da, cleared_dues=cd)
            new_due.save()
            return render(request, 'A_dues.html')  

      
def viewduedetails(request):
    du=dues.objects.all()
    print("..........................................................",du)
    
    return render(request,'A_duedetails.html',context={'hk':du})
def updatedue(request):
    message = ''
    
    if request.method == 'POST':
        try:
            fid = request.POST.get('id')
            fam = int(request.POST.get('amount'))
            print(fid)
            print(fam)

            student = dues.objects.get(pk=fid)
            fixedfee = student.Fee
            dueamount = student.due_amount
            cleareddue = student.cleared_dues
            student.due_amount = fixedfee - fam
            student.cleared_dues = cleareddue + fam
            student.save()
            message='successfully updated'
            return render(request, 'A_updatedue.html', {'message': message})
        except Exception as e:
            message = f"An error occurred due to id mismatch or server issues"
    
    return render(request, 'A_updatedue.html', {'message': message})
def notificateon(request):
    if request.method=="POST":
        nmb=request.POST.get('no')
        nc=request.POST.get('notice')
        nt=notification(notice_no=nmb,notice=nc)
        nt.save()
        return render(request,'A_notification.html')


def deletfeed(request, contactno):
    try:
        obj = feedback.objects.filter(contactno=contactno)
        obj.delete()
        f=feedback.objects.all()
        return render(request,'A_viewfeedback.html',context={"uk":f})
    except feedback.DoesNotExist:
        return render(request, 'A_viewfeedback.html', {'error': 'Feedback not found.'})

#parent section
def parentdue(request): 
 return render(request, 'P_due.html')
def mapdue(request):
     
     if request.method == 'POST':
        i = request.POST.get('id')
        sk = dues.objects.get(pk=i)
        print('...........................',sk.name,'......',type(sk))
        return render(request,'P_viewdues.html',{"jk":[sk]})
def parentnotification(request):
    fd=notification.objects.all()
    return render(request,'P_notification.html',{"fd":fd})
def parentfeedback(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        ad=request.POST.get('address')
        cn=request.POST.get('contactno')
        
        ei=request.POST.get('email')
        rl=request.POST.get('role')
        msg=request.POST.get('message')
        sv=feedback(name=nm,address=ad,contactno=cn,email_id=ei,role=rl,message=msg)
        sv.save()
        
    return render(request,'P_feedback.html')

#student businesslogic section

def stmapdue(request):
     
     if request.method == 'POST':
        i = request.POST.get('id')
        sk = dues.objects.get(pk=i)
        print('...........................',sk.name,'......',type(sk))
        return render(request,'S_viewdues.html',{"jk":[sk]})
def  sendfeed(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        ad=request.POST.get('address')
        cn=request.POST.get('contactno')
        
        ei=request.POST.get('email')
        rl=request.POST.get('role')
        msg=request.POST.get('message')
        sv=feedback(name=nm,address=ad,contactno=cn,email_id=ei,role=rl,message=msg)
        sv.save()
        
    return render(request,'S_feedback.html')
def courseview(requet):
    
    if requet.method=='POST':
        branchname=requet.POST.get('branch')
        u=course.objects.filter(Branch=branchname)
        return render(requet,'courseview.html',{"i":u})
    
def linkdata(request, id):
    # Get course data based on the ID
    course_data = course.objects.filter(id=id)

    # Modify each course object's video link if necessary
    for data in course_data:
        if 'blob' in data.link:
            data.link = data.link.replace('blob', 'raw')  # Replace 'blob' with 'raw'

    return render(request, 'displaycourse.html', {'u': course_data})

    

#Teacher control
def uploadcours(request):
    if request.method == "POST":
        id=request.POST.get('id')
        sub = request.POST.get('sub')
        br = request.POST.get('branch')
        link = request.POST.get('link')
        cdata = course(id=id,subject=sub, Branch=br, link=link)
        cdata.save()
        
       
        

    return render(request, 'T_home.html')
def deletecourse(request):
    if request.method=="POST":
        iid=request.POST.get('id')
        do=course.objects.get(pk=iid)
        do.delete()
    return render(request, 'T_home.html')



