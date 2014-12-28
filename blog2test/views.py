from django.shortcuts import render,render_to_response
from blog2test.models import Author,Book
from django import forms
from django.http import HttpResponse
# Create your views here.

def show_authors(req):
	authors=Author.objects.all()
	return render_to_response('show_authors.html',{'authors':authors})

def show_books(req):
	books=Book.objects.all()
	return render_to_response('show_books.html',{'books':books})

class UserForm(forms.Form):
    name=forms.CharField()
    headimage=forms.FileField()

def register(req):
    if req.method=='POST':
        uf = UserForm(req.POST,req.FILES) #bind form data
        if uf.is_valid():
            print uf.cleaned_data['name']
            print uf.cleaned_data['headimage']
            print uf.cleaned_data['headimage'].name
            print uf.cleaned_data['headimage'].size
            fp=file('/upload/'+uf.cleaned_data['headimage'].name,'wb')
            s=uf.cleaned_data['headimage'].read()
            fp.write(s)
            fp.close()
            return  HttpResponse('ok')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})

