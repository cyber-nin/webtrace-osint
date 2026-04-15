def extract_links(text):
    import re
    urls = re.findall(r'https?://\S+', text)
    return urls
