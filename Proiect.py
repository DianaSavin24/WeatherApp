from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
     try:
          city=textfield.get()

          geolocator=Nominatim(user_agent="geoapiExercices")
          location= geolocator.geocode(city)
          obj=TimezoneFinder()
          result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
          print(result)

          home=pytz.timezone(result)
          local_time=datetime.now(home)
          current_time=local_time.strftime("%I:%M %p")
          clock.config(text=current_time)
          name.config(text="CURRENT WEATHER")

          #weather
          api_key="0dae8e2a2a61866a537de72cc394b12c"
          api=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

          json_data= requests.get(api).json()
          print(json_data)
          condition= json_data['weather'][0]['main']
          description =json_data['weather'][0]['description']
          temp= int(json_data['main']['temp']-273.15)
          pressure= json_data['main']['pressure']
          humidity = json_data['main']['humidity']
          wind= json_data['wind']['speed']

          t.config(text=(temp,"°"))
          c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

          w.config(text=wind)
          h.config(text=humidity)
          d.config(text=description)
          p.config(text=pressure)

     except Exception as e:
          messagebox.showerror("Weather App","Invalid Entry")



#search box
image = Image.open("da2.png")
Search_image = ImageTk.PhotoImage(image)
myimage=Label(image=Search_image)
myimage.place(x=20,y=10)

textfield=tk.Entry(root,justify="center",width=17,font=("Constantia",25,"bold"),border=0,fg="black")
textfield.place(x=100,y=40)
textfield.focus()

icon = Image.open("search_icon.png")
Search_icon= ImageTk.PhotoImage(icon)
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="white", command=getWeather)
myimage_icon.place(x=470,y=34)


#logo
logo_image = Image.open("logo.png")  
logo_image = ImageTk.PhotoImage(logo_image)
logo=Label(root, image=logo_image)
logo.image = logo_image
logo.place(x=210,y=105)


#bottom box
Frame_image=PhotoImage(file="box1.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


#time
name=Label(root,font=("Constantia",13,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Constantia",17))
clock.place(x=30,y=130)



#label
label1=Label(root,text="WIND",font=("Constantia",13,'bold'),fg="black")
label1.place(x=140,y=347) 

label2=Label(root,text="HUMIDITY",font=("Constantia",13,'bold'),fg="black")
label2.place(x=265,y=347) 

label3=Label(root,text="DESCRIPTION",font=("Constantia",13,'bold'),fg="black")
label3.place(x=450,y=347) 

label4=Label(root,text="PRESURE",font=("Constantia",13,'bold'),fg="black")
label4.place(x=635,y=347) 


t=Label(font=("arial",70,'bold'),fg="black")
t.place(x=440,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=440,y=250)

w=Label(text="...",font=("Constantia",17,"bold"))
w.place(x=145,y=390)
h=Label(text="...",font=("Constantia",17,"bold"))
h.place(x=290,y=390)
d=Label(text="...",font=("Constantia",17,"bold"))
d.place(x=435,y=390)
p=Label(text="...",font=("Constantia",17,"bold"))
p.place(x=640,y=390)





root.mainloop()















