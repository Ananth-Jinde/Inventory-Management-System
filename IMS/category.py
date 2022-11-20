from tkinter import*
from tkinter import scrolledtext
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1063x480+200+126")
        self.root.title("Inventory Managemeny System | Developed by Jinde Anantha Sai")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("IMS_ICON.ico")
        self.root.focus_force()


        ####Varibles####
        self.var_cat_id=StringVar()
        self.var_name=StringVar()


#=============title==================

        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=60,y=170,width=300)
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=380,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=550,y=170,width=150,height=30)

#==============category details==========================

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=710,y=100,width=320,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrolly=Scrollbar(cat_frame,orient=HORIZONTAL)
        


        self.categoryTable=ttk.Treeview(cat_frame,columns=("CId","name"))
        #scrollx.pack(side=BOTTOM,fill=X)
        #scrolly.pack(side=RIGHT,fill=Y)
        #scrollx.config(command=self.categoryTable.xview)
        #scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("CId",text="Customer ID")
        self.categoryTable.heading("name",text="Name")
        self.categoryTable["show"]="headings"
        self.categoryTable.column("CId",width=80)
        self.categoryTable.column("name",width=80)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)


        #=======images=====
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((479,230),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)


        self.lb1_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lb1_im1.place(x=60,y=220)
        


        self.im2=Image.open("images/category.jpg")
        self.im2=self.im2.resize((479,230),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)


        self.lb1_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lb1_im2.place(x=550,y=220)
        self.show()

    #=========functions=================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category namee should be Required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already present, try different",parent=self.root)
                else:
                    cur.execute("Insert into category(name) values(?)",(
                                            self.var_name.get(),
                                    
                                           
                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    


    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error", "Please select category from the list",parent=self.root)
            else:
                cur.execute("Select * from category where CId=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where CId=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")


        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()