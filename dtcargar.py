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
worksheet = sh.get_worksheet(0)
df = pd.DataFrame(worksheet.get_all_records())
df = df.replace({np.nan:None})
df["codreq"]=df["codreq"].astype(str)
"""
dfa = pd.read_csv("data_nv.csv",sep=";")
dfd = pd.DataFrame(dfa)
df = dfd.astype(str)
import numpy as np
df = df.replace({np.nan:None})
#print(df)
"""
#print(len(df))
#######
## TODO CONECTION A LA BASE DE DATOS MYSQL
#######
server = 'us-cdbr-east-06.cleardb.net'
database = 'heroku_9ca78643f8fb80d'
username = 'b70d451b4ff985'
password = '68b102d9'
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#print("listo")
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
#print(len(nuevoee))
#nuevoee.to_csv('cardenas.csv', sep=';')
#######
## TODO CARDEGAE LA DATA A MYSQL SOLO CASOS NUEVOS
#######
print(nuevoee)
### el values es para ver como esta los datos de sql server y poder ingresar 
for index, row in nuevoee.iterrows():
     cursor.execute("INSERT INTO bdtickets (codreq,fec_regist,desnomctr,desmotv,codofcadm,desdtt,codcli,nomcli,numtelefvoip,desobsordtrab,tiptecnologia_x,codnod,Area_CRM,Categorization_Tier2,LastModifiedBy,CUSTOMERID_CRM__c,TELEFONO_REFERENCIA_1_CRM,ESTADO,GESTOR,FEC_PROG,FEC_CERRAR,ACCION,OBS,ACTIVO,LLAMADA) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                    row.codreq,
                    row.fec_regist,
                    row.desnomctr,
                    row.desmotv,
                    row.codofcadm,
                    row.desdtt,
                    row.codcli,
                    row.nomcli,
                    row.numtelefvoip,
                    row.desobsordtrab,
                    row.tiptecnologia_x,
                    row.codnod,
                    row.Area_CRM,
                    row.Categorization_Tier2,
                    row.LastModifiedBy,
                    row.CUSTOMERID_CRM__c,
                    row.TELEFONO_REFERENCIA_1_CRM,
                    row.ESTADO,
                    row.GESTOR,
                    row.FEC_PROG,
                    row.FEC_CERRAR,
                    row.ACCION,
                    row.OBS,
                    row.ACTIVO,
                    row.LLAMADA

 )
cnxn.commit()
cursor.close()
cnxn.close()
