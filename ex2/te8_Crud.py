'''--------------------------------------------------------------
------------------- mariaDB+GUI를 사용한 CURD -----------------------
--------------------------------------------------------------'''

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


class MyMember ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"회원관리", pos = wx.DefaultPosition, size = wx.Size( 363,418 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.txtBunho = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtBunho, 0, wx.ALL, 5 )

        self.btnInsert = wx.Button( self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        bSizer2.Add( self.btnInsert, 0, wx.ALL, 5 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.txtName = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtName, 0, wx.ALL, 5 )

        self.btnUpdate = wx.Button( self.m_panel2, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnUpdate, 0, wx.ALL, 5 )

        self.btnConfirm = wx.Button( self.m_panel2, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnConfirm, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"전화 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.txtTel = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtTel, 0, wx.ALL, 5 )

        self.btnDel = wx.Button( self.m_panel3, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
        bSizer4.Add( self.btnDel, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.lstMem = wx.ListCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer5.Add( self.lstMem, 0, wx.ALL|wx.EXPAND, 5 )


        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer6.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.staCnt = wx.StaticText( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCnt.Wrap( -1 )

        bSizer6.Add( self.staCnt, 0, wx.ALL, 5 )


        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )
        
        # lstMem에 제목 표시
        self.lstMem.InsertColumn(0, '번호', width= 70)
        self.lstMem.InsertColumn(1, '이름', width= 105)
        self.lstMem.InsertColumn(2, '전화', width= 105)
        
        self.btnConfirm.Enable(enable=False) # 수정 / 확인 버튼은 비활성화
        
        # Connect Events
        self.btnInsert.id = 1; self.btnUpdate.id = 2;
        self.btnConfirm.id = 3; self.btnDel.id = 4;
        
        self.btnInsert.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        self.btnDel.Bind( wx.EVT_BUTTON, self.OnBtnClick )
        
        # ViewData 부르기
        self.ViewData()
        
    def __del__( self ):
        pass

    # VIEW
    
    def ViewData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "select * from pymem"
            cursor.execute(sql)
            
            self.lstMem.DeleteAllItems() # 초기화
            count = 0 #건수
            
            # 행,열에 넣어주어야 한다.
            for data in cursor:
                i = self.lstMem.InsertItem(10000, 0) # 동적인 행을 만들어줌.(동적인 행번호 얻기, 현재 최대 행 = 10000)
                self.lstMem.SetItem(i, 0, str(data[0]))
                self.lstMem.SetItem(i, 1, data[1])
                self.lstMem.SetItem(i, 2, data[2])
                count += 1 
                
            self.staCnt.SetLabel(str(count) + '명') #인원수
                
            
        except Exception as e:
            wx.MessageBox('읽기오류: ',e)
        
        finally:
            cursor.close()
            conn.close()


    # event handlers
    def OnBtnClick( self, event ):
        id = event.GetEventObject().id
#         print(id)
        if id == 1:
            self.MemInsert()
        elif id == 2:
            self.MemUpdate() # 수정 준비
        elif id == 3: 
            self.MemUpdateOk() # 수정 준비
        elif id == 4:
            self.MemDelete()
        elif id == 5:
            self.MemUpdateCancel() # 수정 취소
        
           
    ## Event Handler 활성화
    # 등록 버튼 활성화
    def MemInsert( self ):
        no = self.txtBunho.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel =='':
            wx.MessageBox('자료를 입력하시오.', '입력', wx.OK)
            return
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            data = self.SelectData(no)
#             print(data)
            
            if data != None:
                wx.MessageBox('이미 사용중인 번호입니다.', '알림', wx.OK)
                self.txtBunho.SetFocus()
                return 
            
            #추가 작업 계속
            sql = "insert into pymem values(%s,%s,%s)"
            cursor.execute(sql, (no, name, tel))
            conn.commit()
            
            #등록후 목록보기
            self.ViewData()
            self.txtBunho.SetLabel("")
            self.txtName.SetLabel("")
            self.txtTel.SetLabel("")
            
        except Exception as e:
            wx.MessageBox('입력 에러: ' + str(e), '알림', wx.OK)
            conn.rollback()
        
        finally:
            cursor.close()
            conn.close()

    # 수정 버튼 활성화
    def MemUpdate( self ):
        ## 모달창으로 만들기
        dlg = wx.TextEntryDialog(None, '수정할 번호 입력', '수정')
        
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
        
            upno = dlg.GetValue() ##모달창으로 부터 값을 받아옴.
#             print(upno)    
            data = self.SelectData(upno)
            
            if data == None:
                wx.MessageBox(upno + '번은 등록된 자료가 아닙니다', '알림', wx.OK)
                return
            
            '''
                        수정 작업) 여기서 MODAL창에 입력된 값이 존재하면 데이터를 UI로 띄어줌.
            '''
            #수정 작업 계속
            self.txtBunho.SetValue(str(data[0]))
            self.txtName.SetValue(data[1])
            self.txtTel.SetValue(data[2])
            
            '''
                        수정 작업) 번호는 수정에서 제외 시켜준다.(read only가 됨.)
                        
            '''
            self.txtBunho.SetEditable(False) # 번호는 수정에서 제외
            self.btnConfirm.Enable(enable = True)   # 비활성화된 확인 버튼을 활성화 시킴.
            
            '''
                        수정 작업)     1) SetLable을 이용해서 수정 -> 취소로 이름을 바꿔줬음.
                        2) 작업중에 동적으로 id값을 5번으로 바꿈. 떄문에 SelectData()로 넘어가게 됨.
            '''
            self.btnUpdate.SetLabel('취소') 
            self.btnUpdate.id = 5   # 여기서 ID로 동적으로 움직이면서 id값이 5인 SelectData()로 넘어간다.
            
        else :
            return
        
        dlg.Destroy()
            
    def MemUpdateOk( self ):
        '''
                수정 확인)     1) 수정 확인 버튼을 누르면 이곳으로 넘어옴.
                    2) 수정 후 작업까지 확인해 주는게 포인트.(self.ViewData(), self.MemUpdateCancel())
                    3) 
        '''
    
        no = self.txtBunho.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if name == '' or tel =='':
            wx.MessageBox('수정 자료를 입력하시오.', '입력', wx.OK)
            return
        
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
        
            sql = "update pymem set irum=%s, junhwa=%s where bun=%s"
            cursor.execute(sql, (name, tel, no))
            conn.commit()
            
            self.ViewData() # 수정 후 마무리 작업 ( 수정 후 목록 보기)
            self.MemUpdateCancel() # 수정 후  input 부분은 원래대로 돌려 놓기
            
        except Exception as e:
            wx.MessageBox('수정 에러: ' + str(e), '알림', wx.OK)
            conn.rollback()
        
        finally:
            cursor.close()
            conn.close()
        
    def MemDelete( self ):
        ## memUpdate에서 if data == None: 까지 복붙함.
        dlg = wx.TextEntryDialog(None, '삭제할 번호 입력', '수정')
        
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
        
            delno = dlg.GetValue() ##모달창으로 부터 값을 받아옴.
#             print(upno)    
            data = self.SelectData(delno)
            
            if data == None:
                wx.MessageBox(delno + '번은 등록된 자료가 아닙니다', '알림', wx.OK)
                return
    
        ## 위에 까지 문제가 없다면 삭제 작업 진행. (여기는 memUpdateOK에서 복붙함)
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
        
            sql = "delete from pymem where bun=%s"
            cursor.execute(sql, (delno))
            conn.commit()
            
            self.ViewData() # 삭제 후 마무리 작업 ( 삭제 후 목록 보기)
            
        except Exception as e:
            wx.MessageBox('수정 에러: ' + str(e), '알림', wx.OK)
            conn.rollback()
        
        finally:
            cursor.close()
            conn.close()
        
        
    def MemUpdateCancel( self ):
        '''
                수정 취소)     1) SetLable을 이용해서 취소 -> 수정으로 이름을 바꿔줬음.
                    2) 작업중에 동적으로 id값을 2번으로 바꿈. 떄문에  다시 원래대로 넘어가게 됨.
        '''
        self.btnUpdate.id = 2
        self.btnUpdate.SetLabel('수정')
        self.btnConfirm.Enable(False)
        
        self.txtBunho.SetEditable(True)
        
        self.txtBunho.SetValue('')
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
    
    
    # 일반메소드 (해당 번호의 자료 읽기 : 등록, 수정 삭제 시 사용)
    def SelectData(self, no):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "select * from pymem where bun={0}".format(no)
            cursor.execute(sql)
            
            data = cursor.fetchone()
            return data
            
        except Exception as e:
            wx.MessageBox('입력 에러: ' + str(e), '알림', wx.OK)
            conn.rollback()
        
        finally:
            cursor.close()
            conn.close()
    
    
if __name__ == '__main__':
    app = wx.App()
    MyMember(None).Show()
    app.MainLoop()

