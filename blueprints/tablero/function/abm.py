import os
import pandas as pd
import plotly.express as px
from blueprints.usuario.model_usuario import Usuario

class Dashboard:
    def guardar_dashboard(self,):
        
           
         
        df = pd.DataFrame({
            "A": [1,2,3,4,5],
            "B": [5,4,3,2,1]
        })
        fig = px.bar(df, x="A", y="B", title="Gráfico de Ventas")
        
        
        ruta_carpeta = os.path.join("blueprints", "tablero", "templates")
        os.makedirs(ruta_carpeta, exist_ok=True)  
        ruta_archivo = os.path.join(ruta_carpeta, "tablero.html")
        fig.write_html(ruta_archivo)
dash = Dashboard()
dash.guardar_dashboard()