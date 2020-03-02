run: main.py display.py draw.py matrix.py parse.py
	python main.py
	#magick convert pic.ppm image.png
	#imdisplay image.png 

clean:
	rm *.pyc
	rm *~
