"""
Icon from https://iconarchive.com/show/seasonal-icons-by-robinweatherall/cloud-dark-icon.html
"""

import os
import requests
import sys

from PIL import Image
from PIL import ImageTk
from io import BytesIO
from time import localtime
from time import strftime
from tkinter import *

# Width and the height of the window
WIDTH = 800
HEIGHT = 500

# The directory containing this file
THIS = os.path.abspath(os.path.dirname(__file__))

# Copy and paste your API key here
API_KEY = '0fa0eb1029b422ba434ffff1758bff25'

# Create the starter class for the app
class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	# Create init_window
	def init_window(self):
		def clear(self):
			e.set("")

		def key_submit(event):
			if(event.keysym == 'Return'):
				try:
					search = search_entry.get()
					# Create the url to use to fetch data
					url = f'https://api.openweathermap.org/data/2.5/weather?q={search}&units=metric&appid={API_KEY}'
					# print(search, url)

					# Fetch data
					response = requests.get(url)
					data = response.json()

					# print(data)
					if(len(data) == 13):
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
						time_date["text"] = f'{strftime("%H:%M - %A, %d %b %Y", localtime(int(data["dt"])+int(data["timezone"])))}'

						# Update the search bos
						e.set('')

						longitudes["text"] = f'Longitudes: {data["coord"]["lon"]}'
						latitudes["text"] = f'Latitudes: {data["coord"]["lat"]}'
						temp_range["text"] = f'Temperature Range: {data["main"]["temp_min"]} - {data["main"]["temp_max"]}'
						humidity["text"] = f'Humidity: {data["main"]["humidity"]}'
						wind_speed["text"] = f'Wind speed: {data["wind"]["speed"]} m/s'
						cloudy["text"] = f'Couldy: {data["clouds"]["all"]}%'
					if(len(data) == 2 and int(data['cod']) == 404):
						# Add connection error image to the r_image
						# r_image = requests.get(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png")
						# load = Image.open(BytesIO(r_image.content))
						file = os.path.join(THIS, "img\\404.gif")
						render = PhotoImage(file="img\\404.gif")
						img["image"] = render
						img.image = render

						# Update the explanation label
						exp["text"] = f'{data["cod"]}: {data["message"]}'

						# Update the temperature label
						temp["text"] = ''

						# Update the place label
						place["text"] = ''

						# Update the time_date label
						time_date["text"] = ''

						# Update the search bos
						e.set('')

						longitudes["text"] = ''
						latitudes["text"] = ''
						temp_range["text"] = ''
						humidity["text"] = ''
						wind_speed["text"] = ''
						cloudy["text"] = ''

				except requests.exceptions.ConnectionError:
					# Add connection error image to the r_image
					# r_image = requests.get(f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png")
					# load = Image.open(BytesIO(r_image.content))
					file = os.path.join(THIS, "img\\no_connection.gif")
					render = PhotoImage(file=file)
					img["image"] = render
					img.image = render

					# Update the explanation label
					exp["text"] = f'Unable to connect.\nCheck your connection and try again.'

					# Update the temperature label
					temp["text"] = ''

					# Update the place label
					place["text"] = ''

					# Update the time_date label
					time_date["text"] = ''

					# Update the search bos
					e.set('')

					longitudes["text"] = ''
					latitudes["text"] = ''
					temp_range["text"] = ''
					humidity["text"] = ''
					wind_speed["text"] = ''
					cloudy["text"] = ''

		# Change the title of the window
		self.master.title('Weather App')
		# self.master.iconname('weatherapp')
		# self.master.iconbitmap(self, default='img\\Robinweatherall-Seasonal-Cloud-dark.ico');

		# Allow the widget to take the full space of root window
		self.pack(fill=BOTH, expand=1)

		# Create a quit button
		Button(self.master, text='Quit', width=10, height=2, borderwidth=0, bg="#FF0000", fg="#FFFFFF", font=("Roboto", 9), command=self.client_exit).place(relx=1, rely=1, anchor=SE)

		# Create the left label
		showcase_frame = Frame(self, width=WIDTH-WIDTH/2.5, height=HEIGHT, bg="gray50")
		showcase_frame.pack(side=LEFT, expand=True, fill=BOTH)

		# image label
		img = Label(showcase_frame, bg="gray50")
		img.pack(pady=(50,20), side=TOP)
	   	# explanation label
		exp = Label(showcase_frame, font=('Roboto', 12), bg="gray50")
		exp.pack(side=TOP)

	   	# temperature label
		temp = Label(showcase_frame, font=('Roboto', 32, 'bold'), bg="gray50")
		temp.pack(side=TOP)

	   	# place label
		place = Label(showcase_frame, font=('Roboto', 23), bg="gray50")
		place.pack(side=TOP)

		# time and date label
		time_date = Label(showcase_frame, font=('Roboto', 15), bg="gray50")
		time_date.pack(side=TOP)

		# Create the entry frame
		entry_frame = Frame(self, width=WIDTH/2.5, height=HEIGHT, bg="gray50")

		# Create a search input
		e = StringVar()
		search_entry = Entry(entry_frame, textvariable=e, font=('Roboto', 10), borderwidth=5, relief="flat")
		search_entry.bind('<FocusIn>', clear)
		search_entry.bind('<Key>', key_submit)
		search_entry.grid(row=0, column=0, padx=(3,10), pady=(70, 100), ipadx=40, ipady=7)
		e.set("Enter city or zip code")

		# Create a submit button
		search_button = Button(entry_frame, text="Search", font=('Roboto', 10), command=lambda: submit())
		search_button.grid(row=0, column=1, pady=(70, 100), ipadx=20, ipady=7)

		longitudes = Label(entry_frame, font=('Roboto', 10), bg="gray50")
		longitudes.grid(row=3, column=0, padx=(10,0))
		latitudes = Label(entry_frame, font=('Roboto', 10), bg="gray50")
		latitudes.grid(row=4, column=0, padx=(10,0))
		temp_range = Label(entry_frame, font=('Roboto', 10), bg="gray50")
		temp_range.grid(row=5, column=0, padx=(10,0))
		humidity = Label(entry_frame, font=('Roboto', 10), bg="gray50")
		humidity.grid(row=6, column=0, padx=(10,0))
		wind_speed = Label(entry_frame, font=('Roboto', 10), bg="gray50")
		wind_speed.grid(row=7, column=0, padx=(10,0))
		cloudy = Label(entry_frame, font=('Roboto', 10), bg="gray50")
		cloudy.grid(row=8, column=0, padx=(10,0))

		entry_frame.pack(side=LEFT, fill=BOTH)

		# Create a function to fetch the data
		def submit():
			try:
				search = search_entry.get()
				# Create the url to use to fetch data
				url = f'https://api.openweathermap.org/data/2.5/weather?q={search}&units=metric&appid={API_KEY}'
				# print(search, url)

				# Fetch data
				response = requests.get(url)
				data = response.json()

				# print(data)
				if(len(data) == 13):
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
				if(len(data) == 2 and int(data['cod']) == 404):
					# Add connection error image to the r_image
					file = os.path.join(THIS, "img\\404.gif")
					render = PhotoImage(file="img\\404.gif")
					img["image"] = render
					img.image = render

					# Update the explanation label
					exp["text"] = f'{data["cod"]}: {data["message"]}'

					# Update the temperature label
					temp["text"] = ''

					# Update the place label
					place["text"] = ''

					# Update the time_date label
					time_date["text"] = ''

					# Update the search bos
					e.set('')

					longitudes["text"] = ''
					latitudes["text"] = ''
					temp_range["text"] = ''
					humidity["text"] = ''
					wind_speed["text"] = ''
					cloudy["text"] = ''

			except requests.exceptions.ConnectionError:
				# Add connection error image to the r_image
				file = os.path.join(THIS, "img\\no_connection.gif")
				render = PhotoImage(file="img\\no_connection.gif")
				img["image"] = render
				img.image = render

				# Update the explanation label
				exp["text"] = f'Unable to connect.\nCheck your connection and try again.'

				# Update the temperature label
				temp["text"] = ''

				# Update the place label
				place["text"] = ''

				# Update the time_date label
				time_date["text"] = ''

				# Update the search bos
				e.set('')

				longitudes["text"] = ''
				latitudes["text"] = ''
				temp_range["text"] = ''
				humidity["text"] = ''
				wind_speed["text"] = ''
				cloudy["text"] = ''

	def client_exit(self):
		sys.exit(0)

def weather():
	root = Tk()

	# Size of the window
	root.overrideredirect(1)
	POS_X = int(root.winfo_screenwidth()/2-WIDTH/2)
	POS_Y = int(root.winfo_screenheight()/2-HEIGHT/2)
	root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')
	root.resizable(0,0)
	root.wm_attributes("-transparentcolor", 'grey')
	app = Window(root)

	root.mainloop()
