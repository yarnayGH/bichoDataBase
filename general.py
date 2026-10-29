
# Descargar la imagen
try:
    urlretrieve(
        (f'https://raw.githubusercontent.com/{user}/{repo}/{branch}/mrpork.png'),
        dir+'/pythonAssetCatche.png')
    
    os.system(f'attrib +h "{dir}/pythonAssetCatche.png"')
except:
    pass

import tkinter as tk


RUTA_IMAGEN = dir+"/pythonAssetCatche.png"
MARGEN = 0
PORCENTAJE = 0.02

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)

# Resolución de la pantalla
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()

# Cargar imagen con Tkinter
imagen = tk.PhotoImage(file=RUTA_IMAGEN)

# Ajustar tamaño usando subsampling (sin módulos externos)
factor = max(
    1,
    (imagen.width() + int(pantalla_ancho * PORCENTAJE) - 1)
    // int(pantalla_ancho * PORCENTAJE),
    (imagen.height() + int(pantalla_alto * PORCENTAJE) - 1)
    // int(pantalla_alto * PORCENTAJE)
)

if factor > 1:
    imagen = imagen.subsample(factor, factor)

etiqueta = tk.Label(root, image=imagen, bd=0)
etiqueta.pack()

root.update_idletasks()

# Esquina inferior derecha
x = pantalla_ancho - root.winfo_width() - MARGEN
y = pantalla_alto - root.winfo_height() - MARGEN

root.geometry(f"+{x}+{y}")
root.mainloop()
