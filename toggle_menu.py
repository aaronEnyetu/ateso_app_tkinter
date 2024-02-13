import tkinter as tk


root = tk.Tk() 
root.geometry('300x500')
root.title('Ateso Prayer App')


options_frame = tk.Frame(root, bg='#c3c3c3')

def indicate(lb):
    lb.config(bg='#9b7653')

def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg='#9b7653')

    aimala_btn = tk.Button(toggle_menu_fm, text='Aimala', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white', command=lambda:indicate(aimala_indicate))
    aimala_btn.place(x=20, y=20)
    aimala_indicate = tk.Label(options_frame, text='', bg='#9b7653')
    aimala_indicate.place(x=3, y=20, width=5, height=20)



    alungakin_btn = tk.Button(toggle_menu_fm, text='Alungakin', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    alungakin_btn.place(x=20, y=50)

    aimorikikina_btn = tk.Button(toggle_menu_fm, text='Aimorikikina', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    aimorikikina_btn.place(x=20, y=80)

    aingarenikino_btn = tk.Button(toggle_menu_fm, text='Aingarenikino', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    aingarenikino_btn.place(x=20, y=110)

    aitingaleuno_btn = tk.Button(toggle_menu_fm, text='Aitingaleuno', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    aitingaleuno_btn.place(x=20, y=140)

    aisigalikino_btn = tk.Button(toggle_menu_fm, text='Aisigalikino', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    aisigalikino_btn.place(x=20, y=170)

    aidaro_btn = tk.Button(toggle_menu_fm, text='Aidaro', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    aidaro_btn.place(x=20, y=200)

    aitimio_btn = tk.Button(toggle_menu_fm, text='Aitimio', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    aitimio_btn.place(x=20, y=230)

    idue_btn = tk.Button(toggle_menu_fm, text='Idue', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    idue_btn.place(x=20, y=260)

    alosit_btn = tk.Button(toggle_menu_fm, text='Alosit', font=('Bold', 14), bd=0, bg='#9b7653', fg='white', activebackground='#9b7653', activeforeground='white')
    alosit_btn.place(x=20, y=290)










    window_height = root.winfo_height()
    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)







head_frame = tk.Frame(root, bg='#9b7653', highlightbackground='#867e36', highlightthickness=1)


toggle_btn = tk.Button(head_frame, text= '☰', bg='#c3b091', 
                        fg='#faf0e6', font=('Bold, 20'), 
                        bd=0, activebackground='#c3b091', 
                        activeforeground='white',
                        command=toggle_menu)



toggle_btn.pack(side=tk.LEFT)

title_lb = tk.Label(head_frame, text='Ailip Naka Bahai', bg='#9b7653', fg='white', font=('Bold', 20))
title_lb.pack(side=tk.LEFT)


head_frame.pack(side=tk.TOP, fill=tk.X)

head_frame.pack_propagate(False)
head_frame.configure(height=50)



root.mainloop()