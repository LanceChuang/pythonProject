from django.shortcuts import render
from .models import Post
# Create your views here.
# from django.http import HttpResponse

# def hello_world(request):
# 	return HttpResponse("Hello world!")
from datetime import datetime
from django.shortcuts import render
# 我們改成用 render 這個 function 產生要回傳的 HttpResponse 物件
def hello_world(request):
	return render(request, 'hello_world.html', {
		'current_time': str(datetime.now()),
		})

def home(request):
	post_list = Post.objects.all()
	return render(request,'home.html',{
		'post_list' : post_list,
		})

def post_detail(request,pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post': post})