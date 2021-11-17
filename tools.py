import webbrowser
import tkinter as tk
from art import tprint
import os
import datetime as dt
from googletrans import Translator

live = dt.datetime.now()
tprint("Patok tools")
while True:
    opsi = input(">: ")
    if opsi=="help":
        print("""
-show
-run -h
-run
-clear
-exit
        """)
    elif opsi=="clear":
        os.system("clear")
    elif opsi=="show":
        print("Tools ini untuk menjalankan seperti google translate dan searching youtube, jangan lupa tools nya di share!")
    elif opsi=="run -h":
        print("Menjalankan [google translate] ketik [run -t] / jika ingin lebih ketik [run -t -h], \n untuk menjalankan [searching youtube] ketik [run -y] / jika ingin lebik ketik [run -y -h]")
    elif opsi=="run -t":
        os.system("clear")
        tprint("Google translate")
        while True:
            kata = input("Masukkan kata: ")
            a = Translator()
            b = a.translate(kata)
            print(b.text)
    elif opsi=="run -t -h":
        print("Jika ingin menjalankan google translate tanpa gui ketik saja [run -t], jika ingin menggunakan gui ketik [run -t -g]")
    elif opsi=="run":
        print("Mau apa nich yang di run [run -h] <= agar lebih jelas!")
    elif opsi=="run -t -g":
        root = tk.Tk()
        root.title(live)
        root.geometry("500x500")
        label = tk.Label(root,text="Google translate")
        label.pack()
        kata2 = tk.Entry(root)
        kata2.pack()
        def hasil_translate():
            c = Translator()
            d = c.translate(kata2.get())
            label2 = tk.Label(root,text=d)
            label2.pack()
        btn = tk.Button(root,text="Submit",command=hasil_translate)
        btn.pack()
        root.mainloop()
    elif opsi=="exit":
        exit()
    elif opsi=="run -y -h":
        print("Jika ingin menjalankan searching youtube tanpa gui ketik saja [run -y], jika ingin menggunakan gui ketik [run -y- g]")
    elif opsi=="run -y":
        os.system("clear")
        tprint("Youtube")
        search2 = input("Search: ")
        webbrowser.open_new(f"https://www.youtube.com/results?search_query={search2}")
        print(f"Mencari channel {search2}")
        print(f"Channel {search2} berhasil di buka!")
    elif opsi=="run -y -g":
        root2 = tk.Tk()
        root2.title(live)
        root2.geometry("500x500")
        label3 = tk.Label(root2,text="Youtube",fg="red")
        label3.pack()
        cari = tk.Entry(root2)
        cari.pack()
        def hasil_youtube():
            webbrowser.open_new(f"https://www.youtube.com/results?search_query={cari.get()}")
            label4 = tk.Label(root2,text=f"Membuka channel {cari.get()}")
            label4.pack()
            label5 = tk.Label(root2,text=f"Channel {cari.get()} berhasil di buka")
            label5.pack()
        btn2 = tk.Button(root2,text="Submit",command=hasil_youtube)
        btn2.pack()  
        root2.mainloop()
    else:
        print("Command not found")