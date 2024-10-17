from django.shortcuts import render
from collegeapp.models import *
# Create your views here.


def login(request):

    return render(request,'index.html')

#login validation
def validation(request):
    if request.method == 'POST':
        try:
            incomeing_email = request.POST.get('email')
            print(incomeing_email)
            incomeing_password = request.POST.get('password')

            # Attempt to get the user from the database
            d = userregistration.objects.get(email_id=incomeing_email)
            roles = d.role

            # Validate the password
            if incomeing_password == d.password:  # d.password is fetched from the database
                if roles == 'admin':
                    return render(request, 'A_home.html')
                elif roles == 'student':
                    return render(request, 'S_home.html')
                elif roles == 'parent':
                    return render(request, 'P_home.html')
                elif roles == 'teacher':
                    return render(request, 'T_home.html')
            else:
                return render(request, 'loginfail.html')
        
        except userregistration.DoesNotExist:
            # Handle the case where the email is not found in the database
            print("User with this email does not exist.")
            return render(request, 'loginfail.html')

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An error occurred: {e}")
            return render(request, 'loginfail.html')

def forgetpass(request):
    return render(request,'forget.html')
#password change authentication
def passwordcheck(request):
    if request.method == "POST":
        email = request.POST.get('email')
        action = request.POST.get('authmethod')
        uinput = request.POST.get('previous')
        cinput = request.POST.get('password')
        
        try:
            if action == 'id':
                did = userregistration.objects.get(pk=uinput)
                if str(uinput) == str(did.id):  
                    did.password = cinput
                    did.save()
                    
                    return render(request, 'index.html')
                else:
                   
                    return render(request, 'loginfail.html')
            else:
                us = userregistration.objects.get(email_id=email)
                if uinput == us.password:
                    us.password = cinput
                    us.save()
                    
                    return render(request, 'index.html')
                else:
                    
                    return render(request, 'loginfail.html')
        except :
            
            return render(request, 'loginfail.html')
        
    else:
        return render(request, 'forget.html')
    

    
#admin nav control
def adminhome(request):
    return render(request,'A_home.html')
def admin_addprofile(request):
    return render(request,'A_addprofile.html')
def admin_dues(request):
    return render(request,'A_dues.html')
def admin_notification(request):
    return render(request,'A_notification.html')
def admin_feedback(request):
    f=feedback.objects.all()

    return render(request,'A_viewfeedback.html',context={"uk":f})
def admin_view(request):
    u=userregistration.objects.all()
    return render(request,'A_viewprofile.html',{'hk':u})
#parent nav control
def parenthome(request):
    return render(request,'P_home.html')
#student nav control
def studenthome(request):
    return render(request,'S_home.html')
def  studentdues(request):
    return render(request,'S_dues.html')
def studentfeedbacks(request):
    return render(request,'S_feedback.html')
def studentnotification(request):
    fd=notification.objects.all()
    return render(request,'S_notification.html',{"fd":fd})
def  studentstudymaterial(request):
    return render(request,'S_studymaterial.html')
def studentresult(request):
    return render(request,'S_result.html')


