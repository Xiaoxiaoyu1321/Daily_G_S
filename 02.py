import socket
import random
import wx
import _thread
import easygui
import time
import dns.resolver
#设置基本信息
version = "1.3"
print("All Copyright 2019-2022 XiaoyuStudio")
print("This project use GPL3.0 LICENSE OpenSource")
Client = socket.socket()
#host = "jinju.xiaoyustudio.com"
host_domain = 'jinju.xiaoyustudio.com'
port_domain = 'jinju_port.xiaoyustudio.com'
domaintype = 'TXT'
servernumber = 1
host_domain2 = dns.resolver.query(host_domain,domaintype,raise_on_no_answer=False)
port_domain2 = dns.resolver.query(port_domain,domaintype,raise_on_no_answer=False)
host_domain3 = str(host_domain2.rrset)
port_domain3 = str(port_domain2.rrset)
host_domain4 = host_domain3.split('"')
port_domain4 = port_domain3.split('"')
print(host_domain4)
print(port_domain4)
#port = 16369
host = host_domain4[1]
#host = "127.0.0.1"
port = int(port_domain4[1])

CreateDate = "2022.12.29"
getmin = 0
getmax = 0
q = 0 

def Connecttoserver():
    
    Client.connect((host,port))
    time.sleep(1)
    _thread.start_new_thread(canusemember,())
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
def DebugMessage(HaveBug):
    ver = '当前版本/Version:' + version
    server = '服务器/Server：' + host
    serverport = "端口/Port：" +str( port)
    nowbugs = '当前错误/Error：' + HaveBug
    servernum = '服务器序号/Num：' + str(servernumber)
    CDate = '创建日期/CreateDate：' + CreateDate
    print('[Error]当前遇到错误，\n' + ver + '\n' + server + '\n' + serverport + '\n'  + '\n'+servernum +CDate +'\n'+nowbugs)
    easygui.msgbox('[Error]当前遇到错误，\n' + ver + '\n' + server + '\n' + serverport  + '\n'+servernum + '\n' + CDate+'\n' +nowbugs,'[Error]当前遇到错误')
def GetGlodOnline(event):
    print("getGlodOnlineLoaded")
    #_thread.start_new_thread(canusemember,())
    global q
    w = q
    q = random.randint(getmin,getmax)
    if q ==0:
        easygui.msgbox('服务器或网络环境出现问题，请重试',title="Network Error")
        global HaveBugs
        HaveBugs = "[系统错误]无法连接到服务器"
        DebugMessage(HaveBugs)
        
        time.sleep(1)
        _thread.start_new_thread(Connecttoserver,())
    while w == q and q != 0:
        q = random.randint(getmin,getmax)
        print(q)
    msg = "GetGlod|||" + str(q)
        
    Client.send(msg.encode('gbk'))
    #print(msg)
    a114514 = Client.recv(9999)
    #print(a114514)
    getmessage1 = a114514.decode('gbk')
    #print(getmessage1)

    getmessage2 = getmessage1.split("|||")
    if getmessage2[0]== "Glod":
        people_text.SetValue(getmessage2[1])
        peoplesays_text.SetValue(getmessage2[2])

def fuckyou(event):
    print("yee")
_thread.start_new_thread(Connecttoserver,())

#上传窗口
def upload(event):
    uploadapp = wx.App()
    uploadframe = wx.Frame(None,title='投稿金句',pos=(200,200),size=(320,200))
    uploaduser = wx.TextCtrl(uploadframe,pos=(5,5),size=(380,30))
    uploaduser.SetValue('请在这里输入您的昵称')
    uploadpeople = wx.TextCtrl(uploadframe,pos=(5,35),size=(300,30))
    uploadpeople.SetValue('xxx 向你发送金句')
    uploadtext = wx.TextCtrl(uploadframe,pos=(5,65),size=(300,60),style= wx.TE_MULTILINE)
    uploadtext.SetValue('输入金句')
    uploadbutton = wx.Button(uploadframe,label="上传",pos=(5,125),size=(50,30))
    
    de_uploaduser = uploaduser.GetValue()
    de_uploadpeople = uploadpeople.GetValue()
    de_uploadtext = uploadtext.GetValue()

    def Uploading(event):
        if de_uploadtext == uploadtext.GetValue() or de_uploadpeople == uploadpeople.GetValue() or de_uploaduser == uploaduser.GetValue():
            easygui.msgbox('请输入内容')
        elif de_uploadtext != uploadtext.GetValue() and de_uploadpeople != uploadpeople.GetValue() and de_uploaduser != uploaduser.GetValue():
            msg = "uploadtext|||" + uploaduser.GetValue() + '|||' + uploadpeople.GetValue() + '|||' + uploadtext.GetValue()
            Client.send(msg.encode('gbk'))
            qback = Client.recv(9999).decode('gbk')
            if qback == 'Success':
                easygui.msgbox('成功上传')
            elif qback == 'Error':
                DebugMessage('[发生错误]未知错误，但是您的网络连接是正常的')

    uploadbutton.Bind(wx.EVT_BUTTON,Uploading)
    uploadframe.Show()
    uploadapp.MianLoop()



#所有句子窗口
def AllSentence(evnet):
    def GetAll():
        msg = "GetAll|||GetAll"
        Client.send(msg.encode('gbk'))
        q = Client.recv(99999999).decode('gbk')
        AllSentence_Text.SetValue(q)
    
    AllSentenceApp = wx.App()
    AllSentenceFrame = wx.Frame(None,title='所有金句',pos=(200,200),size=(600,400))
    AllSentence_Text =  wx.TextCtrl(AllSentenceFrame,pos=(5,65),style= wx.TE_MULTILINE)
    _thread.start_new_thread(GetAll,())
    AllSentenceFrame.Show()
    AllSentenceApp.MainLoop()



#主窗口
app = wx.App()
frame = wx.Frame(None,title="每日金句Online V"+version,pos=(200,200),size=(330,210))#实例化一个窗口
people_text = wx.TextCtrl(frame,pos=(5,5),size=(300,30))
peoplesays_text = wx.TextCtrl(frame,pos=(5,35),size=(300,100),style= wx.TE_MULTILINE)
yes_buttom = wx.Button(frame,label="接受",pos=(5,135),size=(50,30))
no_buttom = wx.Button(frame,label="拒绝",pos=(55,135),size=(50,30))
stop_buttom = wx.Button(frame,label="取消",pos=(105,135),size=(50,30))
upload_button = wx.Button(frame,label = "投稿",pos=(165,135),size=(50,30))
all_button = wx.Button(frame,label='查看所有金句',pos=(210,135),size=(100,30))
yes_buttom.Bind(wx.EVT_BUTTON,GetGlodOnline)
no_buttom.Bind(wx.EVT_BUTTON,GetGlodOnline)
stop_buttom.Bind(wx.EVT_BUTTON,GetGlodOnline)
upload_button.Bind(wx.EVT_BUTTON,upload)
all_button.Bind(wx.EVT_BUTTON,AllSentence)
frame.Show()
app.MainLoop()#启动主循环
print("stop")
