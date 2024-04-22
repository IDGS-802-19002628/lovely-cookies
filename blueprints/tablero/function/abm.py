import os
import pandas as pd
import plotly.express as px
from blueprints.usuario.model_usuario import Usuario
from blueprints.venta.model_venta import VentaGalleta
from blueprints.receta.models import Galleta

class Dashboard:
    def guardar_dashboard(self):
        ventas = VentaGalleta.query.all()
        galletas = Galleta.query.all()
        
        lista1_ = []
        lista2_ = []
        lista_nombres_galletas = []  
        

        for venta in ventas:
            lista1_.append(venta.subTotal)
            lista2_.append(venta.cantidad)
         
            for galleta in galletas:
                if venta.idGalleta == galleta.idGalleta:  
                    lista_nombres_galletas.append(galleta.nombre)
                    break  
        
       
        df = pd.DataFrame({
            "Total de Ventas": lista1_,
            "Cantidad": lista2_,
            "Galletas": lista_nombres_galletas  
        })
        
        
        fig = px.bar(df, x="Total de Ventas", y="Cantidad", title="Gráfico de Ventas", color="Galletas")
        
      
        ruta_carpeta = os.path.join("blueprints", "tablero", "templates")
        os.makedirs(ruta_carpeta, exist_ok=True)  
        ruta_archivo = os.path.join(ruta_carpeta, "tablero.html")
        

        fig.write_html(ruta_archivo)
        
 
        enlace_html = f'<a class="btn btn-light border border-1" href="/menu"><i class="bx bx-chevron-left bx-sm align-middle"></i> Volver</a>'

  
        print("Haz clic en el siguiente enlace para descargar el tablero:")
        print(enlace_html)
