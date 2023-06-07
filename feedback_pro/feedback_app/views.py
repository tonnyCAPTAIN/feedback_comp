from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Message
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages



def index(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phone')
        message = request.POST.get('message')
        category = request.POST.get('category')
        
        category_id = Category.objects.get(name=category).id
        user_message = Message(email=email, firstname=firstname, lastname=lastname, phonenumber=phonenumber, category_id=category_id, description=message)
        user_message.save()
        messages.success(request, "submitted successfully.")
        return redirect('welcome')
    
    content = {
        'cat': categories
    }
    return render(request, 'index.html', content)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete(request, id):
    del_mes = Message.objects.get(id=id)
    del_mes.delete()
    return redirect('admin_pr')



@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_profile(request):
    messages = Message.objects.all()
    content = {
        'messages': messages
    }
    return render(request, 'admin.html', content)


