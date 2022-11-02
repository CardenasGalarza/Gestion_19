import time
import mysql.connector
import pandas as pd
import gspread
import numpy as np
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings

from pyautogui import sleep
warnings.filterwarnings('ignore')
#########################################3333
gc = gspread.service_account(filename='datacargar-947843f340e2.json')
sh = gc.open("MASTER_GESTOR")
worksheet = sh.get_worksheet(0)
df = pd.DataFrame(worksheet.get_all_records())
df = df.replace({np.nan:None})
df["codreq"]=df["codreq"].apply(str)

print("Conexion de la data web Gpon")

#######
## TODO CONECTION A LA BASE DE DATOS MYSQL
#######
cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="b70d451b4ff985",
                                passwd="68b102d9",
                                db="heroku_9ca78643f8fb80d"
                                )
cursor = cnxn.cursor()
print("Conexion Listo a la base de datos MYSQL")

sql = "DELETE FROM bdtickets  WHERE ESTADO = 'PENDIENTE' AND GESTOR =''"
cursor.execute(sql)


sql = """
SELECT * FROM bdtickets ;
"""
#######
## TODO BASE DE DATOS MYSQL
#######
df1 = pd.read_sql(sql, cnxn)
df1["codreq"]=df1["codreq"].astype(str)
#print(len(df1))
#######
## TODO UNIR BASE DE DATOS MYSQL Y GOOGLE
#######
union = pd.concat([df, df1])
#print(len(union))
#######
## DE LA UNION BORRAR LOS DATOS DUPLICADOS Y QUEDARME SOLO CON LOS NUEVO TICKETS
#######
union2 = pd.concat([union, df1])
nuevoee = union2.drop_duplicates(subset=['codreq'], keep=False)
#AGREGAR 2 COLUMNAS
nuevoee['ESTADO']= 'PENDIENTE'
nuevoee['GESTOR']= ''
nuevoee['ACTIVO']= '0'
nuevoee['LLAMADA']= '0'

## TODO CONECTION A LA BASE DE DATOS MYSQL
#######
sql = """INSERT INTO bdtickets (codreq,fec_regist,desnomctr,desmotv,codofcadm,desdtt,codcli,nomcli,numtelefvoip,desobsordtrab,tiptecnologia_x,codnod,Area_CRM,Categorization_Tier2,LastModifiedBy,CUSTOMERID_CRM__c,TELEFONO_REFERENCIA_1_CRM,ESTADO,GESTOR,FEC_PROG,FEC_CERRAR,ACCION,OBS,ACTIVO,LLAMADA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
for row in nuevoee.values.tolist():
    cursor.execute(sql, tuple(row))
cnxn.commit()
cnxn.close()

print("Se cargo la cantidad de: " +  str(len(nuevoee)))

time.sleep(6)