'''--------------------------------------------------------------
--------------------- wxFormBuilder를 사용한 계산기 만들기 ---------------
--------------------------------------------------------------'''

import wx
import wx.xrc


class MyCulc ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"간단한 계산기", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"숫자1 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.txtNum1 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtNum1, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( bSizer7 )
        self.m_panel4.Layout()
        bSizer7.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"숫자2 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.txtNum2 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtNum2, 0, wx.ALL, 5 )


        self.m_panel5.SetSizer( bSizer8 )
        self.m_panel5.Layout()
        bSizer8.Fit( self.m_panel5 )
        bSizer5.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox( self.m_panel6, wx.ID_ANY, u"연산자 선택", wx.DefaultPosition, wx.DefaultSize, rdoOpChoices, 1, wx.RA_SPECIFY_ROWS )
        self.rdoOp.SetSelection( 1 )
        bSizer9.Add( self.rdoOp, 1, wx.ALL, 5 )


        self.m_panel6.SetSizer( bSizer9 )
        self.m_panel6.Layout()
        bSizer9.Fit( self.m_panel6 )
        bSizer5.Add( self.m_panel6, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"결과 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer10.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.staResult = wx.StaticText( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )

        bSizer10.Add( self.staResult, 0, wx.ALL, 5 )


        self.m_panel7.SetSizer( bSizer10 )
        self.m_panel7.Layout()
        bSizer10.Fit( self.m_panel7 )
        bSizer5.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnCulc = wx.Button( self.m_panel8, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btnCulc, 0, wx.ALL, 5 )

        self.btnClear = wx.Button( self.m_panel8, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btnClear, 0, wx.ALL, 5 )

        self.btnExit = wx.Button( self.m_panel8, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.btnExit, 0, wx.ALL, 5 )


        self.m_panel8.SetSizer( bSizer11 )
        self.m_panel8.Layout()
        bSizer11.Fit( self.m_panel8 )
        bSizer5.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer5 )
        self.Layout()
        bSizer5.Fit( self  )

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnCulc.id = 1
        self.btnClear.id = 2
        self.btnExit.id = 3
        
        self.btnCulc.Bind( wx.EVT_BUTTON, self.btnClickHandler )
        self.btnClear.Bind( wx.EVT_BUTTON, self.btnClickHandler )
        self.btnExit.Bind( wx.EVT_BUTTON, self.btnClickHandler )


    # Virtual event handlers, overide them in your derived class
    def btnClickHandler( self, event ):
        sel_id = event.GetEventObject().id
#         print(sel_id)

        # 계산 버튼 활성화.
        if sel_id == 1:
            op = self.rdoOp.GetStringSelection()
            num1 = self.txtNum1.GetValue()
            num2 = self.txtNum2.GetValue()
            
            if num1 == '' or num2 == '':
                wx.MessageBox('값을 입력 하시오.', '오류!', wx.OK)
                return
            try :
                mes = eval(num1 + op + num2) # ex) "4" + "3"을 수식화
                                    
            except Exception as e:
                wx.MessageBox('연산오류', str(e) ,'오류!', wx.OK)
                return

#             print(mes)
            self.staResult.SetLabel(str(mes))
        
        # 초기화 버튼 활성화
        elif sel_id == 2:
            self.txtNum1.SetLabel('')
            self.txtNum2.SetLabel('')
            self.staResult.SetLabel('')
            self.rdoOp.SetSelection(0)
            self.txtNum1.SetFocus()
        
        # 종료 버튼 활성화.
        elif sel_id == 3:
            dlg = wx.MessageDialog(self, '정말 종료할까요?', '알림', wx.YES_NO)
            imsi = dlg.ShowModal()
            
            if imsi == wx.ID_YES:
                dlg.Destroy()   #MessageDialog를 닫는다.
                self.Close()    #Frame 닫기
            

if __name__ == '__main__':
    app = wx.App()
    MyCulc(None).Show()
    app.MainLoop()

'''==============================================================='''  