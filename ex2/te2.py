'''--------------------------------------------------------------
------------------ 레이아웃 컨테이너 중 BoxSizer 연습  --------------------
--------------------------------------------------------------'''

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300,250))
        
        panel1 = wx.Panel(self, -1, style = wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style = wx.SUNKEN_BORDER)        

        panel1.SetBackgroundColour("blue")
        panel2.SetBackgroundColour("red")
        
        # 자바의 FlowLayOut과비슷함.
#         box = wx.BoxSizer(wx.VERTICAL)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(panel2, 2, wx.EXPAND)
        
        self.SetSizer(box)
        self.Center()
        self.Show(show=True)
        

if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title='레이아웃 연습연습')
    app.MainLoop()

'''==============================================================='''  