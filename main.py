"""
Astro pinger:
Astro pinger was created for multiple reasons:
	1. Teaching users on how to use requests, and send them.
	2. Teaching users on how to thread.
Also astro pinger was explained with comments so new coders
learn how to use every library included.
I had a great time coding it, i hope you understand the code new coder.
"""
# I used try so exiting out of threads can be more stabler
try:
	import os # Imported for clearing screen and stuff
	import time # Imported for time sleeping
	import requests # Imported for requesting
	from threading import Thread # Imported for threading

	if os.name == "nt": # OS finding to run commands
		os.system("cls") # Clearing screen
		os.system("title Astro Pinger") # Setting a title

	else: # If the OS name is not equal to windows use Unix
		os.system("clear") # Clearing screen

	# Printing menu
	print("\u001b[38;5;46m                          ╔═╗╔═╗╔╦╗╦═╗╔═╗")
	print("\u001b[38;5;48m                          ╠═╣╚═╗ ║ ╠╦╝║ ║")
	print("\u001b[38;5;50m                          ╩ ╩╚═╝ ╩ ╩╚═╚═╝")
	print("\u001b[38;5;51m                         🛸 .gg/zeroday 🛸\n\n")

	# Set user input to variable
	ip = input("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo@localhost# Enter IP: \033[0m")
	port = input("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo@localhost# Enter Port: \033[0m")
	method = input("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo@localhost# Enter Method (GET OR POST): \033[0m")
	amount = input("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Input time to sleep every ping: ")

	if amount == "0": # Make this not a DoS tool
		print("this isn't a DoS tool retard.")
		exit() # Exit out of script.

	threaded = input("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Threaded? (Y/n): ")
	session = requests.Session() # Make requests faster

	def requestget(): # Send GET Requests function
		try: # Try inside a try :nerd:
			s = session.get(f"http://{ip}:{port}") # Send GET request
			if s.status_code in (200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210): # If statement for code 200
				print(f"\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Host replied back with code: {s.status_code}")
				time.sleep(int(amount)) # Time sleeping
			else: # Else statement for status code
				print(f"\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Host is probably down or not found, code: {s.status_code}")
				time.sleep(int(amount)) # Time sleeping
		except Exception as err: # Except for the try above :nerd:
			print("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Host is down, or no internet connection available.")
			time.sleep(int(amount)) # Time sleeping

	def requestpost(): # Send POST Requests function
		try: # Try inside a try before a try :ultra_nerd:
			s = session.post(f"http://{ip}:{port}") # Send POST request
			if s.status_code in (200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210): # If statement for status codes
				print(f"\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Host replied back with code: {s.status_code}")
				time.sleep(int(amount)) # Time sleeping
			else: # Else statement for status code
				print(f"\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Host is probably down or not found, code: {s.status_code}")
				time.sleep(int(amount)) # Time sleeping
		except Exception as err: # Except for the try below that try inside a try :ultra_nerd:
			print("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Host is down, or no internet connection available.")
			time.sleep(int(amount)) # Time sleeping

	def requestgetstart(): # Thread GET Request function
		while True: # While loop to spam threading
			Thread(target=requestget).start() # Thread start
			time.sleep(int(amount)) # Time sleeping

	def requestpoststart(): # Thread POST Request function
		while True: # While loop
			Thread(target=requestpost).start() # Thread start
			time.sleep(int(amount)) # Time sleeping

	if threaded.lower() == "y": # If statement to see if user wants to thread
		if method.lower() == "get": # Check the method variable to see which function to choose
			requestgetstart() # Start function
		if method.lower() == "post": # Check the method variable to see which function to choose
			requestpoststart() # Start function
		else: # Else statement to return to an error
			error = input("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - ERROR: You have entered a incorrect method and or you typed it incorrectly, press enter to exit.\033[0m")

	if threaded.lower() == "n": # Same thing here
		if method.lower() == "get": # ..
			while True: # ..
				requestget() # ..
		if method.lower() == "post": # ..
			while True: # ..
				requestpost() # ..
		else: # ..
			error = input("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - ERROR: You have entered a incorrect method and or you typed it incorrectly, press enter to exit.\033[0m") # ..

except KeyboardInterrupt: # Finish main try function
	print("\u001b[38;5;46ma\u001b[38;5;48mst\u001b[38;5;50mr\u001b[38;5;51mo - Exiting...")
	os._exit(1)
