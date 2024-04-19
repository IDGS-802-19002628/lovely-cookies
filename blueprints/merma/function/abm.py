from blueprints.venta.model_venta import InventarioG
from blueprints.merma.model_merma import Merma
from config import db
from blueprints.receta.models import Galleta



class GestionMerma:

    def guardar_merma(self, form, id_Usuario):
        producto = form.galleta.data
        cantidad = form.cantidad_m.data
        observacion = form.observaciones.data
        alert = ''
        messages = ''
        print(producto)
        id = id_Usuario
        nueva_merma = Merma(producto=producto,
                            cantidad=int(cantidad),
                            observacion=observacion,
                            id = int(id))
        print(nueva_merma.fecha)
        db.session.add(nueva_merma)
        db.session.commit()
        cambio_g = Galleta.query.filter_by(nombre=producto).first()
        cambio_i = InventarioG.query.filter_by(idGalleta=cambio_g.idGalleta).first()
        cantidad_db = cambio_i.cantidad
        if cantidad <= 0:
          alert = 'warning'
          messages = "No se puede realizar con envio de cantidad de {} merma".format(cantidad)
          return messages , alert
      
        if cantidad > cambio_i.cantidad:
          alert = 'warning'
          messages = "No se puede generar el registro de merma ya que es mayor al stock existente. ( Stock: {cantidad_db} y merma de envio {cantidad})".format(cantidad_db=cantidad_db, cantidad=cantidad)

          return messages , alert
        
        c = cambio_i.cantidad - cantidad
        cambio_i.cantidad = c
        db.session.add(cambio_i)
        db.session.commit()
        return messages, alert


