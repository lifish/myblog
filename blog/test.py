from models import userData,content

yearList = []
monthList = []
contentList = []
yearDoc = {}
monthDoc = {}

user = userData.objects.get(id=1)
conentList = user.content_set.all()

for y in range(2012, 2010, -1):
	monthDoc = {}
	for m in range(1,12,1):
		con = contentyList.filter(created__year ='%s'%y, created__month='%s'%m)
		monthDoc[m] = con
	
	yearDoc[y] = monthDoc

yearList = yearDoc

yearList
