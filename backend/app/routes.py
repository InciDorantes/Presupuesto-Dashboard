from flask import Blueprint, request, jsonify
from .models import FuenteFinanciamiento, CajaGasto, Movimiento
from .database import db

main = Blueprint('main', __name__)

@main.route('/fuentes', methods=['GET'])
def get_fuentes():
    fuentes = FuenteFinanciamiento.query.all()
    return jsonify([{'id': f.id, 'nombre': f.nombre, 'monto': f.monto} for f in fuentes])

@main.route('/cajas', methods=['GET'])
def get_cajas():
    cajas = CajaGasto.query.all()
    return jsonify([{'id': c.id, 'nombre': c.nombre, 'total': c.total} for c in cajas])

@main.route('/movimiento', methods=['POST'])
def crear_movimiento():
    data = request.json
    fuente_id = data['fuente_id']
    caja_id = data['caja_id']
    monto = data['monto']

    # Actualizar monto de la fuente
    fuente = FuenteFinanciamiento.query.get(fuente_id)
    if fuente.monto < monto:
        return jsonify({'error': 'Fondos insuficientes'}), 400
    fuente.monto -= monto

    # Actualizar total de la caja
    caja = CajaGasto.query.get(caja_id)
    caja.total += monto

    # Crear el movimiento
    movimiento = Movimiento(fuente_id=fuente_id, caja_id=caja_id, monto=monto)
    db.session.add(movimiento)
    db.session.commit()

    return jsonify({'message': 'Movimiento registrado con éxito'})
