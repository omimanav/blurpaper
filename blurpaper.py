#!/usr/bin/env python3

from PIL import Image, ImageFilter
import readline, os #need to sort out local files autocomplete

done = False

while not done:
	path = input("Enter 'exit' to exit or\nPath to image.\n>>> ")

	if path.lower() == "exit":
		break

	if "~" in path:
		path = path.replace("~", os.environ["HOME"])

	try:
		image = Image.open(path)
		bg = image.crop((((image.width-image.width*0.8)//2) , (image.height-image.height*0.8)//2, (image.width+image.width*0.8)//2, (image.height+image.height*0.8)//2))
		bg.show()
		bg = bg.resize((2560, int(2560//(image.width/image.height))))
		try:
			blur = int(input("Select a level of blur to apply on the background:\n1: None\n2: Low\n3: Medium\n4: High\n>>> "))
		except Exception as e:
			print("Please select an option as listed by entering the number and pressing the return/enter key.\ne.g. >>> 1\n")
			break
		bg = bg.filter(ImageFilter.GaussianBlur({1: 0, 2: 5, 3: 25, 4:50}[blur]))
		image = image.resize((1366, int(1366//(image.width/image.height))))
		bg.paste(image, ((bg.width-image.width)//2, (bg.height-image.height)//2))

		bg.save(f"{os.environ['HOME']}/Downloads/blurpape.jpg")
		print("Saved as ~/Downloads/blurpape.jpg")
		image.close()
		bg.close()
	except Exception as e:
		print(f"Please enter a valid path.\n{e}\n")
