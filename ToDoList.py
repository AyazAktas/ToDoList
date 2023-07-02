from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
import os

root=Tk()
root.title("Ayaz'ın To Do List Programı")
root.geometry("500x500")

icon_path=os.path.abspath("to-do-list-apps.ico")
root.iconbitmap(icon_path)

my_Font=Font(family="Lucida Consale", size=30,weight="normal")

my_frame=Frame(root)
#list box
my_frame.pack(pady=10)
my_list=Listbox(my_frame,font=my_Font,width=25,height=5,bg="SystemButtonFace",bd=0,highlightthickness=0,selectbackground="#a6a6a6",activestyle="none")

my_list.pack(side=LEFT,fill=BOTH)
my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#item eklemek için
my_entry=Entry(root,font=("Lucida Console",24),width=26)
my_entry.pack(pady=20)
#buton oluşturmak için
button_frame=Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)

def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    #bardan kurtul
    my_list.select_clear(0,END)

def uncross_item():
    my_list.itemconfig(
    my_list.curselection(),
    fg="#464646")
    #bardan kurtul
    my_list.select_clear(0,END)

def delete_crossed_item():
    #işaretlenmişleri nasıl bulacağız?
    count=0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")== "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count+=1

def save_list():
    file_name = filedialog.asksaveasfilename(initialdir='C:/Users/Poyraz/Desktop/ToDoLists',  title='Save File',filetypes=(('Dat Files', '*.dat'), ('All Files', '*.*')))
    if file_name:
        delete_crossed_item()
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'

        tasks = my_list.get(0, END)
        output_file = open(file_name, 'wb')
        pickle.dump(tasks, output_file)

def open_list():
    file_name=filedialog.askopenfilename(initialdir="C:/gui/listem",title="Save File",filetypes=(("Dat Files","*.dat"),("All Files","*.*")))
    if file_name:
        my_list.delete(0,END)
        input_file=open(file_name,'rb')

        #load the data from the file
        stuff=pickle.load(input_file)
        for item in stuff:
            my_list.insert(END,item)
def clear_list():
    my_list.delete(0,END) 


my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Listeyi Kaydet",command=save_list)
file_menu.add_command(label="Liste Aç",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Listeyi temizle",command=clear_list)

delete_button=Button(button_frame,text="Görev Sil",command=delete_item)
add_button=Button(button_frame,text="Görev Ekle",command=add_item)
cross_off_button=Button(button_frame,text="Tamamlandı",command=cross_off_item)
uncross_button=Button(button_frame,text="Tamamlanamadı",command=uncross_item)
delete_crossed_button=Button(button_frame,text="Tamamlanmışları Sil",command=delete_crossed_item)
delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
cross_off_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3,padx=20)
delete_crossed_button.grid(row=0,column=4)
root.mainloop()
def on_entry_keypress(event):
    if event.keycode == 13:
        add_item()

my_entry.bind("<KeyRelease>", on_entry_keypress)
