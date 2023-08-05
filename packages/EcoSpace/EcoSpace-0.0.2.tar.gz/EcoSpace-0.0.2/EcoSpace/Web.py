from requests import get
from base64 import b64encode

def ShortLink(url):
    url = str(b64encode(url.encode('utf-8')))[2:-1]
    url = get('https://www.mxnzp.com/api/shortlink/create?app_secret=WnhrK251TWlUUThqaVFWbG5OeGQwdz09&app_id=rgihdrm0kslojqvm&url='+url).json()['data']
    return 'https://ecospace.top/api/sl.php?url='+url['shortUrl'].split('/')[-1]