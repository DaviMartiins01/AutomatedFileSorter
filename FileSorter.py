import os, shutil

path = r"C:/Users/davib/Documents/Projetos/AutomatedFileSorter"

file_name = os.listdir(path)

folder_names = ["ArquivosCSV", "ArquivosPNG", "ArquivosTXT"]

for loop in range(0, 3):
	if not os.path.exists(path + folder_names[loop]):
		os.makedirs(path + folder_names[loop])


for file in file_name:
	if ".csv" in file and not os.path.exists(path + "ArquivosCSV/" + file):
		shutil.move(path + file, path + "ArquivosCSV/" + file)

	elif ".png" in file and not os.path.exists(path + "ArquivosPNG/" + file):
		shutil.move(path + file, path + "ArquivosPNG/" + file)

	elif ".txt" in file and not os.path.exists(path + "ArquivosTXT/" + file):
		shutil.move(path + file, path + "ArquivosTXT/" + file)

	else:
		print("Alguns arquivos não foram movidos.")
