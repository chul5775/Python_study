import wx
import wx.xrc
import MySQLdb


config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class MyFrame1 ( wx.Frame ):
    

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"상품 등록/검색", pos = wx.DefaultPosition, size = wx.Size( 650,320 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"상품명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer4.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )

        self.txtSang = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer4.Add( self.txtSang, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"수량 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer4.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )

        self.txtSu = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtSu, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"단가 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer4.Add( self.m_staticText3, 1, wx.ALL|wx.EXPAND, 5 )

        self.txtDan = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtDan, 0, wx.ALL, 5 )

        self.btnOK = wx.Button( self.m_panel3, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btnOK, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer3.Add( self.m_panel3, 0, wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"상품별 검색 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.txtSearch = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.txtSearch, 0, wx.ALL, 5 )

        self.btnSearch = wx.Button( self.m_panel4, wx.ID_ANY, u"검색", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.btnSearch, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer3.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"코드", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer6.Add( self.m_staticText7, 1, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"상품", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer6.Add( self.m_staticText8, 1, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"수량", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer6.Add( self.m_staticText9, 1, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"단가", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        bSizer6.Add( self.m_staticText10, 1, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer6.Add( self.m_staticText11, 1, wx.ALL, 5 )


        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer3.Add( self.m_panel5, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.code = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.code.Wrap( -1 )

        bSizer12.Add( self.code, 1, wx.ALL|wx.EXPAND, 5 )

        self.sang1 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sang1.Wrap( -1 )

        bSizer12.Add( self.sang1, 1, wx.ALL|wx.EXPAND, 5 )

        self.su1 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.su1.Wrap( -1 )

        bSizer12.Add( self.su1, 1, wx.ALL|wx.EXPAND, 5 )

        self.dan1 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.dan1.Wrap( -1 )

        bSizer12.Add( self.dan1, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText22 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer12.Add( self.m_staticText22, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText27 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"건수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        bSizer13.Add( self.m_staticText27, 0, wx.ALL, 5 )

        self.staCount = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )

        bSizer13.Add( self.staCount, 0, wx.ALL, 5 )


        bSizer11.Add( bSizer13, 0, wx.EXPAND, 5 )


        self.m_panel6.SetSizer( bSizer11 )
        self.m_panel6.Layout()
        bSizer11.Fit( self.m_panel6 )
        bSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnOK.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.btnSearch.Bind( wx.EVT_BUTTON, self.OnSearch )


    # Virtual event handlers, overide them in your derived class
    def OnInsert(self, event):
        #등록 버튼 활성화
        inputSang = self.txtSang.GetValue()
        inputSu = self.txtSu.GetValue()
        inputDan = self.txtDan.GetValue()

        if inputSang == "" or inputSu == "" or inputDan == "":
            wx.MessageBox("입력을 확인해 주세요!", "알림", wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            #Code 구하기
            sql = "select count(*) from sangdata"
            cursor.execute(sql)
            maxCode = str(cursor.fetchone()[0] + 1)
            
            #insert
            sql = "insert into sangdata values(%s,%s,%s,%s)"
            sql_data = ([int(maxCode), inputSang, int(inputSu), int(inputDan)])
            cursor.execute(sql, sql_data)
        
            conn.commit()
            
            wx.MessageBox("등록이 완료 되었습니다!", "알림", wx.OK)
            
            self.txtSang.SetLabel('')
            self.txtSu.SetLabel('')
            self.txtDan.SetLabel('')
            self.txtSang.SetFocus()
            
            
            
        except Exception as e :
            print('err: ', str(e))
            wx.MessageBox("등록에 실패 하였습니다!", "알림", wx.OK)
            conn.rollback()
    
        finally:
            cursor.close()
            conn.close()    
        
        
            
    def OnSearch( self, event ):
        search = self.txtSearch.GetValue()
      
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            if search == "":
                wx.MessageBox("검색어를 입력해 주세요!", "알림", wx.OK)
                
            else:
                sql = "select code, sang, su, dan from sangdata where sang like '%s'".format(search)
                cursor.execute(sql)
                print(cursor.execute(sql))

                for(a,b,c,d) in cursor:
                    print(a,b,c,d)
                
                
                conn.commit()
                
                cursor.execute("select count(*) from sangdata")
                print("건수: " + str(cursor.fetchone()[0]))

        except Exception as e:
            print('err :' + str(e))
            conn.rollback()
        
        finally:
            conn.close()
            
if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()