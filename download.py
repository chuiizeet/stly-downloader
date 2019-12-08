import requests
from PIL import Image
import os
import sys

_api = 'http://api.sticker.ly/v1/stickerPack/'
name = ''
urls = []
code = sys.argv[1]
api = _api+code

# Get data
r = requests.get(api)
_json = r.json()
name = str((_json['result']['name'])).replace(' ', '_')
static_link = _json['result']['resourceUrlPrefix']
for l in _json['result']['resourceFiles']:
	link = static_link+l
	urls.append(link)


def downloader():

	print("-------------------")
	print("URL: "+ api)
	print("-------------------")

	# Make dir
	path = './stickers/'+(name)
	if not os.path.exists(path):
		os.mkdir(path, 0o755)
	else:
		print("The path already exist.")
		return

	for e,link in enumerate(urls):
		os.system('wget -O '+str(e)+'.png '+str(link))

		# Change image size
		im = Image.open(str(e) +'.png')
		im = im.resize((512, 512))

		# Delete old file and save new file
		os.system('rm '+str(e)+'.png')
		im.save(str(e)+'.webp', "webp", quality=40)

		# Move items
		os.system('mv *.webp ./stickers/'+name)

downloader()