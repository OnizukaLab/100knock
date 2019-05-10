import urllib.request, urllib.parse
import json
import re

params = {
    "action": "query",
    "format": "json",
    "titles": "File:Flag of the United Kingdom.svg",
    "prop": "imageinfo",
    "iiprop": "url"
}
p = urllib.parse.urlencode(params)
url = "https://commons.wikimedia.org/w/api.php?" + p

with urllib.request.urlopen(url) as res:
   html = res.read().decode("utf-8")
   imgurl = re.sub(".*['\"]url['\"]\s*:\s*['\"](.*?)['\"].*", "\\1", html)
   print(imgurl)
