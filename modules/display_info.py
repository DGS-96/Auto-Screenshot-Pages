def display_info(folder_path, startup_delay, number_of_pages):
	print(symbol * 23, "Info", symbol * 23,
f"""
Total  pages : {number_of_pages}
Startup delay: {startup_delay} seconds
Folder path  : {folder_path}
""")


def display_help():
	print(symbol * 23, "Help", symbol * 23,
"""
To change the number of pages, enter:
	"pages <number>" or "p <number>"

To change the start delay, enter:
	"delay <seconds>" or "d <seconds>"

To change the folder for screenshots, enter:
	"path <../folder name" or "ph <../folder name>"

To view information about the output folder,
number of pages, and startup delay, enter:
	"info" or "i"

To run the program, enter:
	"run" or "r"
After the program has been started, switch to the multipage document window.
After the specified delay time has elapsed, the "delay" will a program is
launched that switches desired number of "pages" to the right, take a screenshot
and save along the given path. At the end, the window will change to a terminal
and a completion message will appear.

Setup file
	"whrite" or "wc"
	"create" or "cc"
	"delete" or "dc"

To interrupt the program press:
	"ctrl+c"

To exit, enter:
	"quit" or "q"
""")

symbol = "-"

if __name__ == '__main__':
	display_info("test/path/", "test number", "test delay")
	display_help()
