from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class lots(db.Model):
        lot_id = db.Column(db.Integer, primary_key=True)
        lot_name = db.Column(db.String, nullable=True)
        farm_id = db.Column(db.Integer, nullable=True)
        weather_id = db.Column(db.Integer, nullable=True)
    
        def __repr__(self):
            return '<lots {}>'.format(self.lot_name)

class measure_types(db.Model):
        measure_id = db.Column(db.Integer, primary_key=True)
        measure_name = db.Column(db.String, nullable=True)
        
        def __repr__(self):
            return '<measure_types {}>'.format(self.measure_name)

class roasters(db.Model):
        roaster_id = db.Column(db.Integer, primary_key=True)
        roaster_name = db.Column(db.String, nullable=True)
            
        def __repr__(self):
            return '<roasters {}>'.format(self.roaster_name)

class roastings(db.Model):
        roasting_id = db.Column(db.Integer, primary_key=True)
        cause_name = db.Column(db.String, nullable=True)
        place_name = db.Column(db.String, nullable=True)
        start_dttm = db.Column(db.DateTime, nullable=False)
        end_dttm = db.Column(db.DateTime, nullable=False)
        initial_weight_val = db.Column(db.Float, nullable=False)
        lot_id = db.Column(db.Integer, nullable=False)
        acidity_val = db.Column(db.Float, nullable=True)
        roasters_roaster_id = db.Column(db.Integer, nullable=False)

        def __repr__(self):
            return '<roastings {} {} {}>'.format(self.cause_name, self.place_name, self.start_dttm)

class temperature(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        measure_id = db.Column(db.Integer, nullable=False)
        roasting_id = db.Column(db.Integer, nullable=False)
        timestamp_num = db.Column(db.Integer, nullable=True)
        temperature_val = db.Column(db.Float, nullable=True)
        
        def __repr__(self):
            return '<temperature> {}>'.format(self.id)
