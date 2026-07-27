import urllib.request

def check_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        urllib.request.urlopen(req)
        print(url, "WORKS")
    except Exception as e:
        print(url, "FAILS:", e)

check_url('https://dasactruyen.com/index.php/the_loai/bach-hop/page/2/')
check_url('https://dasactruyen.com/index.php/the_loai/bach-hop/?page=2')
