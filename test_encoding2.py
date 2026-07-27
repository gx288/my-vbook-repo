with open('plugin.json', 'rb') as f:
    content = f.read()
    print("Has BOM:", content.startswith(b'\xef\xbb\xbf'))
    print(content[:100])
