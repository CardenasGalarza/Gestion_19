
import gspread
import pandas as pd
from ftplib import FTP
import os


host = '10.226.44.223'
user = 'activadeco'
password = 'activa2015'


ftp = FTP(host, user, password)
#print('listp')
#print('yaa' + ftp.pwd() + "\n")
#ftp.dir();
ftp.cwd("averias")
ftp.retrlines("LIST")
names = ftp.nlst()
#print(names)
nombre_archivo = names[-1]
#print('ingreso' + ftp.pwd() + "\n")
#ftp.dir();

os.chdir("DESCARGA")

#nombre_archivo = "BT_Pendientes_20221126120201.txt"

abrir = open(nombre_archivo, 'wb')

#ftp.retrbinary("RETR" + nombre_archivo, abrir.write)
ftp.retrbinary('RETR %s' % nombre_archivo, abrir.write)
ftp.quit()
abrir.close()
#import shutil
#shutil.move(abrir, "DESCARGA")
from datetime import datetime
date = datetime.now()
tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


df = pd.DataFrame()
df['ARCHIVO'] = ['nombre_archivo']
df['FECHA_HR'] = tiempo

print(df)



gc = gspread.service_account(filename='datacargar-947843f340e2.json')
sh = gc.open("ARCHIVOS_CARGADOS_APPgestion19")

#  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
worksheet = sh.get_worksheet(0)

#cargar datos df
worksheet.update([df.columns.values.tolist()] + df.values.tolist())