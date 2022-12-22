from flask import Flask, request, jsonify


import skfuzzy as fuzz
from skfuzzy import control as ctrl


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import skfuzzy as fuzz


app = Flask(__name__)



@app.route('/processjson', methods=['POST'])
def processjson():

        
    # Humidity from 0 to 100 percent
    humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')

    # Temperature from 0 to 40 celcius degrees - we assume this plant is in the house
    temperature = ctrl.Antecedent(np.arange(0, 40, 1), 'temperature')


    # Water amount a plant needs per day given all the conditions
    water_amount = ctrl.Consequent(np.arange(0, 120, 1), 'water_amount')

    # Automatically split water_need and water_amount on 3 categories low, medium, max

    water_amount.automf(5)

    # We define rules for humidity if it's dry, optimal, humid
    humidity['dry'] = fuzz.trimf(humidity.universe, [0, 10, 20])
    humidity['optimal'] = fuzz.trimf(humidity.universe, [20, 40, 60])
    humidity['humid'] = fuzz.trimf(humidity.universe, [60, 80, 100])

    # Temperature has more levels as it matters more for plant
    temperature['cold'] = fuzz.trimf(temperature.universe, [0, 5, 20])
    temperature['optimal'] = fuzz.trimf(temperature.universe, [15, 25, 30])
    temperature['warm'] = fuzz.trimf(temperature.universe, [25, 35, 40])


    # We define set of rules

    rule1 = ctrl.Rule(humidity['dry'] & temperature['cold'], water_amount['average'])
    rule2 = ctrl.Rule(humidity['dry'] & temperature['optimal'], water_amount['average'])
    rule3 = ctrl.Rule(humidity['dry'] & temperature['warm'], water_amount['good'])

    rule4 = ctrl.Rule(humidity['optimal'] & temperature['cold'], water_amount['poor'])
    rule5 = ctrl.Rule(humidity['optimal'] & temperature['optimal'], water_amount['average'])
    rule6 = ctrl.Rule(humidity['optimal'] & temperature['warm'], water_amount['good'])

    rule7 = ctrl.Rule(humidity['humid'] & temperature['cold'], water_amount['poor'])
    rule8 = ctrl.Rule(humidity['humid'] & temperature['optimal'], water_amount['poor'])
    rule9 = ctrl.Rule(humidity['humid'] & temperature['warm'], water_amount['average'])





    # Set rules needed to operate the fuzzy logic
    water_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

    # Add the simulation to control system
    water = ctrl.ControlSystemSimulation(water_ctrl)

    #req_data = request.get_json()
    humidity = request.json['humid']
    temperature = request.json['temp']

    #return '{}'.format(humidity+temperature)

    water.input['humidity'] = humidity
    water.input['temperature'] = temperature
  
    water.compute()
   
    
    return jsonify( water.output['water_amount'])







if __name__ == '__main__':
    app.run(debug=True, port=5000)
