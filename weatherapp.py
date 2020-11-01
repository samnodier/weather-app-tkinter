"""
Icons from https://iconarchive.com/show/seasonal-icons-by-robinweatherall/cloud-dark-icon.html
"""

from tkinter import *
from PIL import Image, ImageTk
import requests
from time import localtime, strftime
from io import BytesIO

# Copy and paste your API key here
API_KEY = '0fa0eb1029b422ba434ffff1758bff25'

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Create init_window
    def init_window(self):
        def clear(self):
            e.set("")

        # Change the title of the window
        self.master.title('Weather App')
        self.master.iconname('weatherapp')
        self.master.iconbitmap(self, default='Robinweatherall-Seasonal-Cloud-dark.ico');

        # Allow the widget to take the full space of root window
        self.pack(fill=BOTH, expand=1)

        # Create a quit button
        Button(self.master, text='Quit', bg="#FF0000", fg="#FFFFFF", font=("Roboto", 9), command=self.client_exit).place(relx=1, rely=1, anchor=SE)

        request_back_image = requests.get('https://images.unsplash.com/photo-1415750465391-51ed29b1e610?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80')
        load = Image.open(BytesIO(request_back_image.content))
        background_image = ImageTk.PhotoImage(load)

        # Create the left label
        showcase_frame = Frame(self, width=WIDTH-WIDTH/2.5, height=HEIGHT)
       	showcase_frame.pack(side=LEFT, expand=True, fill=BOTH)

        # Background label
        background_label = Label(showcase_frame, image = background_image)
        background_label.place(x=-2, y=-2)
        background_label.image = background_image

       	# image label
        img = Label(showcase_frame)
        img.pack(pady=(50,20), side=TOP)
       	# explanation label
        exp = Label(showcase_frame, font=('Roboto', 12))
        exp.pack(side=TOP)

       	# temperature label
        temp = Label(showcase_frame, font=('Roboto', 32, 'bold'))
        temp.pack(side=TOP)

       	# place label
        place = Label(showcase_frame, font=('Roboto', 23))
        place.pack(side=TOP)

       	# time and date label
        time_date = Label(showcase_frame, font=('Roboto', 15))
        time_date.pack(side=TOP)

       	# Create the entry frame
       	entry_frame = Frame(self, width=WIDTH/2.5, height=HEIGHT)

        # Create a background color label
        background_color = Label(entry_frame)
        background_color.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a search input
       	e = StringVar()
       	search_entry = Entry(entry_frame, textvariable=e, font=('Roboto', 9))
        search_entry.bind('<FocusIn>', clear)
        search_entry.grid(row=0, column=0, padx=(0,10), pady=(70, 100), ipadx=40, ipady=10)
       	e.set("Enter city or zip code")

        # Create a submit button
       	search_button = Button(entry_frame, text="Search", font=('Roboto', 9), command=lambda: submit())
        search_button.grid(row=0, column=1, padx=(10,0), pady=(70, 100), ipadx=20, ipady=10)

        longitudes = Label(entry_frame, font=('Roboto', 10))
        longitudes.grid(row=3, column=0, padx=(10,0))
        latitudes = Label(entry_frame, font=('Roboto', 10))
        latitudes.grid(row=4, column=0, padx=(10,0))
        temp_range = Label(entry_frame, font=('Roboto', 10))
        temp_range.grid(row=5, column=0, padx=(10,0))
        humidity = Label(entry_frame, font=('Roboto', 10))
        humidity.grid(row=6, column=0, padx=(10,0))
        wind_speed = Label(entry_frame, font=('Roboto', 10))
        wind_speed.grid(row=7, column=0, padx=(10,0))
        cloudy = Label(entry_frame, font=('Roboto', 10))
        cloudy.grid(row=8, column=0, padx=(10,0))

       	entry_frame.pack(side=LEFT, fill=BOTH)

        # Create a function to fetch the data
        def submit():
            search = search_entry.get()
            # Create the url to use to fetch data
            url = f'https://api.openweathermap.org/data/2.5/weather?q={search}&units=metric&appid={API_KEY}'
            print(search, url)

            # Fetch data
            response = requests.get(url)
            data = response.json()

            print(data)

            # Add data to the image label
            r_image = requests.get(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png")
            load = Image.open(BytesIO(r_image.content))
            render = ImageTk.PhotoImage(load)
            img["image"] = render
            img.image = render

            # Update the explanation label
            exp["text"] = f'{data["weather"][0]["main"]}'

            # Update the temperature label
            temp["text"] = f'{data["main"]["temp"]}\u2070'

            # Update the place label
            place["text"] = f'{data["name"]}, {data["sys"]["country"]}'

            # Update the time_date label
            time_date["text"] = f'{strftime("%H:%M - %A, %d %b %Y", localtime(int(data["dt"])))}'

            # Update the search bos
            e.set('')

            longitudes["text"] = f'Longitudes: {data["coord"]["lon"]}'
            latitudes["text"] = f'Latitudes: {data["coord"]["lat"]}'
            temp_range["text"] = f'Temperature Range: {data["main"]["temp_min"]} - {data["main"]["temp_max"]}'
            humidity["text"] = f'Humidity: {data["main"]["humidity"]}'
            wind_speed["text"] = f'Wind speed: {data["wind"]["speed"]} m/s'
            cloudy["text"] = f'Couldy: {data["clouds"]["all"]}%'


    def client_exit(self):
    	exit()

root = Tk()

# Size of the window
WIDTH = 800
HEIGHT = 500
root.overrideredirect(1)
POS_X = int(root.winfo_screenwidth()/2-WIDTH/2)
POS_Y = int(root.winfo_screenheight()/2-HEIGHT/2)
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')
root.resizable(0,0)
root.wm_attributes("-transparentcolor", 'grey')
app = Window(root)

root.mainloop()
