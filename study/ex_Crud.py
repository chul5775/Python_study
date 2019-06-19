'''
te8_Crud에서 사용된 부분들. (하나의 핸들러를 통해 DB자료를 등록/수정/삭제 하기)
'''

'''==============================================================='''  
''' 1) __init__ 부분'''
'''==============================================================='''  

''' <------- 1-1) lstMem에 제목 표시 ------->'''
self.lstMem.InsertColumn(0, '번호', width= 70)
self.lstMem.InsertColumn(1, '이름', width= 105)
self.lstMem.InsertColumn(2, '전화', width= 105)

self.btnConfirm.Enable(enable=False) # 수정 / 확인 버튼은 비활성화

''' <------- 1-2) Evnet에서 각 아이디 마다 번호 부여하기  ------->'''
self.btnInsert.id = 1; self.btnUpdate.id = 2;
self.btnConfirm.id = 3; self.btnDel.id = 4;

''' <------- 1-3) # ViewData 부르기  ------->'''
self.ViewData()



'''==============================================================='''  
''' 2) wxFormBuilder에서 만들어진 함수 말고 따로 만들어준 함수.'''
'''==============================================================='''  

''' <------- 2-1) ViewData ------->'''
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

''' <------- 2-2) 수정 취소 버튼  ------->'''
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
    

''' <------- 2-3) Select Data ------->'''
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
            
'''==============================================================='''                
''' 3) wxFormBuilder에서 만들어진 함수 활성화'''
'''==============================================================='''  
            
''' <------- 3-1) event Handler ------->'''                    
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
        
''' <------- 3-2) 등록 버튼  ------->'''                   
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

''' <------- 3-3) 수정 버튼 ------->'''        
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
        
''' <------- 3-4) 확인 버튼  ------->'''               
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
            
            
'''==============================================================='''             
            
            
            