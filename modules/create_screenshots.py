from time import sleep
from pyautogui import screenshot, press, hotkey


def start_as(number_of_pages, folder_path, startup_delay):
	# Sleep for ... seconds to allow me to open book
	sleep(startup_delay)
	
	# Range can be changed depending on the number of pages
	for page in range(number_of_pages):
		# Take and save a screenshot
		screenshot(f"{folder_path}/page-{page}.png")
		
		#pyautogui.screenshot().save(r'file_path/filename.png')
		#screenshot().save(f"{folder_path}/page-{page}.png")
		
		sleep(0.05)
		# Turn page
		press("right")

	# Switch to terminal
	hotkey("alt", "tab")


if __name__ == '__main__':
	# Linux
	#start_as(2, "/home/dg/Pictures", 5)

	# Windows
	#start_as(2, "/home/dg/Pictures", 5)
	pass
