from PIL import Image, ImageDraw, ImageFont
from random import randint
from pathlib import Path
from textwrap import wrap
quotes = open('AbabouQuotes.txt').read().split('/')
for x in range(100):
    quote_index = randint(0,len(quotes))-1
    string = quotes[quote_index]
    w = 640
    h = 256
    colors = ['white','red','yellow','green','blue','magenta','black','purple']
    index = randint(0,len(colors)-1)
    img = Image.new('RGBA', (w,h), colors[index])
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('arial.ttf', 20)

    if index < 4:
        text_color = 'black'
    else:
        text_color = 'white'

    text = wrap(string,40)
    print(''.join(text))
    if 'Mohamed' in text[len(text)-2] and 'Ababou' in text[len(text)-1]:
        first = text.pop(len(text)-2)
        second = text.pop(len(text)-1)
        text.append(' '.join([first,second]))
        print(''.join(text), '\n')
    string = '\n'.join(text)
    d.multiline_text((w/5,h/2.5), string, font = fnt, fill = text_color, align = 'center', spacing = 4)
    path = Path(f'new_quotes/ababou_quote{quote_index}.png')
    img.save(path)
