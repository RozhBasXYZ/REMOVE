import os
if __name__ == "__main__":
	try:
		__import__("REMOVE").make()
	except Exception as e:
		exit(e)
