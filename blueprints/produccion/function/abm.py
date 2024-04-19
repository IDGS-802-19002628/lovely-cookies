
from blueprints.mp.models import Mp
from blueprints.venta.model_venta import InventarioG
from blueprints.receta.models import Galleta, Receta
from blueprints.receta.recetas import recetas_bp
from ..model_produccion import Produccion, db


class Gestorproduccion:
    def guardar_produccion(self, form_pro):
        lista_ = []
        galleta = form_pro.galleta.data
        produccion = int(200)
        fecha = form_pro.fecha.data
        estatus = 'pendiente'
        #Recetas, invetario_materia invetario_g
        galleta = Galleta.query.filter(Galleta.nombre == galleta).first()
        inventario_in = InventarioG.query.filter(InventarioG.idGalleta == galleta.idGalleta).first()
        ingre = Receta.query.filter_by(idGalleta=inventario_in.idGalleta).all()
        print(ingre)
        print('prueba')
        incremento = inventario_in.cantidad + produccion
        
        incremento = inventario_in.cantidad + produccion
        inventario_in.cantidad = incremento
        db.session.add(inventario_in)
        db.session.commit()
        nueva_Produccion = Produccion(nombre=galleta,
                                cantidad=produccion,
                                create_date=fecha,
                                estatus=estatus)
        db.session.add(nueva_Produccion)
        db.session.commit()
        messages = "La producción ha sido registrada exitosamente."
        alert = 'success'
        return messages, alert
    def obtener_produccion(self):
         b = Produccion.query.all()
         return b
    def modificar_produccion(self, id_produccion, form_pro, method):
         produccion_a_modificar = {}
         id = 0
         if method == 'GET':
           produccion_a_modificar = Produccion.query.filter(Produccion.id == id_produccion).first()
           form_pro.id.data = produccion_a_modificar.id
           form_pro.cantidad.data = produccion_a_modificar.cantidad
           form_pro.galleta.data = produccion_a_modificar.nombre
           form_pro.estatus.data = produccion_a_modificar.estatus
           form_pro.fecha.data = produccion_a_modificar.create_date
         if method == 'POST':
           print('Entro')
           id = form_pro.id.data
           produccion_a_modificar = Produccion.query.filter(Produccion.id == id).first()
           if not form_pro.cantidad.data :
             produccion_a_modificar.nombre = form_pro.galleta.data
             produccion_a_modificar.create_date = form_pro.fecha.data
           else:
             produccion_a_modificar.cantidad = form_pro.cantidad.data
             produccion_a_modificar.nombre = form_pro.galleta.data
             produccion_a_modificar.create_date = form_pro.fecha.data
             produccion_a_modificar.estatus =  form_pro.estatus.data
           db.session.add(produccion_a_modificar)
           db.session.commit()
         alert = 'success' 
         messages = "Se a actualizado la produccion de galletas de {}".format(produccion_a_modificar.nombre)
         return messages, form_pro, alert