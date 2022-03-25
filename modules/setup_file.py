from os import environ, path, remove


def check_setup():
	global config_path
	return path.exists(config_path)


def read_setup():
	global config_path
	#return folder_path, startup_delay, number_of_pages
	pass

# example
def read(setup_file_path):
	setup_file = open(setup_file_path, "r")
	temp = setup_file.read().replace("\n", "")
	microphone_position = int(temp.split("=")[1].strip())
	setup_file.close()
	del temp
	return microphone_position	


def whrite_setup():
	global config_path
	pass


def create_setup():
	global config_path

	folder_path = environ["USERPROFILE"] + r"\Desktop\Auto-Screens"
	
	config_file = open(config_path, "w")
	print(f"""\
		folder_path = {folder_path}
		startup_delay = 5
		number_of_pages = 1""",
		file=config_file)
	config_file.close()


def del_setup():
	global config_path
	remove(config_path)


setup_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Documents/Auto-Screenshot-Page_Setup.txt")


if __name__ == "__main__":
	create_setup()
	check_setup()
	#del_setup()
	#check_setup()
	#read_setup()
	#whrite_setup()
