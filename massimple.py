import mysql.connector
import pandas as pd
import numpy as np
import streamlit as st

uploaded_Simple = st.sidebar.file_uploader(
                        label="Solo cargar data__+Simple. (200MB max)",
                        type=['csv'])

global df
if uploaded_Simple is not None:
    #print(uploaded_file)
    #print("hello")
    with st.spinner('Procesando los datos...'):
        try:
            #Trouble = pd.read_excel(uploaded_file, engine="openpyxl", skiprows=3)

            df = pd.read_csv(uploaded_Simple, sep=',')
            #df = pd.read_csv('base_2.csv', sep=',')

            df = df[['ID ', 'Fecha de Creación', 'Tipo de nivel 1:', 'Titulo', 'Dueńo']]

            df = df.rename(columns={'ID ':'codreq','Fecha de Creación':'fec_regist','Tipo de nivel 1:':'desnomctr','Titulo':'desmotv','Dueńo':'LastModifiedBy'})

            df['codofcadm'] = ''
            df['desdtt'] = ''
            df['codcli'] = ''
            df['nomcli'] = ''
            df['numtelefvoip'] = ''
            df['desobsordtrab'] = ''
            df['tiptecnologia_x'] = 'GPON'
            df['codnod'] = ''
            df['CUSTOMERID_CRM__c'] = ''
            df['TELEFONO_REFERENCIA_1_CRM'] = ''
            df['servicioAfectado'] = ''

            df['Area_CRM'] = df['desnomctr']
            df['Categorization_Tier2'] = df['desnomctr']

            df['ESTADO']= 'PENDIENTE'
            df['GESTOR']= ''
            df['ACTIVO']= '0'
            df['LLAMADA']= '0'
            df['MENSAJE']= '0'

            df['FEC_PROG']= ''
            df['FEC_CERRAR']= ''
            df['ACCION']= ''
            df['OBS']= ''


            df = df[['codreq', 'fec_regist', 'desnomctr', 'desmotv', 'codofcadm', 'desdtt',
                'codcli', 'nomcli', 'numtelefvoip', 'desobsordtrab', 'tiptecnologia_x',
                'codnod', 'Area_CRM', 'Categorization_Tier2', 'LastModifiedBy',
                'CUSTOMERID_CRM__c', 'TELEFONO_REFERENCIA_1_CRM', 'servicioAfectado',
                'ESTADO', 'GESTOR', 'FEC_PROG', 'FEC_CERRAR', 'ACCION', 'OBS', 'ACTIVO',
                'LLAMADA', 'MENSAJE']]

            df = pd.DataFrame(df).astype(str)

            df['fec_regist'] = pd.to_datetime(df.fec_regist, errors = 'coerce').dt.strftime("%Y/%m/%d  %H:%M:%S")
            df["codreq"]=df["codreq"].apply(str)

            #print(string)
            ############################################ OCULTAR INFROMACION NO IMPORTANTE
            import warnings
            warnings.filterwarnings('ignore')
            #########################################3333
            #######
            ## TODO CONECTION A LA BASE DE DATOS MYSQL
            #######
            cnxn =  mysql.connector.connect( host="localhost",
                                            port="3306",
                                            user="root",
                                            passwd="CARDENAS47465810",
                                            db="bdtickets"
                                            )
            cursor = cnxn.cursor()

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


            df1 = nuevoee.columns
            matriz_np = np.array(df1)
            matriz_np = matriz_np.tolist()
            string = (str(matriz_np)[1:-1])
            characters = "'!?"
            colum = ''.join( x for x in string if x not in characters)

            #TODO Cargar data

            #######
            sql = f"""INSERT INTO bdtickets ({colum}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for row in nuevoee.values.tolist():
                cursor.execute(sql, tuple(row))
            cnxn.commit()


            cursor.close()
            cnxn.close()
            st.success("Se cargo la cantidad de: " +  str(len(nuevoee)))
            #print("Se cargo la cantidad de: " +  str(len(nuevoee)))

        except Exception as e:
            pass


            #time.sleep(6)


