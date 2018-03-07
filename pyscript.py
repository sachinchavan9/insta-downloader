import requests
import base64
from bs4 import BeautifulSoup
from colorama import init
from datetime import datetime
import urllib
import urllib2
import sys
import random
from termcolor import cprint
from pyfiglet import figlet_format
import os
from colorama import Fore
from requests import exceptions

init(autoreset=True)


def insta_dump():
    url = raw_input("Please input " + Fore.RED + "INSTAGRAM " + Fore.RESET + "url: ")
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'html5lib')

    video_find = soup.find('meta', attrs={"property": "og:video"})
    try:
        video_link = video_find.get("content")
    except AttributeError:
        pass
    else:
        video_ext = str(video_link).split(".")[-1:]
        video_read = urllib2.urlopen(video_link)
        with open(str(datetime.now().strftime("%d%m%Y%H%M%S")) + "." + video_ext[0], "wb") as video:
            video.write(video_read.read())
        print("video saved !")
        sys.exit()
    image_find = soup.find('meta', attrs={"property": "og:image"})
    image_link = image_find.get("content")
    img_ext = str(image_link).split(".")[-1:]
    image_read = urllib.urlopen(image_link).read()
    image_64_encode = base64.encodestring(image_read)
    image_64_decode = base64.decodestring(image_64_encode)
    image_result = open(str(datetime.now().strftime("%d%m%Y%H%M%S")) + "." + img_ext[0], "wb")
    image_result.write(image_64_decode)
    print("image saved")


def hidden_tresure():
    init(strip=not sys.stdout.isatty())
    fig_font = ['3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner',
                'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'block',
                'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'computer',
                'contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge', 'cybermedium',
                'cybersmall', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'drpepper', 'eftichess', 'eftifont',
                'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy',
                'goofy', 'gothic', 'graffiti', 'hollywood', 'invita', 'isometric2', 'isometric3',
                'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban', 'larry3d', 'lcd', 'lean',
                'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mini', 'mirror', 'mnemonic',
                'moscow', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre',
                'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid', 'rectangles', 'relief',
                'rev', 'roman', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap',
                'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript',
                'smshadow', 'smslant', 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars', 'stellar', 'stop',
                'straight', 'tanja', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant',
                'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'usaflag', 'wavy', 'weird']
    ran_font = random.choice(fig_font)
    cprint(figlet_format("hidden treasure", font=ran_font), 'red', 'on_grey', attrs=['bold'])
    print("[!] " + ran_font)
    
    pass


if __name__ == "__main__":
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    hidden_tresure()
    insta_dump()
