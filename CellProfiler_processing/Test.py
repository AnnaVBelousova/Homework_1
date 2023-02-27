import os


path_dir = "C:\\Users\\Arteys\\Desktop\\Anya_work\\Insulin_Alexa_488_Glucagon_TexasRed\\" # ссылка на самую верхнюю папку

for address, dirs, files in os.walk(path_dir): # выдает адрес папки , подпапки или файла в оторой что-то лежит  
    for file in files:
        if ".csv" in str(file):
            full_path = os.path.join(address, file)
    print(os.path.join(address, file))
