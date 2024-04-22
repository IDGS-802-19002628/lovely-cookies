
from blueprints.mp.models import Mp
from blueprints.venta.model_venta import InventarioG
from blueprints.receta.models import Galleta, Receta
from blueprints.receta.recetas import recetas_bp
from blueprints.inventario_mp.models import Inventariomp
from ..model_produccion import Produccion, db


class Gestorproduccion:
    def guardar_produccion(self, form_pro):
        
        lista_cantidad = []
        lista_idMp = []
        galleta = form_pro.galleta.data
        produccion = int(200)
        fecha = form_pro.fecha.data
        estatus = 'pendiente'
        #Recetas, invetario_materia invetario_g
        if estatus == 'pendiente' or estatus == 'terminado':
          galleta = Galleta.query.filter(Galleta.nombre == galleta).first()
          nueva_Produccion = Produccion(nombre=galleta.nombre,
                                cantidad=produccion,
                                create_date=fecha,
                                estatus=estatus)
          db.session.add(nueva_Produccion)
          db.session.commit()
          messages = "La producción ha sido registrada exitosamente."
          alert = 'success'
          print('entro en la validacion de producción')
          return messages, alert
        galleta = Galleta.query.filter(Galleta.nombre == galleta).first()
        print(galleta.idGalleta)
        inventario_in = InventarioG.query.filter(InventarioG.idGalleta == galleta.idGalleta).first()
        print(inventario_in)
        if inventario_in.cantidad is 'NoneType':
          print('prueba produccion')
          incremento = produccion
        receta_d = Receta.query.filter(Receta.idGalleta == inventario_in.idGalleta).all()
        print(receta_d)
        for r in receta_d:
           val = r.cantidad * produccion
           inventario_d = Inventariomp.query.filter(Inventariomp.idMP == r.idMP).first()
           rd = inventario_d.existencias - val  
           inventario_d.existencias = rd
           db.session.add(inventario_d)
           db.session.commit()
           lista_cantidad.append(val)
           print(lista_cantidad)
         
        incremento = inventario_in.cantidad + produccion
        inventario_in.cantidad = incremento
        db.session.add(inventario_in)
        db.session.commit()
        nueva_Produccion = Produccion(nombre=galleta.nombre,
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
         inventario_in ={}
         galleta={}
         receta_d={}
         m =""
         id = 0
         produccion_a_modificar = Produccion.query.filter(Produccion.id == id_produccion).first()
         if method == 'GET':
           
             
           form_pro.id.data = produccion_a_modificar.id
           form_pro.g.data = produccion_a_modificar.nombre
           form_pro.estatus.data = produccion_a_modificar.estatus
           form_pro.fecha.data = produccion_a_modificar.create_date
         if method == 'POST':
           print('Entro')
           id = form_pro.id.data
           produccion_a_modificar = Produccion.query.filter(Produccion.id == id).first()
           print("pro m", produccion_a_modificar)
           if  form_pro.cantidad.data is None:
             print('prueba de cantidad')

             form_pro.cantidad.data = produccion_a_modificar.cantidad
             
           if  form_pro.cantidad.data <= 0:
             print('prueba')
             messages = 'No se puede producir la cantidad: {}.'.format(form_pro.cantidad.data)
             alert = 'warning'
             return messages, form_pro, alert
           if form_pro.cantidad.data == 'terminado':
             produccion_a_modificar.estatus =  form_pro.estatus2.data
             db.session.add(produccion_a_modificar)
             db.session.commit()
             alert = 'success' 
             messages = "Se a actualizado la produccion de {}".format(produccion_a_modificar.nombre)
             return messages, form_pro, alert
           if form_pro.estatus2.data == 'proceso':
             galleta = Galleta.query.filter(Galleta.nombre == produccion_a_modificar.nombre).first()
             print(galleta.idGalleta)
             inventario_in = InventarioG.query.filter(InventarioG.idGalleta == galleta.idGalleta).first()
             print(inventario_in.cantidad)
             receta_d = Receta.query.filter(Receta.idGalleta == inventario_in.idGalleta).all()
             
             print(receta_d)
             for r in receta_d:
              val = (r.cantidad * form_pro.cantidad.data)/form_pro.cantidad.data
              inventario_d = Inventariomp.query.filter(Inventariomp.idMP == r.idMP).first()
              inre = Mp.query.filter(Mp.idMP == r.idMP).first()
              if val > inventario_d.existencias :
                alert = 'warning' 
                messages = "No se puede hacer la produccion de esta receta por que no hay suficiente {}".format(inre.ingrediente)
                return messages, form_pro, alert
              m = "prueba de produccion {}".format(m)
              
              inventario_d = Inventariomp.query.filter(Inventariomp.idMP == r.idMP).first()
              rd = inventario_d.existencias - val  
              inventario_d.existencias = rd
              db.session.add(inventario_d)
              db.session.commit()
             
             produccion_a_modificar.cantidad = produccion_a_modificar.cantidad + form_pro.cantidad.data
             inventario_c = InventarioG.query.filter(InventarioG.idGalleta == r.idMP).first()
             inventario_c.cantidad = produccion_a_modificar.cantidad
             db.session.add(inventario_c)
             db.session.commit()
             produccion_a_modificar.estatus =  form_pro.estatus2.data
             db.session.add(produccion_a_modificar)
             db.session.commit()
             alert = 'success' 
             messages = "Se a actualizado la produccion de {}".format(produccion_a_modificar.nombre)
             return messages, form_pro, alert
         alert = 'success' 
         messages = "Se a actualizado la produccion de {}".format(produccion_a_modificar.nombre)
         return messages, form_pro, alert
