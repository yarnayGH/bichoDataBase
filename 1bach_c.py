import urllib.request
import os

# Descargar la imagen
urllib.request.urlretrieve(
    (f'https://raw.githubusercontent.com/{user}/{repo}/{branch}/aver.png'),
    dir, "aver.png")
)
