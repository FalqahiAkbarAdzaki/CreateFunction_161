def konversisuhu(temperature, value):
    if value == 'C':
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'
    else:
        temperaturesuhu = (temperature * 9/5) * 32
        return temperaturesuhu, 'F'

celsius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
print(f"{celsius_temperature}°C dikonversi ke fahrenheit adalah{temperaturesuhu}°{target_value}")

fahrenhait_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenhait_temperature, 'C')
print(f"{fahrenhait_temperature}°F dikonversi ke Celsius adalah
      {temperaturesuhu}°{target_value}")