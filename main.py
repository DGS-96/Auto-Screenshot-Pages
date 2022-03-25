from os import environ, path

# Import my modules
import sys
sys.path.insert(0, "modules")

from create_screenshots import start_as
from input_validation import check_path, check_pages, check_delay, check_input_arg
from display_info import display_help, display_info


def info():
	global settings
	
	display_info(folder_path, startup_delay, number_of_pages)
	print(settings)


print("\n" + "=" * 6 , "Automatic screenshot of multiple pages",  "=" * 6)


# Default setup
if check_config():
	folder_path, startup_delay, number_of_pages = read_setup()
	settings = "Settings from setup file."
else:
	# Windows
	#folder_path = environ["USERPROFILE"] + r"\Desktop\Auto-Screens"
	folder_path = "Test"
	startup_delay = 5
	number_of_pages = 1
	settings = "Default settings."


# First output of information
info()
print("Type 'help' or 'h' to show commands.\n")


while True:
	user_input = input("> ").lower().split()
	first_arg = user_input[0]

	# Input without arguments
	if first_arg in ("help", "h", "run", "r", "info", "i", "quit", "q"):
		if first_arg in ("help", "h"):
			display_help()

		elif first_arg in ("run", "r"):
			del(user_input)
			del(first_arg)

			print(f"Go to the desired window with the document, you have \
				{startup_delay} seconds!")
			start_as(number_of_pages, folder_path, startup_delay)
			print("Completed!")
			break

		elif first_arg in ("info", "i"):
			display_info(folder_path, startup_delay, number_of_pages)

		elif first_arg in ("quit", "q"):
			print(f"Exit by typing {first_arg}.")
			print("Goodbye, Have a nice screenshots!")
			break

	# Work with config file
	elif first_arg in ("whrite", "wc", "create", "cc", "delete", "dc"):
		if first_arg in ("whrite", "wc"):
			pass
		elif first_arg in ("create", "cc"):
			pass
		elif first_arg in ("delete", "dc"):
			pass

	# Input with arguments
	elif first_arg in ("pages", "p", "path", "ph", "delay", "d"):
		if check_input_arg(user_input):

			if first_arg in ("pages", "p"):
				if check_pages(user_input[1]):
					number_of_pages = int(user_input[1])
					info()

			elif first_arg in ("path", "ph"):
				check_path(user_input[1])
				info()

			elif first_arg in ("delay", "d"):
				if check_delay(user_input[1]):
					startup_delay = int(user_input[1])
					info()

	else:
		print("Invalid input.")
