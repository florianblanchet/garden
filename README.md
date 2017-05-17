# Jardin connecté 

### Client1 : Station météo <br/>
 Raspberry Pi reliée à un capteur qui mesure l'humidité et la température de l'air. Une LED est connectée, celle ci évolue progressivement du bleu au rouge en fonction du niveau d'humidité.

### Client2 : Station au sol <br/>
Raspberry Pi reliée à un capteur qui mesure l'humidité et la température du sol. Il contrôle un relais qui permet d'actionner une pompe pour arroser ou non les plantes. Un capteur de présence permet d'actionner un buzzer pour faire fuir les éventuels chats ou animaux qui s'approcheraient.<br/> <br/>

Les données des deux clients sont envoyées en Json au serveur via une requête http Post. <br/> <br/>

### Serveur web : <br/>
Le serveur est lancé sur une troisième raspberry pi connectée via ethernet à internet. Elle sert de point d'accés wifi pour les deux autres raspberry clients afin de créer un sous réseau. Il est relié à une base de donnée Sqlite qui stocke la température et l'humidité de l'air et du sol. Une page web permet d'afficher ces conditions en temps réel ainsi que l'état de la pompe. Un bouton permet d'actionner la pompe à tout moment. Le serveur demande à la station au sol d'activer la pompe si l'humidité est inférieure à 50%.