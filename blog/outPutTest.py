from bolg.modles import contetn, userData

yearList = []
monthList= []
yearDic = {}
monthDic={}
user = userData.objects.get(id=1)
con = user.content_set.all()

for content in con:
	
