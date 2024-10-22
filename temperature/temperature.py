def konversisuhu(temperature, value): #mendefinisikan fungsi konversi suhu
    if value == 'C':# mengecek apakah suhunya menggunakan satuan celsius
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'#mengembalikan fungsi ke suhu celsius
    else:#mengalihkan perhitungan menggunakan fahrenheit jika tidak menggunakan celsius
        temperaturesuhu = (temperature * 9/5) * 32
        return temperaturesuhu, 'F'#menunjukkan hasil suhu fahrenheit

celsius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
print(f"{celsius_temperature}°C dikonversi ke fahrenheit adalah{temperaturesuhu}°{target_value}")
#mengkonversi nilai suhu celsius menjadi fahrenheit

fahrenhait_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenhait_temperature, 'C')
print(f"{fahrenhait_temperature}°F dikonversi ke Celsius adalah
      {temperaturesuhu}°{target_value}")
    #mengkonversi nilai suhu fahrenheit menjadi celsius