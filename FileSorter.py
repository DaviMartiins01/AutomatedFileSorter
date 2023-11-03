import os, shutil

path = r"C:/Users/davib/Documents/Mess/"

folder_names = ["ArquivosCSV", "ArquivosPNG", "ArquivosTXT"]

for loop in range(0, 3):
	if not os.path.exists(path + folder_names[loop]):
		os.makedirs(path + folder_names[loop])
