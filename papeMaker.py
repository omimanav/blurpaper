from PIL import Image, ImageFilter
import readline, os #need to sort out local files autocomplete

done = False

while not done:
	path = input("Enter 'exit'to exit or\nPath to image.\n>>> ")
	if "~" in path:
		path.replace("~", os.environ["HOME"])
	try:
		image = Image.open(path)
		bg = image.resize((2560,2560//(image.width/image.height))).filter(ImageFilter.GaussianBlur(10))
		image = image.resize((1366,1366//(image.width/image.height)))
		bg.paste(img, ((bg.width-image.width)//2),(bg.height-image.height)//2)

		bg.save()
		image.close()
		bg.close()
	except Exception as e:
		print(f"Please enter a valid path.\n{e}\n")

	if path.lower() == "exit":
		done = True
