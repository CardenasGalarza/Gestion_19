import pyodbc
import pandas as pd
import gspread
import numpy as np
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
gc = gspread.service_account(filename='datacargar-947843f340e2.json')
sh = gc.open("MASTER_GESTOR")
worksheet = sh.get_worksheet(1)
df = pd.DataFrame(worksheet.get_all_records())
df = df.replace({np.nan:None})
df["names"]=df["names"].apply(str)
"""
dfa = pd.read_csv("data_nv.csv",sep=";")
dfd = pd.DataFrame(dfa)
df = dfd.astype(str)
import numpy as np

df = df.replace({np.nan:None})
#print(df)
"""
#######
## TODO CONECTION A LA BASE DE DATOS MYSQL
#######

server = 'us-cdbr-east-06.cleardb.net'
database = 'heroku_9ca78643f8fb80d'
username = 'b70d451b4ff985'
password = '68b102d9'
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print("listo")


sql = """
SELECT * FROM bduser ;
"""
#######
## TODO BASE DE DATOS MYSQL
#######
df1 = pd.read_sql(sql, cnxn)
df1["names"]=df1["names"].apply(str)
#print(df)

#######
## TODO UNIR BASE DE DATOS MYSQL Y GOOGLE
#######
union = pd.concat([df, df1]) 
#print(union)
#######
## DE LA UNION BORRAR LOS DATOS DUPLICADOS Y QUEDARME SOLO CON LOS NUEVO TICKETS
#######
nuevo = union.drop_duplicates(subset=['names'], keep=False)
#AGREGAR 2 COLUMNAS
#nuevo['ESTADO']= 'PENDIENTE'
#nuevo['GESTOR']= ''
#nuevo['ACTIVO']= '0'
#nuevo['LLAMADA']= '0'
print(nuevo)

#######
## TODO CARDEGAE LA DATA A MYSQL SOLO CASOS NUEVOS
#######
#print(nuevo)
### el values es para ver como esta los datos de sql server y poder ingresar 
for index, row in nuevo.iterrows():
     cursor.execute("INSERT INTO bduser (names,usernames,passwords) values(?,?,?)", 
                    row.names,
                    row.usernames,
                    row.passwords


 )
cnxn.commit()
cursor.close()
cnxn.close()
