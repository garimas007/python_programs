#data collection from various sensor (temp, humidity, pressure)
#analyze_sensor_data - sensor reading as i/p
#o/p - avg temp, max humidity, min pressure (seperate variables)

def analyze_sensor_data(temp, hum, prss):
    avg_temp = sum(temp)/len(temp)
    max_hum = max(hum)
    min_prss = min(prss)

    return avg_temp, max_hum, min_prss

temperatures = [25,20,35,40]
humidities = [70,68,72,75,69]
pressures = [100,200,800,300,400]
avg_temperature, max_humidity, min_pressure = analyze_sensor_data(temperatures, humidities, pressures)

print("avg temp :", avg_temperature)
print("max hum :" , max_humidity)
print("min press", min_pressure)
