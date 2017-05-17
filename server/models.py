from peewee import *

db = SqliteDatabase('sensor.db')

class Sensor(Model):
	id = PrimaryKeyField()
	air_humidity = TextField()
	earth_humidity = TextField()
	temperature = TextField()
	earth_temperature = TextField()
	class Meta:
		database = db

def initialize_db():
	db.connect()
	db.create_tables([Sensor],safe=True)
