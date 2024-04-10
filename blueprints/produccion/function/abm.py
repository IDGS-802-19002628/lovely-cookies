from ..model_produccion import Produccion, db


class Gestorproduccion:
    def guardar_produccion(self, form_pro):
        galleta = form_pro.galleta.data
        produccion = int(200)
        fecha = form_pro.fecha.data
        estatus = 'processo'
        
        nueva_Produccion = Produccion(nombre=galleta,
                                cantidad=produccion,
                                create_date=fecha,
                                estatus=estatus)
        db.session.add(nueva_Produccion)
        db.session.commit()
        messages = "Se a registrado la produccion"
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
           form_pro.galleta.data = produccion_a_modificar.galleta
           form_pro.fecha.data = produccion_a_modificar.create_date
         if method == 'POST':
           print('Entro')
           id = form_pro.id.data
           produccion_a_modificar = Produccion.query.filter(Produccion.id == id).first()
           if not form_pro.pwd.data:
             produccion_a_modificar.nombre = form_pro.nombre.data
             produccion_a_modificar.create_date = form_pro.fecha.data
             
           else:
             produccion_a_modificar.nombre = form_pro.nombre.data
             produccion_a_modificar.create_date = form_pro.fecha.data
             
           db.session.add(produccion_a_modificar)
           db.session.commit()
         alert = 'success' 
         messages = "Se a actualizado la produccion {}".format(produccion_a_modificar.nombre)
         return messages, form_pro, alert