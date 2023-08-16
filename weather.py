import tkinter as tk
from tkinter import ttk,PhotoImage,Canvas
from PIL import Image,ImageTk
import requests
# key =695b3e7de2e5c6d0f13175870819342d
# new key = 37b238d42db737768b74a785ebe58fbc
class Webapp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x450")
        self.root.title(" Weather App ")
        self.img = PhotoImage(file="icon.png")
        self.root.iconphoto(False,self.img)
        self.photo = Image.open("asd.png")
        self.rphoto = self.photo.resize((500, 450), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.rphoto)
        self.mainframe = Canvas(self.root, width=500, height=450)
        self.mainframe.pack(fill='both', expand=True)
        self.mainframe.create_image(0, 0, image=self.photo, anchor='nw')
        self.mainframe.create_text(180,57,text = "Enter The Name Of City : ",font=("comic sans ms",14,"bold"))
        self.clis = ["Chennai","Mumbai","Hyderabad","Bangalore","Kolkata","Ahmedabad","Pune","Surat","Lucknow","New Delhi","Nashik","Bhopal","Visakhapatnam","Agra","Jaipur","Nagpur","Kanpur","Chandigarh"]
        self.clis.sort()
        self.cname = str()
        self.cbox = ttk.Combobox(self.mainframe,values = self.clis,font=("Arial",12,"bold"),textvariable=self.cname)
        self.cbox.place(x=310, y=45, height=25, width=130)
        self.wbtn = ttk.Button(self.mainframe,text = " Check Weather ",command = self.checkw)
        self.wbtn.place(x=145,y=120,height=30,width="200")
        self.root.mainloop()
    def checkw(self):
        self.city = self.cbox.get()
        self.data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + self.city + "&appid=37b238d42db737768b74a785ebe58fbc").json()
        self.mainframe.create_text(240,200,text = " Climate : " + self.data["weather"][0]["main"],font=("comic sans ms",10,"bold"))
        self.mainframe.create_text(240,220,text = " Discription : " + self.data["weather"][0]["description"],font=("comic sans ms",10,"bold"))
        self.mainframe.create_text(240,240,text = " Temperature : " + str(round(self.data["main"]["temp"] - 273.15, 2)),font=("comic sans ms",10,"bold"))
        self.mainframe.create_text(240,260,text = " Minimum Temperature : " + str(round(self.data["main"]["temp_min"] - 273.15, 2)) ,font=("comic sans ms",10,"bold"))
        self.mainframe.create_text(240,280,text = " Maximum Temperature : " + str(round(self.data["main"]["temp_max"] - 273.15, 2)),font=("comic sans ms",10,"bold"))
        self.mainframe.create_text(240,300,text = " Pressure : " + str(self.data["main"]["pressure"]),font=("comic sans ms",10,"bold"))
Webapp()