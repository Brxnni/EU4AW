import	re
import	os
import	sys
from	PIL import Image

assert len(sys.argv) == 2

def convertFile(filePath, deleteOld = False):
	newFilePath = re.sub(".dds$", ".png", filePath)
	
	img = Image.open(filePath)
	img.save(newFilePath)

	if deleteOld:
		os.remove(filePath)

def convertTree(treePath, deleteOld = False):
	print(treePath)

	for path, dirs, files in os.walk(treePath):
		for fileName in files:
			if fileName.endswith(".dds"):
				convertFile(os.path.join(path, fileName), deleteOld)

convertTree(
    os.path.join(
		os.path.dirname(__file__),
		sys.argv[1]
	),
    True
)