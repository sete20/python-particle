"""tkinter lib"""
import tkinter

windowVar = tkinter.Tk()
windowVar.geometry("1200x600")
windowVar.title('fWindow')
""" label"""
label = tkinter.Label(windowVar,text="Hello window",width=10,height=3).pack( )
"""text"""
text = tkinter.Text(windowVar,width=10,height=3).pack()

tkinter.Radiobutton(windowVar,text="Green",width=10,value=1).pack()
tkinter.Radiobutton(windowVar, text="white", width=10
                     ,value=2).pack()
tkinter.Radiobutton(windowVar, text="black", width=10
                     ,value=3).pack()
"""check button"""
tkinter.Checkbutton(windowVar,text="football",width=10).pack()
tkinter.Checkbutton(windowVar, text="coding", width=10 ).pack()
tkinter.Checkbutton(windowVar, text="travailing", width=10 ).pack()
"""button"""
def myFunction():
      print('hi')
tkinter.Button(windowVar, text="submit", width=10, command=myFunction()).pack()
""" run script window"""
windowVar.mainloop()
