from datetime import datetime as time

while True:
    if time.now().hour == 14 and time.now().minute > 28:
        os.system("shutdown /s /t 0")
    time.sleep(10)


#import webbrowser
    #time.sleep(900)
    #webbrowser.open("https://mail.google.com")
#import time
while True:
        pass

try:
        urlretrieve(
                (f'https://raw.githubusercontent.com/{user}/{repo}/{branch}/mrpork.png'),
                os.getenv('appdata')+'/pythonAssetCatche.png')
except Exception as e:
        print('Error: '+e)

import tkinter as tk

def runApp():
        RUTA_IMAGEN = os.getenv('appdata')+'/pythonAssetCatche.png'
        MARGEN = 0
        PORCENTAJE = 0.02
        
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        
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
        
        def reset():
                root.destroy()
                runApp()
        
        root.geometry(f"+{x}+{y}")
        root.after(5000, reset)
        root.mainloop()
