import re

def clean_text(text):
    text = re.sub(r'<[^>]*?>', '', text)
    #remove URLS
    text= re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',text)
    #remove special charcters
    text=re.sub(r'[^a-zA-Z0-9 ]','',text)
    #replace multiple spaces
    text=re.sub(r'\s{2,}','',text)
    #trim leading and trailing
    text=text.strip()
    #remove extra whitespace
    tex=''.join(text.split())
    return text
