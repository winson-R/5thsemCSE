# import module
from pdf2image import convert_from_path


# Store Pdf with convert_from_path function
images = convert_from_path('3 bigqut.pdf')
# print(images)
print("started!!!")

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

print("Done")