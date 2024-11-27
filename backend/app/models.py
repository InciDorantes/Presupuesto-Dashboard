from .database import db

class FuenteFinanciamiento(db.Model):
    __tablename__ = 'fuentes_financiamiento'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    monto = db.Column(db.Float, nullable=False)

class CajaGasto(db.Model):
    __tablename__ = 'cajas_gasto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    total = db.Column(db.Float, default=0)

class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id = db.Column(db.Integer, primary_key=True)
    fuente_id = db.Column(db.Integer, db.ForeignKey('fuentes_financiamiento.id'), nullable=False)
    caja_id = db.Column(db.Integer, db.ForeignKey('cajas_gasto.id'), nullable=False)
    monto = db.Column(db.Float, nullable=False)

    # Relaciones
    fuente = db.relationship('FuenteFinanciamiento', backref='movimientos')
    caja = db.relationship('CajaGasto', backref='movimientos')
