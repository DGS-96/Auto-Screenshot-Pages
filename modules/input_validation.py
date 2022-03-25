def check_positive_int(var):
	if var.isdigit():
		var = int(var)
		if var > 0:
			return True
	print("The input must be a positive integer.")
	return False


def check_path(path):
	# Доделать проверки пути в виндоус !!!!!!!!!!!!!!!
	print(f"{path = }")


def check_pages(pages):
	return check_positive_int(pages)


def check_delay(delay):
	return check_positive_int(delay)


def check_input_arg(user_input):
	if len(user_input) == 2:
		return True
	print("The input must have two arguments.")
	return False


if __name__ == '__main__':
	check_path("path")

	check_pages("pages")
	check_pages("4")
	check_pages("5.2")
	check_pages("0")
	check_pages("-1")

	check_delay("15")

	check_input(["abc"])
	check_input(["abc", "abc"])
