import socket
import random
import wx
import _thread

#设置基本信息
version = "1.1"
print("All Copyright 2019-2022 XiaoyuStudio")
Client = socket.socket()
host = "jinju.xiaoyustudio.com"
port = 16369
getmin = 0
getmax = 0
q = 0 
Client.connect((host,port))
def canusemember():
    print("canusememberLoaded")
    msg = "Get|||Get"
    Client.send(msg.encode("gbk"))
    getmessage1 = Client.recv(1024).decode('gbk')
    getmessage2 = getmessage1.split('|||')
    print(getmessage1)
    print(getmessage2)
    if getmessage2[0] == "member":
        global getmin
        global getmax
        getmin = int(getmessage2[1])
        getmax = int(getmessage2[2])
        global q
        q = random.randint(getmin,getmax)

def GetGlodOnline(event):
    print("getGlodOnlineLoaded")
    #_thread.start_new_thread(canusemember,())
    global q
    w = q
    q = random.randint(getmin,getmax)
    if q ==0:
        exit()
    while w == q and q != 0:
        q = random.randint(getmin,getmax)
        print(q)
    msg = "GetGlod|||" + str(q)
        
    Client.send(msg.encode('gbk'))
    #print(msg)
    a114514 = Client.recv(1024)
    #print(a114514)
    getmessage1 = a114514.decode('gbk')
    #print(getmessage1)

    getmessage2 = getmessage1.split("|||")
    if getmessage2[0]== "Glod":
        people_text.SetValue(getmessage2[1])
        peoplesays_text.SetValue(getmessage2[2])

def fuckyou(event):
    print("yee")
_thread.start_new_thread(canusemember,())

app = wx.App()
frame = wx.Frame(None,title="每日金句Online V"+version,pos=(1000,200),size=(330,210))#实例化一个窗口
people_text = wx.TextCtrl(frame,pos=(5,5),size=(300,30))
peoplesays_text = wx.TextCtrl(frame,pos=(5,35),size=(300,100),style= wx.TE_MULTILINE)
yes_buttom = wx.Button(frame,label="接受",pos=(5,135),size=(50,30))
no_buttom = wx.Button(frame,label="拒绝",pos=(60,135),size=(50,30))
stop_buttom = wx.Button(frame,label="取消",pos=(115,135),size=(50,30))
yes_buttom.Bind(wx.EVT_BUTTON,GetGlodOnline)
no_buttom.Bind(wx.EVT_BUTTON,GetGlodOnline)
stop_buttom.Bind(wx.EVT_BUTTON,GetGlodOnline)
frame.Show()
app.MainLoop()#启动主循环
print("stop")
