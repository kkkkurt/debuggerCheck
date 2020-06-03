# !/user/bin/env Python3
# -*- coding:utf-8 -*-
  
"""
file：window.py.py
author:kkkurt
desc: 窗口
"""
import tkinter as tk
from tkinter import filedialog, dialog,messagebox
import os

window = tk.Tk()
window.title('窗口标题') # 标题
window.geometry('500x500') # 窗口尺寸
  
file_path = ''
  
file_text = ''

text1 = tk.Text(window, width=50, height=10, bg='orange', font=('Arial', 12))
text1.pack()

files = list();
def DirAll(pathName):
 if os.path.exists(pathName):
  fileList = os.listdir(pathName);
  for f in fileList:
   if f=="$RECYCLE.BIN" or f=="System Volume Information":
    continue;
   f=os.path.join(pathName,f);
   if os.path.isdir(f):
    DirAll(f);
   else:
    dirName=os.path.dirname(f);
    baseName=os.path.basename(f);
    if dirName.endswith(os.sep):
     files.append(dirName+baseName);
    else:
      str = baseName.split(".");
      if str[1]=="jsp" or str[1]=="js":
        files.append(dirName + os.sep + baseName);

  
def open_file():
  '''
  打开文件
  :return:
  '''
  global file_path
  global file_text
  file_path=tk.filedialog.askdirectory()
  print(file_path)
  if file_path == None:
    print("未选择文件夹")
  else:
    DirAll(file_path);
    '''消除debugger 和 console.log'''
    for f in files:
      debuggercount = 0;
      concount = 0;
      file_data = ""
      with open(f, 'r', encoding='utf-8') as file:
        for line in file:

          if "debugger" in line:
            print(line);
            debuggercount=debuggercount+1;
            line = line.replace(line,"");

          if "console.log" in line:
            concount=concount+1;
            print(line);
            line = line.replace(line, "");
          file_data += line
      if debuggercount >0 or concount>0:
        text = f+"此文件有"+str(debuggercount)+"个 debugger 和"+str(concount)+ "个 console.log";
        print(text);
        if tk.messagebox.askyesno("是否修改",text+" 是否修改？"):

          with open(f, "w", encoding="utf-8") as f:
            f.write(file_data);




def save_file():
  global file_path
  global file_text
  file_path = filedialog.asksaveasfilename(title=u'保存文件')
  print('保存文件：', file_path)
  file_text = text1.get('1.0', tk.END)
  if file_path is not None:
    with open(file=file_path, mode='a+', encoding='utf-8') as file:
      file.write(file_text)
    text1.delete('1.0', tk.END)
    dialog.Dialog(None, {'title': 'File Modified', 'text': '保存完成', 'bitmap': 'warning', 'default': 0,
               'strings': ('OK', 'Cancle')})
    print('保存完成')
  
  
bt1 = tk.Button(window, text='打开文件', width=15, height=2, command=open_file)
bt1.pack()
bt2 = tk.Button(window, text='保存文件', width=15, height=2, command=save_file)
bt2.pack()
  
window.mainloop() # 显示