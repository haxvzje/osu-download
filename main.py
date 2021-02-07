from console.utils import set_title
from os import mkdir, path, system, name
from requests import Session,get
from yaml import safe_load
import random
import time
import re

default_values = '''Setting:
  #Your UserName
  UserName: User

  #Open osu & Import beatmap after this beatmap has been downloaded
  Import: false
'''

if path.exists('Config.yml'):
    settings = safe_load(open('Config.yml', 'r', errors='ignore'))
else:
    open('Config.yml', 'w').write(default_values)
    settings = safe_load(open('Config.yml', 'r', errors='ignore'))

if path.exists('Downloaded'):
	pass
else:
    mkdir('Downloaded')

def filename(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def main():
	system('cls')
	print(logo + f"\nVersion: {version}")
	print(f"Author: {author}")
	print(f"User: {minhbuoiteo.user}")
	code = input("\nBeatmap ID (Ex: '586121#osu'): ")
	if code=='':
		print("\nBeatmap ID is required")
		time.sleep(1)
		return
	urlapi = 'https://chimu.moe/d/'
	url = urlapi + code
	print("\nDownloading Beatmap....")
	try:
		r = get(url, allow_redirects=True)
		nameold = filename(r.headers.get('content-disposition'))
		name = nameold.replace('"', '')
		open(f'Downloaded/{name}' , 'wb').write(r.content)
		print(f"\nBeatmap Download Successful ({name})")
		if minhbuoiteo.importmap:
			fileimport = f'Downloaded\\{name}'
			system('"' + fileimport + '"')
		time.sleep(2)
	except:
		print(f"\nAn error occurred while download {code} beatmap...\n\nTroubleshoot:\n- Your Beatmap ID not valid \n- Check your network connection\n")
		input("Press any key to exit....")
		return

class minhbuoiteo:
    user = str(settings['Setting']['UserName'])
    importmap = bool(settings['Setting']['Import'])

if __name__ == '__main__':
	logo = '''   ____   _____ _    _ _ _____   ______          ___   _ _      ____          _____  
  / __ \ / ____| |  | | |  __ \ / __ \ \        / / \ | | |    / __ \   /\   |  __ \ 
 | |  | | (___ | |  | | | |  | | |  | \ \  /\  / /|  \| | |   | |  | | /  \  | |  | |
 | |  | |\___ \| |  | | | |  | | |  | |\ \/  \/ / | . ` | |   | |  | |/ /\ \ | |  | |
 | |__| |____) | |__| |_| |__| | |__| | \  /\  /  | |\  | |___| |__| / ____ \| |__| |
  \____/|_____/ \____/(_)_____/ \____/   \/  \/   |_| \_|______\____/_/    \_\_____/ 
'''
	version = '1.2-debug'
	author = 'Osu!player'
	session = Session()
	time.sleep(2)
	set_title(f'Osu!Download - v{version} | by {author}')
	while True:
		main()
	input()
