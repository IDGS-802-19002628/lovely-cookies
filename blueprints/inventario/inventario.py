from flask import Blueprint, render_template
from .inventario_model import InventarioMP
from blueprints.mp.models import Mp
from config import db
import logging

# Configurar logging para ayudarte a depurar el código
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Crear un Blueprint para el inventario
inventario_bp = Blueprint("inventario", __name__, template_folder="templates")

# Ruta para el inventario
@inventario_bp.route('/inventario')
def inventario():
    # Realiza una consulta con INNER JOIN entre InventarioMP y MP
    resultado = get_inventario()
    
    # Registra la cantidad de resultados obtenidos
    logger.debug(f"Número de resultados de la consulta: {len(resultado)}")

    # Si hay resultados, también imprime el primer resultado para verificar los datos
    if resultado:
        logger.debug(f"Primer resultado de la consulta: {resultado[0]}")

    # Renderiza la plantilla con los datos de InventarioMP unidos a MP
    return render_template('inventario.html', inventario=resultado)

# Consulta con INNER JOIN para obtener datos de InventarioMP junto con datos de MP
def get_inventario():
    resultado = db.session.query(
        InventarioMP.idMateria,
        Mp.ingrediente,
        Mp.medicion,
        InventarioMP.existencias,
        InventarioMP.fecha_caducidad
    ).join(
        Mp,
        Mp.idMP == InventarioMP.idMP
    ).all()
    
    # Verifica los datos obtenidos
    if not resultado:
        logger.debug("La consulta no obtuvo resultados.")
    
    # Retorna los resultados obtenidos de la consulta
    return resultado
