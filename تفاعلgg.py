import os
import time
try:
	import aminofix
except:
	os.system("pip install aminofix")
	import aminofix


title = ""
clinet = aminofix.Client()
print ("_ "*30)
e= input ("\n Email -")
print ("_ "*10)
p = input("\n Password -")
print ("_ "*10)
clinet.login(e,p)
link = input("\nCommunity Link -")
print ("_"*60)

id = clinet.get_from_code(link)
comId = id.comId
sub = aminofix.SubClient(comId,profile=clinet.profile)
try:
	sub.check_in()
except:
	pass
LIS=[]

def get_chat():
    for i in range(0, 300, 100):
        print(f"<{i}>")
        ids = sub.get_online_users(start=i, size=100).profile.userId

        if len(ids) >= 1:
            for id in ids:
                LIS.append({"id": id})
        else:
            i = sub.get_online_users(ids).profile.userId
            LIS.append({"id": ids})

get_chat()
print ("_"*60)

print(" \n Interaction minutes \n")
def tzr():
    localhour=time.strftime("%H", time.gmtime()); localminute=time.strftime("%M", time.gmtime()); 
    UTC={"GMT0":'+0', "GMT1":'+60', "GMT2":'+120', "GMT3":'+180', "GMT4":'+240', "GMT5":'+300', "GMT6":'+360', "GMT7":'+420', "GMT8":'+480', "GMT9":'+540', "GMT10":'+600', "GMT11":'+660', "GMT12":'+720', "GMT13":'+780', "GMT-1":'-60', "GMT-2":'-120', "GMT-3":'-180',"GMT-4":'-240', "GMT-5":'-300', "GMT-6":'-360', "GMT-7":'-420', "GMT-8":'-480', "GMT-9":'-540', "GMT-10":'-600', "GMT-11":'-660'}; hour = [localhour, localminute]
    if hour[0]=="00":tz=UTC["GMT-1"];return int(tz)
    if hour[0]=="01":tz=UTC["GMT-2"];return int(tz)
    if hour[0]=="02":tz=UTC["GMT-3"];return int(tz)
    if hour[0]=="03":tz=UTC["GMT-4"];return int(tz)
    if hour[0]=="04":tz=UTC["GMT-5"];return int(tz)
    if hour[0]=="05":tz=UTC["GMT-6"];return int(tz)
    if hour[0]=="06":tz=UTC["GMT-7"];return int(tz)
    if hour[0]=="07":tz=UTC["GMT-8"];return int(tz)
    if hour[0]=="08":tz=UTC["GMT-9"];return int(tz)
    if hour[0]=="09":tz=UTC["GMT-10"];return int(tz)
    if hour[0]=="10":tz=UTC["GMT13"];return int(tz)       #UTC["GMT-11"]
    if hour[0]=="11":tz=UTC["GMT12"];return int(tz)
    if hour[0]=="12":tz=UTC["GMT11"];return int(tz)
    if hour[0]=="13":tz=UTC["GMT10"];return int(tz)
    if hour[0]=="14":tz=UTC["GMT9"];return int(tz)
    if hour[0]=="15":tz=UTC["GMT8"];return int(tz)
    if hour[0]=="16":tz=UTC["GMT7"];return int(tz)
    if hour[0]=="17":tz=UTC["GMT6"];return int(tz)
    if hour[0]=="18":tz=UTC["GMT5"];return int(tz)
    if hour[0]=="19":tz=UTC["GMT4"];return int(tz)
    if hour[0]=="20":tz=UTC["GMT3"];return int(tz)
    if hour[0]=="21":tz=UTC["GMT2"];return int(tz)
    if hour[0]=="22":tz=UTC["GMT1"];return int(tz)
    if hour[0]=="23":tz=UTC["GMT0"];return int(tz)
    
def trr():
    return [{"start": int(time.time()), "end": int(time.time() + 300)} for _ in range(50)]

for i in range(24):
 sub.send_active_obj(tz=tzr(),timers=trr())
 print(f"{i+1} Done")
 time.sleep(2)


print("\n  post  blog Done \n")


print (" \n comment & like \n")

for us in LIS:
    userId = us["id"]
    nm = sub.get_user_info(userId).nickname
    blog = sub.get_user_blogs(userId,start=0,size=10).blogId
    if blog == []:
        pass
    else:
        print (f"\nuser   --  {nm} \n\n")
        for bId in blog:
            try:
                sub.like_blog(blogId=bId)
            except:
                sub.like_blog(wikiId=bId)
            print("like done")
            try:
                print("comment")
            except:
                print("cant comment Wikipedia")
                pass
            time.sleep(2)

        print("\ndone -------\n\n\n")
        time.sleep(7)


