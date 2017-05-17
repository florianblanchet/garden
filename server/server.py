from flask import Flask,request, render_template, redirect, url_for
import json
import requests
from models import *

app = Flask(__name__)

activatee = 0

@app.before_request
def before_request():
	initialize_db()
	if (len(Sensor.select())==0): # Si base de donnée vide
		Sensor.create(
			air_humidity = 'init_air',
			earth_humidity = 'init_earth',
			temperature = 'init_temp',
			earth_temperature = 'init_tem_earth'
			)

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route('/',methods=['POST']) #Envoi de data par un des clients
def home():
	#data = request.data.decode()
	data = json.loads(request.data.decode())  #recupere le message envoye a notre chatbot
	#print(data)
	station = data['station'] # Données de quelle station
	condition = Sensor.select()
	for i in condition: # Affiche dernieres conditions
		print('Temp : '+i.temperature+'; Air_humidity : ' + i.air_humidity+'; Earth_humidity : ' + i.earth_humidity)
	if (station=='1'): # Weather station
		print('Conditions station meteo :')
		air_humidity = data['air_humidity']
		temperature = data['temperature']
		print(air_humidity)
		print(temperature)
		condition[0].air_humidity = air_humidity # Change la base de donnée
		condition[0].temperature = temperature
		condition[0].save()
		response = 'Bien reçu par le serveur'
	elif (station=='2'): # Earth Station
		print('Conditions station terre :')
		earth_humidity = data['earth_humidity']
		earth_temperature = data['earth_temperature']
		print(earth_humidity)
		print(earth_temperature)
		condition[0].earth_humidity=earth_humidity # Change la base de donnée
		condition[0].earth_temperature = earth_temperature		
		condition[0].save()
		print(activatee)
		if (int(earth_humidity)<50):
			response = 'activate'
			print('pompe activee automatiquement')
		elif (activatee==1):
			response = 'activate'
			global activatee 
			activatee = 0
			print('pompe activee manuellement')
		else :
			response = 'deactivate'
	print(response)	
	return response

@app.route('/',methods=['GET'])  #Demande de page web
def index():
	condition = Sensor.select()[0]
	if (int(condition.earth_humidity)<50):
		pump=True
	elif(activatee==1):
		pump=True
	else:
		pump=False
	return render_template('index.html',condition=condition,pump=pump)

@app.route('/activate/',methods=['POST'])
def activate():
	global activatee 
	activatee = 1
	#print (request.form['pompe'])
	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80) # Changer port mettre à 80
