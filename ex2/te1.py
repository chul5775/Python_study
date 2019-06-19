'''--------------------------------------------------------------
--------------------- GUI : wxPython 모듈을 사용.--------------------
--------------------------------------------------------------'''
import wx



'''------------------- 1. wxPython 중앙에 배치 시키기------------------
<개요>
    1. wxPython은 thinker와 같이 파이썬에서 GUI가 뜨게 도움을 주는 API이다.

<사용법>
    1. GUI 중앙에 뜨게 만들기 = Center() or Centre()
    
    2. 글을 쓸 수 있는  TextArea 만들기 = wx.TextCtrl()
    
    3. 왼쪽 위에 Menu만들기 = wx.MenuBar
    
    4. GUI에서 File을 열 수 있는 Menu 만들기 = wx.Menu
    
    5. JAVA와 같이 GUI위의 원하는 박스 붙이기 = wx.Panel
    
        - wx.StaticText로 TEXT 입력이 가능한 PANEL을 원하는 모양으로 만들어 낼 수 있다.
    
    6. Event는 Bind 처리와 함수처리를 해주어야 사용 가능  = EVT_BUTTON or EVT_BUTTON
                                            = def ~~~~~~~ 
    
    7. 경고창 처럼 사용할 수 있는 Dialog = wx.MessageDialLog()
    
    * 참고1) 여기서 -1은 wx에게 너가 알아서 판단해 달라고 말하는거다.
    * 참고2) OnClick Event의 경우 , 그냥 이렇게 쓰면 일반 메소드여서 Err가 뜸.
      
           def onClick1(self):
           self.txtA.SetLabelText('버튼1')
--------------------------------------------------------------'''

class Ex(wx.Frame):
    
    def __init__(self, parent,title):
        super(Ex, self).__init__(parent, title=title, size=(300,300))
        
#       text Box
#         self.txtA = wx.TextCtrl(self)
#         self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        
        self.CreateStatusBar()
        
        #메뉴 
        menuBar = wx.MenuBar()
        
        mnuFile = wx.Menu()
        mnuNew = mnuFile.Append(wx.ID_NEW, 'New', '새글')
        mnuOpen = mnuFile.Append(wx.ID_OPEN, 'Open', '열기')
        
        mnuFile.AppendSeparator() # 구분선
        
        mnuExit = mnuFile.Append(wx.ID_EXIT, 'Exit', '종료')
        
        menuBar.Append(mnuFile, 'File')
        self.SetMenuBar(menuBar)
        
        # 라벨과 텍스트 박스
        panel = wx.Panel(self)
        
        wx.StaticText(panel, label='I D: ', pos = (5,5))
        wx.StaticText(panel, label='PWD: ', pos = (5,40))
        
        self.txtA = wx.TextCtrl(panel, pos = (40, 5))
        self.txtB = wx.TextCtrl(panel, pos = (40, 40), size =(150,-1)) #참고 1
        
        #버튼
        
        btn1 = wx.Button(panel, label='일반버튼', pos=(5, 100))
        btn2 = wx.ToggleButton(panel, label='토글버튼', pos=(100, 100))
        btn3 = wx.Button(panel, label='종 료', pos=(200, 100), size = (50, -1))
        
#       #이벤트 처리 (1-1, 이벤트가 각각의 함수를 찾아서 반응하는 방식)
#         btn1.Bind(wx.EVT_BUTTON, self.OnClick1)
#         btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClick2)
#         btn3.Bind(wx.EVT_BUTTON, self.OnClick3)
        
            
        # 이벤트처리 (2-1)
        self.Bind(wx.EVT_MENU, self.OnEvent1, mnuNew)
        
        # 이벤트 처리 (3-1, 이벤트 핸들러가 같은 방식(버튼값으로 구분))
        btn1.id = 1
        btn2.id = 2
        btn3.id = 3        
        
        btn1.Bind(wx.EVT_BUTTON, self.OnBtnHandler)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnBtnHandler)
        btn3.Bind(wx.EVT_BUTTON, self.OnBtnHandler)
        
        
        # GUI 출력
#       self.Center()
        self.Centre()
        self.Show()
    
    # 이벤트 처리(1-2)
    
    def OnClick1(self, event):  #이벤트 핸들러 메소드, 참고2
        self.txtA.SetLabelText('버튼1')
    # 대화상자 호출
        msgDial = wx.MessageDialog(self, '메세지', '제목', wx.OK)
        msgDial.ShowModal()
        msgDial.Destroy()
    
    def OnClick2(self, event):  #이벤트 핸들러 메소드, 참고2
#         print('aa')
#         print(event.GetEventObject().GetValue())
        if event.GetEventObject().GetValue():
            self.txtA.SetLabelText('kbs')
            self.txtB.SetLabelText('9')
        else:
            self.txtA.SetLabelText('sbs')
            self.txtB.SetLabelText('5')
    
    def OnClick3(self, event):
        self.Close()
    
    
    # 이벤트 처리 (2-2)
    def OnEvent1(self, evnet):
        pass


    # 이벤트처리 (3-2)
    def OnBtnHandler(self, event):
#         print('a')
        print(event.GetEventObject().id)
 
        if event.GetEventObject().id == 1:
            self.txtA.SetLabelText('One')
            
        elif event.GetEventObject().id == 2:
            self.txtA.SetLabelText('Two')
        else:
            self.Close()


if __name__ == '__main__':
    app = wx.App()
    Ex(None, title='GUI연습')
    app.MainLoop()
    
'''==============================================================='''  
    
    
    
    
    
    
    
    
    
    
