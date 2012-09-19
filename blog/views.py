# Create your views here.
from django.shortcuts import render_to_response , get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from django.template import RequestContext
from blog.models import userData, content

def login(request):
	print('in login')
	return render_to_response('blog/login.html','', context_instance=RequestContext(request))

def check(request):
	c = {}
	name=request.POST['name']
	p = userData.objects.filter(name = request.POST['name'], password = request.POST['password'])
	#p = get_object_or_404(userData, request.POST['name'])
	if p:
		print('%s'%p[0].name)
		selected = p[0].content_set.all()
		return HttpResponseRedirect('/%s'%p[0].id)
	else:
		return HttpResponseRedirect('/login/')
				
def main(request,user_id,content_id =1):
	yearList = []
	monthList = []
	contentList = []
	yearDoc = {}
	monthdoc = {}
	p = userData.objects.get(id = user_id)
	contentList = p.content_set.all()
	for y in range(2012,2009,-1):
		monthDoc = {}
		monthList = []
		for m in range(1,12,1):
			con = contentList.filter(created__year ='%s'%y, created__month = '%s'%m)
			if con:
				monthDoc['month'] = '%s'%m
				monthDoc['content'] = con
				monthList.append(monthDoc)
		if monthList:
			yearDoc['year'] = '%s'%y
			yearDoc['content'] = monthList
			yearList.append(yearDoc)
	print(yearList)
	print('in main')
	print(content_id)
	#name=request.POST['name']
	#p = userData.objects.filter(name = request.POST['name'], password = request.POST['password'])
	#p = get_object_or_404(userData, request.POST['name'])
	content_list = p.content_set.all()
	content = p.content_set.get(id=content_id)
	print(content.content)
	return render_to_response('blog/main.html',{'userdata' : p, 'years':yearList,'content_right': content})
	
def new(request,user_id):
	if(request.POST):
		user = userData.objects.get(id=user_id)
		print(user.name)
		print('in new\'s post')
		if request.POST['title']:
			print('post data')
			user.content_set.create(title= request.POST['title'],content=request.POST['content'])
		return HttpResponseRedirect('/%s/'%user_id)
	return render_to_response('blog/new.html',{'user_id': user_id}, context_instance=RequestContext(request))
