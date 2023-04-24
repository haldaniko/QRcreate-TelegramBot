import validators

while True:
    link = str(input('Link: '))
    if validators.url(link):
        print('Link Ok')
    else:
        print('Link false')
