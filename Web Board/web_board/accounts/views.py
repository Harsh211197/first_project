from .forms import BoardRegistrationform,Registrationform, TopicRegistrationform
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Board,Topic
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.db.models import Q

def delete(modelname,id):
    try:
        modelname.objects.get(id=id).delete()
    except modelname.DoesNotExist:       
        return HttpResponse("Sorry !Not Found")

# def update(modelname,modelform,urlname,id,request):
#     try:
#         model=modelname.objects.get(pk=id) 
#         form=modelform(request.POST if request.method == 'POST' else None,instance=model)
#         if request.method == 'POST':
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(urlname)
#         else:
#            form=modelform()
#     except modelname.DoesNotExist:       
#         return HttpResponse("Not Found")

def homepage(request):
    if request.user.is_superuser:
        boards=Board.objects.all()    
    else:
        boards=Board.objects.filter(board_starter=request.user.id)    
    return render(request,'enroll/homepage.html',{'boards':boards})

def board_update(request,id):
    # update(Board,BoardRegistrationform,'/home/',id,request)
    # return render(request,'enroll/updateboard.html',{'update': BoardRegistrationform()})    
    try:
        board=Board.objects.get(pk=id) 
        board_form=BoardRegistrationform(request.POST if request.method == 'POST' else None,instance=board)
        if request.method == 'POST':
            if board_form.is_valid():
                board_form.save()
                return HttpResponseRedirect("/home/")
        else:
            board_form=BoardRegistrationform()
        return render(request,'enroll/updateboard.html',{'update': BoardRegistrationform(instance=board)})
    except Board.DoesNotExist:       
        return HttpResponse("Sorry !Not Found")

def board_delete(request,id):
        delete(Board,id)
        return HttpResponseRedirect('/home/')
    
def topic_update(request,id):
    try:
        topic=Topic.objects.get(pk=id)
        topic_form=TopicRegistrationform(request.POST if request.method == 'POST' else None,instance=topic)
        if request.method == 'POST':
            if topic_form.is_valid():
                topic_form.save()
                return HttpResponseRedirect("/home/")
        return render(request,'enroll/updatetopic.html',{'update': TopicRegistrationform(instance=topic)})
    except Topic.DoesNotExist:
        return HttpResponse("Sorry !! Not Found")

def topic_delete(request,id):
    delete(Topic,id)
    return HttpResponseRedirect('/home/')
   

def register_user(request):
    try:
        registration_form = Registrationform(request.POST if request.method == 'POST' else None)
        if request.method == 'POST':
            if  registration_form.is_valid():     
                    registration_form.save()
                    return HttpResponseRedirect("/user_login/")
        return render(request,'enroll/register_user.html',{'registration_form':registration_form})
    except:
        return HttpResponse('Not founf')

def user_login(request):
    try:
        if request.method=="POST":  
            username = request.POST['username']
            password = request.POST['password']    
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    form=login(request,user)
                    return HttpResponseRedirect("/home/")
                else:
                    return HttpResponse("Your Account is disabled")
            else:
                return HttpResponse("Your account details is Incorrect")
        else:
            form=AuthenticationForm()
        return render(request,'enroll/login.html',{'user_login':form})
    except:
        pass

def user_logout(request):
    try:
        logout(request)
        return HttpResponseRedirect('/user_login/')
    except:
        pass

def change_password(request):
    try:
        if request.method=="POST":
            change_pass=PasswordChangeForm(request.user,request.POST)
            if change_pass.is_valid():
                change_pass.save()
                update_session_auth_hash(request,change_pass.user)
                return HttpResponseRedirect('/home/')    
        else:
            change_pass=PasswordChangeForm(request.user)    
        return render(request,'enroll/changepassword.html',{'change_pass':change_pass})
    except:
        pass

def user(request):
    try:
        users=User.objects.all()
        return render(request,'enroll/show_users.html',{'users':users})
    except:
        pass

def user_update(request,id):
    try:    
        user=User.objects.get(pk=id)
        registration_form=Registrationform(request.POST if request.method == 'POST' else None,instance=user)
        if request.method == 'POST':
            if registration_form.is_valid():
                registration_form.save()
                return HttpResponse("Users Updated Successfully")
        else:
           registration_form=Registrationform()            
        return render(request,'enroll/updateuser.html',{'update': Registrationform(instance=user)})
    except User.DoesNotExist:       
        return HttpResponse("Not Found We Could Not Find This Page")

def user_delete(request,id):
    delete(user,id)
    return HttpResponseRedirect('/users/')
     
def board(request):
    try:
        boardform=BoardRegistrationform(request.POST)
        if request.method =='POST':
            if boardform.is_valid():
                boardform.save()
                return HttpResponseRedirect("/home")
        else:
            boardform=BoardRegistrationform()    
        return render(request,'enroll/boardregister.html',{'boardform':boardform})
    except:
        pass

def board_topics(request,id):    
    if request.user.is_superuser:
        topics=Topic.objects.filter(board_id=id)
    else:
        topics=Topic.objects.filter(Q(board_id=id) & Q(starter_id=request.user.id))    
    return render(request,'enroll/topiclist.html',{'topics':topics})

def topic(request):
    try:
        topicform=TopicRegistrationform(request.POST)
        if request.method=='POST':
            if topicform.is_valid():
                topicform.save()
                return HttpResponse("Topic created sucessfully")
        else:
            topicform=TopicRegistrationform()
        return render(request,'enroll/topicregister.html',{'topicform':topicform})
    except:
        pass