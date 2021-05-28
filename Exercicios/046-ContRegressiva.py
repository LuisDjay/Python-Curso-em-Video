import emoji
from time import sleep
for c in range (10, -1, -1):
    sleep(0.5)
    print (c)
print(emoji.emojize(':fireworks:'*50, use_aliases=True))
print(emoji.emojize('FELIZ ANO NOVO!! :fireworks:', use_aliases=True))
