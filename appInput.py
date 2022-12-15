
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
#from soupsieve import select  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
############################################ OCULTAR INFROMACION NO IMPORTANTE
import base64
import mysql.connector
from mysql.connector import Error
#import pyodbc
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
##########################
import time
from datetime import datetime
from datetime import timedelta
import gspread
import re
#import pyautogui


st.set_page_config(page_title='bdtickets-Averias', page_icon="🌀", layout='centered', initial_sidebar_state='auto')

## borrar nombres de la pagina
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()
#st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
# --- USER AUTHENTICATION ---
names = ['Giancarlos Cardenas', 'Genesis Medrano', 'Luis Llerena', 'DIANA BERNEDO', 'VIVIAN CERVERA', 'CAROL CHUNGA', 'LAURA VIERA', 'MERCEDES RAYMUNDO', 'MONTES CABANILLAS', 'RENZO RIMARACHIN', 'LORENA BENAVIDES', 'NANCY YEREN', 'GIULIANA BELLIDO', 'CARMEN HUAMANCHUMO', 'GABRIEL SANTA ANA', 'CARMEN POMA REYES', 'JOSE ECHEVARRIA', 'YORMAN MORI', 'ENZO PAULINO', 'GUSTAVO SALCEDO', 'KAREN MAYORCA', 'LESLIE PRUDENCIO', 'BARBARA HUAMANCHUMO', 'Jose Ricardo', 'Eber Hinostroza', 'Bot cardenas', 'YERSON HINOSTROZA', 'Roberto Faustor', 'John Jairo Bravo', 'Mauro Arturo Garcia']
usernames = ['Cardenas', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot', 'YERSON', 'Roberto', 'jbravob', 'Mauroar']

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")
#print(username)
#### fondo al costado
def sidebar_bg(side_bg):
   side_bg_ext = 'jpg'
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'nooa.jpg'
sidebar_bg(side_bg)


st.markdown(
    """
    <style>

    header .css-1595djx e8zbici2{
    display: flex;
    flex-direction: column;
    align-items: center;
    }

    header .logo-text{
        margin: 0;
        padding: 10px 26px;
        font-weight: bold;
        color: rgb(60, 255, 0);
        font-size: 0.8em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# para los botones horizontal
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)



if authentication_status == False:
    st.error("Username/password is incorrect")

        ## borrar nombres de la pagina
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if authentication_status == None:
    st.warning("Please enter your username and password")

        ## borrar nombres de la pagina
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


    st.markdown(
        """
        <style>

        header .css-1595djx e8zbici2{
        display: flex;
        flex-direction: column;
        align-items: center;
        }

        header .logo-text{
            margin: 0;
            padding: 10px 26px;
            font-weight: bold;
            color: rgb(60, 255, 0);
            font-size: 0.8em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # para los botones horizontal
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)



    st.markdown(
        f"""
        <header class="css-1595djx e8zbici2">
            <p class="logo-text">App Alarmas 👨🏻‍💻Giancarlos .C</p>
        </header>
        """,
        unsafe_allow_html=True
    )

    def hide_anchor_link():
        st.markdown("""
            <style>
            .css-15zrgzn {display: none}
            .css-eczf16 {display: none}
            .css-jn99sy {display: none}
            </style>
            """, unsafe_allow_html=True)
    texto  = ('🔒Estamos mejorando la privacidad de la información, si aún no cuentas con tus credenciales, comunicarte con:')
    st.caption( f'<h6 style="color:#FFFFFF;">{texto}</h6>', unsafe_allow_html=True )

    textoo = ('\n\n👨🏻‍💻Luis Llerena. \n\n👨🏻‍💻Giancarlos Cardenas.')
    st.caption( f'<h6 style="color:#FFFFFF;">{textoo}</h6>', unsafe_allow_html=True )
    ###
    ####
    ####
    ####
    ######



if authentication_status:
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Bienvenid@ {name}")
    #### fondo al costado



    # 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
    EXAMPLE_NO = 1


    def streamlit_menu(example=1):
        if example == 1:
            # 1. as sidebar menu
            with st.sidebar:
                selected = option_menu(
                    menu_title="Main Menu",  # required
                    options=["CargarDt", "Projects", "Contact"],  # required
                    icons=["house", "book", "envelope"],  # optional
                    menu_icon="cast",  # optional
                    default_index=0,  # optional
                )
            return selected

        if example == 2:
            # 2. horizontal menu w/o custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["CargarDt", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
            )
            return selected

        if example == 3:
            # 2. horizontal menu with custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["CargarDt", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                },
            )
            return selected

    selected = streamlit_menu(example=EXAMPLE_NO)

    if selected == "CargarDt":
        #st.title(f"You have selected {selected}")
        st.title("CARGAR DATOS GESTION⌚")

        # Add a sidebar
        st.sidebar.subheader("Cargar datos de acuerdo a lo requerido")

                # Setup file upload
        uploaded_file = st.sidebar.file_uploader(
                                label="Solo cargar data TT y CMR. (200MB max)",
                                type=['csv', 'xlsx', 'XLS'])

        global df
        if uploaded_file is not None:
            #print(uploaded_file)
            #print("hello")

            with st.spinner('Procesando los datos...'):
                try:
                    Trouble = pd.read_excel(uploaded_file, engine="openpyxl", skiprows=3)
                    ######3######################
                    Troubledt=Trouble[["Incident Number",	"Area_CRM",	"Categorization Tier 2", "Last Modified By", "CUSTOMERID_CRM__c", "TELEFONO_REFERENCIA_1_CRM","servicioAfectado"]]
                    Troubledt["servicioAfectado"] = Troubledt["servicioAfectado"].replace({'broadband':'internet', 'landline':'telef fijo'}, regex=True)
                    Troubledt.rename(columns={'Incident Number': 'codreq'}, inplace=True)
                    Troubledt = Troubledt.drop_duplicates(subset=['codreq'])
                    Troubledt = Troubledt.astype("string")
                    Troubledt = Troubledt.fillna('')
                    gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                    sh = gc.open("DT_PEDIR_COLUM")
                    #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                    worksheet = sh.get_worksheet(0)
                    #borrar datos total y dejar encabezado
                    worksheet.resize(rows=1)
                    worksheet.resize(rows=30)
                    #cargar datos df
                    worksheet.update([Troubledt.columns.values.tolist()] + Troubledt.values.tolist())
                    ################################################################
                    ################################################################

                    datos = {
                        'CONTRATA_TOA__c': ['ANALISIS DE RUIDO PEX','ANOVO','CABECERA','COBRA','COMFICA','CUARENTENA COE','DOMINION','ENERGIA','EZENTIS','FIBRA','GAC-VOIP','INGENIERIA HFC',
                                'LARI','LITEYCA','TRABAJOS PROGRAMADOS','TRANSMISIONES','TRATAMIENTO INTERMITENCIA','TRIAJE HFC','TRATAMIENTO CALL PIN TV-M1'],
                        'codctr' : ['485','333','60','15','363','429','335','211','19','209','353','435','245','470','365','210','483','474','434']
                    }
                    df = pd.DataFrame(datos)
                    #print(df)
                    datos2 = {
                        'Categorization Tier 3': ['Control Remoto'],
                        'codmotv' : ['I129']
                    }
                    df2 = pd.DataFrame(datos2)
                    #print(df2)

                    
                    Trouble=Trouble[['Incident Number','CREATION_DATE_CRM__c','Tipo de incidencia padre','CONTRATA_TOA__c','Categorization Tier 3','CUSTOMER_NAME_CRM__c',
                    'OBSERVATIONS_CRM__c','STREETTYPE_CRM__c','STREETNAME_CRM__c','STREETNUMBER_CRM__c','SUBUNITTYPE_CRM__c','DEPARTMENT_CRM','DISTRICT_CRM__c',
                    'Network Technology__c','LEX_NIL__c','BORNE_NIL__c','TROBA_ TYPE_NIL__c','TAP_STREET_NIL__c','PLANE_OLT_PORT','NODE_HFC_OLT_HOSTNAME',
                    'currentVozTelephone_OMS__c','currentVozProduct_OMS__c','currentVozServiceTechnology_OMS__c','currentBafAccessid_OMS__c','CFS_SERVICE_TECHNOLOGY_NIL__c'
                    ]]
                    #<<------------------------->>
                    #comvertir año 1070-01-01 con  FECHA REAL
                    Trouble['CREATION_DATE_CRM__c'] = pd.to_datetime(Trouble['CREATION_DATE_CRM__c'], errors='coerce', unit='d', origin='1899-12-30')
                    Trouble['CREATION_DATE_CRM__c'] = pd.to_datetime(Trouble.CREATION_DATE_CRM__c, errors = 'coerce').dt.strftime("%Y/%m/%d  %H:%M:%S")
                    #concatenated_df=pd.concat([Trouble,cms],ignore_index=True)
                    union1 = pd.merge(left=Trouble,right=df, how='left', left_on='CONTRATA_TOA__c', right_on='CONTRATA_TOA__c')
                    union2 = pd.merge(left=union1,right=df2, how='left', left_on='Categorization Tier 3', right_on='Categorization Tier 3')
                    Trouble2=union2[['Incident Number','CREATION_DATE_CRM__c','Tipo de incidencia padre','codctr','CONTRATA_TOA__c','codmotv','Categorization Tier 3','CUSTOMER_NAME_CRM__c',
                    'OBSERVATIONS_CRM__c','STREETTYPE_CRM__c','STREETNAME_CRM__c','STREETNUMBER_CRM__c','SUBUNITTYPE_CRM__c','DEPARTMENT_CRM','DISTRICT_CRM__c',
                    'Network Technology__c','LEX_NIL__c','BORNE_NIL__c','TROBA_ TYPE_NIL__c','TAP_STREET_NIL__c','PLANE_OLT_PORT','NODE_HFC_OLT_HOSTNAME',
                    'currentVozTelephone_OMS__c','currentVozProduct_OMS__c','currentVozServiceTechnology_OMS__c','currentBafAccessid_OMS__c','CFS_SERVICE_TECHNOLOGY_NIL__c'
                    ]]
                    Trouble2["CFS_SERVICE_TECHNOLOGY_NIL__c"] = Trouble2["CFS_SERVICE_TECHNOLOGY_NIL__c"].replace({'VOIP':'VOZ','GPON':'DATOS','CATV':'TV','DOCSIS':''}, regex=True)
                    Trouble2 = Trouble2.rename(columns={'CFS_SERVICE_TECHNOLOGY_NIL__c':'BORRAR',})
                    Trouble2.columns = ['codreq','fec_regist','codedo','codctr','desnomctr','codmotv','desmotv','nomcli','desobsordtrab','destipvia','desnomvia','numvia','destipurb','codofcadm',
                    'desdtt','tiptecnologia','codtap','codbor','codtrtrn','desurb','nroplano','codnod','numtelefvoip','codpromo','tiplinea','codcli','BORRAR']
                    Trouble2['AVERIAS']='Trouble'


                    Trouble2['fec_regist'] = pd.to_datetime(Trouble2.fec_regist, errors = 'coerce').dt.strftime("%Y/%m/%d  %H:%M:%S")
                    Trouble2 = Trouble2.fillna('')

                    gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                    sh = gc.open("DT_AVERIAS_Trouble")

                    #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                    worksheet = sh.get_worksheet(0)

                    #borrar datos total y dejar encabezado
                    worksheet.resize(rows=1)
                    worksheet.resize(rows=30)
                    #cargar datos df
                    worksheet.update([Trouble2.columns.values.tolist()] + Trouble2.values.tolist())

                    # ver datos de google sheet
                    #dataframe = pd.DataFrame(worksheet.get_all_records())
                    #print(dataframe)





                    st.write("SER CARGO CON EXITO Trouble Tickets")
                    #st.write(df)
                    # para ver la cantidad de registros
                    total = str(len(Trouble2))
                    st.success('Total de '+total+' Registros')

                except Exception as e:
                    print(e)
                    gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                    sh = gc.open("DT_AVERIAS_Trouble")
                    #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                    worksheet = sh.get_worksheet(0)
                    Trouble2 = pd.DataFrame(worksheet.get_all_records())
                    #print(Trouble2)
                    #Trouble2 = pd.read_csv('AVERIAS/DT_AVERIAS_Trouble.csv',sep=',')
                    warnings.simplefilter("ignore")
                    df = pd.read_excel(uploaded_file, dtype=str, engine='xlrd')
                    

                    cms=df[['codreq','fec_regist','codedo','codctr','desnomctr','codmotv','desmotv','nomcli','desobsordtrab','destipvia','desnomvia','numvia','destipurb','codofcadm',
                    'desdtt','tiptecnologia','codtap','codbor','codtrtrn','desurb','nroplano','codnod','numtelefvoip','codpromo','tiplinea','codcli'
                    ]]
                    
                    # para ver la cantidad de registros
                    total = str(len(cms))
                    st.success('CMS total de '+total+' Registros')

                    cms['AVERIAS']='CMS'
                    cms['BORRAR']=''
                    cms=pd.concat([Trouble2,cms],ignore_index=True)
                    #cms.to_csv('borrarrrr.csv',index=False, sep=";")
                    #print(cms)
                    profesiones=["DECO","TV","SEÑAL","TARJETA","REMOTO","CONTROL","CABLE","CANAL","HD","PIX","VISUA","PANTALL"]
                    cond=[cms['desobsordtrab'].str.contains(profesion,case=False).fillna(False) for profesion in profesiones]
                    cms['TV']=np.select(cond,profesiones,default = '')
                    profesiones=["NAVE","LENT","CORTE","INTER","POTEN","WI","IP","VELOC","NAT","DUO","TRIO","PARAM","TAP","ELECT","LEVAN","EGA","SPEED","ERNET","MASIV",
                    "LLEGA","SEÑA","SERVI","MODEM","LUCES","ROUT","CONECT","SRN","DOWN","REPET","NIVEL","RNET","NAEV","NAV","OFFLINE","SATURAC","MODEN",
                    "CLIENTE ACTIVO","RECOMIE","RUTINA","TRIAJE","SATUR","SNR","ANULAC","MAISVA","CLEAR","PEX","PAQUET","MASVIA","SIVA","MASVI","AMP","SE TRANS",
                    "INFANC","UP","M´DEM","MÓDEM","PORTADO","TOA","NVGA","PUERTO"]
                    cond=[cms['desobsordtrab'].str.contains(profesion,case=False).fillna(False) for profesion in profesiones]
                    cms['DATOS']=np.select(cond,profesiones,default = '')
                    profesiones=["LINEA","VOZ","VOLUMEN","TELEFO","LLAMA","FIJ","LOCU","RECIB","FONO","SALID","VOIP","CASILLA","TLF","REGISTR","REALIZA","LLAMDAS","MUERTA","MUERTO",
                    "TONO","MULTIDESTINO","LLMAR","TELF","IDENTIF","RUIDO","ESCUCHA"]
                    cond=[cms['desobsordtrab'].str.contains(profesion,case=False).fillna(False) for profesion in profesiones]
                    cms['VOZ']=np.select(cond,profesiones,default = '')
                    profesiones=["NAT","JUEGO","CAMARA","PUERTO","CAMBIO IP","CAMBIO DE IP","SERVIDOR"]
                    cond=[cms['desobsordtrab'].str.contains(profesion,case=False).fillna(False) for profesion in profesiones]
                    cms['CAMBIO_IP']=np.select(cond,profesiones,default = '')
                    #CAMBIAR todo lo encontrado y poner por puerto
                    cms['CAMBIO_IP'] = cms['CAMBIO_IP'].replace(profesiones,'PUERTO')
                    #Reordenar para ver TRUE O FALSE
                    cms["TV"] = cms["TV"].str.len() != 0
                    cms["TV"] = cms["TV"].replace({True:'TV',False:''}, regex=True)
                    cms["DATOS"] = cms["DATOS"].str.len() != 0
                    cms["DATOS"] = cms["DATOS"].replace({True:'DATOS',False:''}, regex=True)
                    cms["VOZ"] = cms["VOZ"].str.len() != 0
                    cms["VOZ"] = cms["VOZ"].replace({True:'VOZ',False:''}, regex=True)
                    cms["PRIORIDAD"] = cms['TV'] + " " + cms['DATOS'] + " " + cms['VOZ']
                    cms["PRIORIDAD"] = cms["PRIORIDAD"].str.lstrip()
                    cms["PRIORIDAD"] = cms["PRIORIDAD"].str.rstrip()
                    cms["PRIORIDAD"] = cms["PRIORIDAD"].replace({' ':'-'}, regex=True)
                    cms["PRIORIDAD"] = cms["PRIORIDAD"].replace({'--':'-'}, regex=True)
                    cms[['TV','DATOS','VOZ']] = cms[['TV','DATOS','VOZ']].replace(r'^\s*$', np.nan, regex=True)
                    cms['PRIORIDAD_2'] = np.where(cms['TV'].isna(), cms['DATOS'], cms['TV'])
                    cms['PRIORIDAD_2'] = np.where(cms['PRIORIDAD_2'].isna(), cms['VOZ'], cms['PRIORIDAD_2'])
                    #JUNTAR DE LA COLUMNA AL COSTADO
                    cms['PRIORIDAD_2'] = np.where(cms['PRIORIDAD_2'].isna(),
                                            cms['BORRAR'],
                                            cms['PRIORIDAD_2'])
                    cms[['PRIORIDAD','PRIORIDAD_2']] = cms[['PRIORIDAD','PRIORIDAD_2']].replace({'':'OTROS', np.nan:'OTROS'})
                    cms.rename(columns={'PRIORIDAD':'Total_Prioridad','PRIORIDAD_2':'Primera_Variable','PORT_ID':'Codigo_Gpon'},inplace=True)


                    #convertir columna a numero
                    regex = re.compile(r'[^0-9]') # Eliminamos todo lo que no sean números
                    cms['codcli']=cms['codcli'].replace(regex, '').fillna(0).apply(pd.to_numeric, errors='ignore')
                    #print("listo")
                    # EXTARER DATOS
                    gpontick = pd.read_csv('PLANTA_GPON/Gpon_ticket.csv', sep=',')
                    gpontick['SUBSCRIPCION']=gpontick['SUBSCRIPCION'].apply(pd.to_numeric, errors='ignore')
                    #print(gpontick)
                    #gpontick = pd.read_csv('PLANTA_GPON/Gpon_ticket.csv', sep=',')
                    union = pd.merge(left=cms,right=gpontick, how='left', left_on='codcli', right_on='SUBSCRIPCION')
                    union['Date'] = pd.to_datetime(union['fec_regist'], errors='coerce')
                    union['Date'] = union['Date'].dt.strftime('%B-%d')
                    #TODO tabla dinamica
                    uu  = pd.pivot_table(union, index=['OLT_ALIAS'], columns=['Date'], aggfunc='size')
                    ##################################################################
                    #uu.to_csv("EXPORTADO/ticket_averias.csv", sep=';')
                    #gpontick = pd.read_csv('EXPORTADO/ticket_averias.csv', sep=';')
                    #df1 = uu.iloc[3:-1, : ]
                    #aa = gpontick.drop(['Date'], axis=1)
                    #añss = (aa.columns)
                    #gpontick[añss] = gpontick[añss].fillna(0)
                    #gpontick[añss] = gpontick[añss].astype(int)
                    tb_olt = pd.read_csv('PLANTA_GPON/Tabla_dinamica_OLT.csv', sep=',')
                    #print(tb_olt)
                    #tb_olt = pd.read_csv('EXPORTADO/Tabla_dinamica_OLT.csv', sep=',')
                    #TODO sumar una tabla dinamica
                    gpontick = uu.apply(pd.to_numeric, downcast='signed',errors='ignore')
                    gpontick['Total'] = gpontick.sum(axis=1)
                    union2 = pd.merge(left=gpontick,right=tb_olt, how='left', left_on='OLT_ALIAS', right_on='OLT_ALIAS')
                    #TODO para dividir
                    #union2['formula'] = union2.Total / union2.value
                    #TODO para color
                    #df_style = union2.style.applymap(lambda x: 'color:blue', subset=["OLT_ALIAS"]) \
                    #.background_gradient(cmap="coolwarm",axis=None, vmin=0.0039, vmax=0.005, subset=["formula"])
                    #df_style
                    union = pd.merge(left=union,right=tb_olt, how='left', left_on='OLT_ALIAS', right_on='OLT_ALIAS')
                    union = union.rename(columns={'value':'Cliente',})
                    union['fec_regist'] = pd.to_datetime(union['fec_regist'], errors='coerce')
                    union['Year'] = union['fec_regist'].dt.year
                    union['Month'] = union['fec_regist'].dt.month
                    union['day'] = union['fec_regist'].dt.day
                    union = union.drop(['Date'], axis=1)
                    #gpontick=gpontick.drop([0])
                    #gpontick.to_csv("EXPORTADO/ticket_averias.csv", sep=';')
                    #TODO CRUCE CON OLT
                    df = pd.read_excel('NODO/NODO.xlsx')
                    #Trouble = pd.read_excel('OLT/OLT.xlsx')
                    df = df[['NODO','Descripcion','Nombre OLT']]
                    df = df[df['NODO'].notna()]
                    df = df.drop_duplicates(subset=['NODO'])
                    df = df.groupby(['NODO','Descripcion','Nombre OLT']).agg(NODO_size=('NODO', 'size')).reset_index()
                    ###########
                    #print(df)
                    #print(union)
                    union3 = pd.merge(left=union,right=df, how='left', left_on='codnod', right_on='NODO')
                    #print(union3)
                    union = union3.drop(['NODO','NODO_size'], axis=1)
                    union["tiptecnologia"] = union["tiptecnologia"].replace({'FTTH':'GPON'}, regex=True)
                    #####
                    ## TODO lo nuevo data 
                    ####
                    data = pd.DataFrame()
                    nombres = ['G', 'R', '']
                    edades = ["GPON", "HFC", "HFC"]
                    data['nroplanooo'] = nombres
                    data['tiptecnologia'] = edades
                    #convertir columna a numero
                    regex = re.compile(r'[^A-Z]') # Eliminamos todo lo que no sean números
                    union['nroplanooo']=union['nroplano'].replace(regex, '').fillna(0).astype(str)
                    #df = df[df.Año != 2022]
                    union = pd.merge(union, data, on='nroplanooo', how='outer')
                    #JUNTAR DE LA COLUMNA AL COSTADO
                    union['tiptecnologia_x'] = np.where(union['tiptecnologia_x'].isna(),
                                            union['tiptecnologia_y'],
                                            union['tiptecnologia_x'])

                    union = union.drop(['BORRAR','Nombre OLT','tiptecnologia_y','nroplanooo'], axis=1)
                    union['tiptecnologia_x']=union['tiptecnologia_x'].replace("","HFC")

                    ### pedir a trabol del inicio origina para aumnetar columnas cruzar
                    #limpio duplicado
                    gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                    sh = gc.open("DT_PEDIR_COLUM")
                    #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                    worksheet = sh.get_worksheet(0)
                    Troubledt = pd.DataFrame(worksheet.get_all_records())
                    #cruzar la data actual con trabol origial y aumter columnas requeridos 
                    union = pd.merge(union, Troubledt, on='codreq', how='outer')
                    ######################

                    union['fec_regist'] = pd.to_datetime(union.fec_regist, errors = 'coerce').dt.strftime("%Y/%m/%d  %H:%M:%S")
                    
                    ### lo mejor converir a numero
                    union['CUSTOMERID_CRM__c']=pd.to_numeric(union['CUSTOMERID_CRM__c'], errors='coerce').astype('Int64')
                    #convertir columna a numero
                    regex = re.compile(r'[^0-9]')
                    union['codcli']=union['codcli'].replace(regex, '').fillna(0).astype(int)
                    union = union.astype("string")
                    union = union.fillna('')
                    ## ORDENAR DATA
                    union = union.sort_values(by='fec_regist').reset_index(drop=True)
                    ######## ORDENADO FIN ##################
                    gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                    sh = gc.open("Gpon_ticket_WEB")
                    #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                    worksheet = sh.get_worksheet(0)
                    #borrar datos total y dejar encabezado
                    worksheet.resize(rows=1)
                    worksheet.resize(rows=30)
                    #cargar datos df
                    worksheet.update([union.columns.values.tolist()] + union.values.tolist())

                    st.write("SE CARGO CON EXITO AHORA YA PUEDES ACTUALIZAR \n EL EXCEL DE LAS TABLAS DINAMICAS")
                    # para ver la cantidad de registros
                    total = str(len(union))
                    st.success('Consolidado total de '+total+' Registros')

                                ## borrar nombres de la pagina
                    hide_streamlit_style = """
                                <style>
                                #MainMenu {visibility: hidden;}
                                footer {visibility: hidden;}
                                </style>
                                """
                    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        uploaded_Simple = st.sidebar.file_uploader(
                                label="Solo cargar data__+Simple. (200MB max)",
                                type=['csv'])
#########
##TODO CARGAR SOLO MAS SIMPLE
##########
        if uploaded_Simple is not None:
            #st.sidebar.title("Solo cargar +Simple")
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

                except Exception as e:
                    st.error('DATA NO CORRESPONDE 👋🏻')

            ## borrar nombres de la pagina
            hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        </style>
                        """
            st.markdown(hide_streamlit_style, unsafe_allow_html=True)

            st.markdown(
                """
                <style>

                header .css-1595djx e8zbici2{
                display: flex;
                flex-direction: column;
                align-items: center;
                }

                header .logo-text{
                    margin: 0;
                    padding: 10px 26px;
                    font-weight: bold;
                    color: rgb(60, 255, 0);
                    font-size: 0.8em;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <header class="css-1595djx e8zbici2">
                    <p class="logo-text">App Alarmas 👨🏻‍💻Giancarlos .C</p>
                </header>
                """,
                unsafe_allow_html=True
            )
            ###
            ####
            ####
            ####
            ######
            ######
        primaryColor = st.get_option("theme.primaryColor")
        s = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Atma:wght@600&display=swap');
        div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; }}
        <style>
        """
        st.markdown(s, unsafe_allow_html=True)

        ## borrar nombres de la pagina
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    xs = ['Cardenas', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot', 'YERSON', 'Roberto']
    #xs = ['Cardenas', 'LLLERENAL', 'Hinostroza', 'Argomedo', 'VIERA']
    bs = (username in xs)

    if selected == "Projects":
        if bs == True:

            cnxn = mysql.connector.connect( host="localhost",
                                            port="3306",
                                            user="root",
                                            passwd="CARDENAS47465810",
                                            db="bdtickets"
                                            )
            cursor = cnxn.cursor()
                #st.title(f"You have selected {selected}")
            st.title("GESTION TICKETS PENDIENTES💻")
            st.sidebar.image("logo2.png", width=290)


            page_names = ['GPON', 'HFC']
            page = st.sidebar.radio('Selecciona inf. Tecnoligia💻',page_names, index=0)
            #######
            ## TODO CONECTION A LA BASE DE DATOS MYSQL

            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')
            st.sidebar.markdown('')

            st.sidebar.markdown(
            '<p class="big-font"; style="text-align:center;color:Lime;font-size:16px;border-radius:2%;">©👨🏻‍💻Giancarlos .C</p>', unsafe_allow_html=True
            )

            sql = """
            SELECT GESTOR, codreq,tiptecnologia_x, FEC_CERRAR FROM bdtickets WHERE  ESTADO="PENDIENTE" ;
            """
            pend = pd.read_sql(sql, cnxn)
            pend = pend[pend['tiptecnologia_x'] == page]
            pendca = str(len(pend))
            #print("listo")
            sql = """
            SELECT GESTOR, codreq, FEC_CERRAR FROM bdtickets WHERE  ESTADO="CERRAR" ;
            """
            df = pd.read_sql(sql, cnxn)
            dfg = df[df['GESTOR'] == name]
            date = datetime.now()
            ##TODO SIEMPRE VER ESTO PARA CONTADOR
            ##FIXME SOLO CAMBIAR ESTO FIRMATO DE FECHA NO LO DE ABAJO
            tcanti = (date.strftime("%Y-%d-%m"))   ## inicio de semana
            #tcanti = (date.strftime("%Y-%m-%d"))  ## luego dias despues de se semana
            #print(tcanti)
        ##### cantidad de cerradas
            df = dfg
            df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR']).dt.date
            #df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR'], format='%Y-%m-%d')
            df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR'])
            #print(df)
            canti = str(len(df[df['FEC_CERRAR'] == tcanti]))
            #print(canti)
            st.markdown(f'<p class="big-font"; style="text-align:center;color:Cyan;font-size:24px"><b>👉🏻  {canti} ✔️{pendca}</b></p>', unsafe_allow_html=True)
            #st.sidebar.header("catidad trabajada "+ str(canti))
            ### EXTARER DATOS
            sql = """
            SELECT * FROM bdtickets  WHERE ESTADO = 'PENDIENTE' ORDER BY fec_regist ;
            """
            date = datetime.now()
            tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))

            df = pd.read_sql(sql, cnxn)
            df = df[df['tiptecnologia_x'] == page]
            df = df[df['FEC_PROG'] < tiempo]
            df = df[(df["GESTOR"]==name) | (df["GESTOR"]=="")].head(1)

            #df = df[df['codofcadm'] == 'GIANCARLOS']
            #df = df.head(1)
            #print(df)

            #dfu =df["codreq"].head(1)
            #dfu = (dfu.to_string(index=False))
            #print(df)
            #df = df[df.year.isin([2008, 2009])]


            ###########
            ### EXTARER DATOS
            sql2 = """
                SELECT *
                FROM bdtickets
                WHERE
                ESTADO = 'PROGRAMADO' ORDER BY FEC_PROG ;
            """

            date = datetime.now()
            tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))

            df2 = pd.read_sql(sql2, cnxn)
            df2 = df2[df2['GESTOR'] == name]
            df2 = df2[df2['FEC_PROG'] < tiempo].head(1)
            #df2 = df2[df2['ESTADO'] == 'PROGRAMADO']
            #df = df[df['codofcadm'] == 'GIANCARLOS']
            #df = df.head(1)
            #print(df2)


            dfunom =df2["nomcli"].head(1)
            dfu2 =df2["codreq"].head(1)
            codcli =df2["codcli"].head(1)
            fec_regist =df2["fec_regist"].head(1)
            tiptecnologia_x =df2["tiptecnologia_x"].head(1)
            numtelefvoip =df2["numtelefvoip"].head(1)
            TELEFONO_REFERENCIA_1_CRM =df2["TELEFONO_REFERENCIA_1_CRM"].head(1)
            codnod =df2["codnod"].head(1)
            Categorization_Tier2 =df2["Categorization_Tier2"].head(1)
            CUSTOMERID_CRM__c =df2["CUSTOMERID_CRM__c"].head(1)
            Area_CRM =df2["Area_CRM"].head(1)
            desmotv =df2["desmotv"].head(1)
            # ejemplo de texto completo
            desobsordtrab =(df2["desobsordtrab"].unique())

            ##TODO ESTO es para ver cada datos de la tabla filtrada

            dfunom = (dfunom.to_string(index=False))
            dfu2 = (dfu2.to_string(index=False))
            codcli = (codcli.to_string(index=False))
            fec_regist = (fec_regist.to_string(index=False))
            tiptecnologia_x = (tiptecnologia_x.to_string(index=False))
            numtelefvoip = (numtelefvoip.to_string(index=False))
            TELEFONO_REFERENCIA_1_CRM = (TELEFONO_REFERENCIA_1_CRM.to_string(index=False))
            codnod = (codnod.to_string(index=False))
            Categorization_Tier2 = (Categorization_Tier2.to_string(index=False))
            CUSTOMERID_CRM__c = (CUSTOMERID_CRM__c.to_string(index=False))
            Area_CRM = (Area_CRM.to_string(index=False))
            desmotv = (desmotv.to_string(index=False))
            #desobsordtrab = (desobsordtrab.to_string(index=False))
            ## ejemplo de texto completo
            desobsordtrab = (str(desobsordtrab)[2:-2])
            #print(desobsordtrab)
            #df = df[df.year.isin([2008, 2009])]
            # para los botones horizontal
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


            try:


                genre = st.radio(
                    "Establece tu preferencia de actividad",
                    ('Programar', 'En espera','Finalizar', 'Analisis', 'Dashboard'))


                if  genre == 'Programar':
                    lencodcli = len(codcli)
                    #print(lencodcli)
                    if lencodcli == 0:

                        my_bar = st.progress(0)
                        ## fecha para programar y cerrar
                        date = datetime.now()
                        tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                        #print(tiempo) # DD Month, YYYY HH:MM:SS

                        options = (df2['codreq'].unique())


                        add  = str('CERRAR')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        rreeee = (str(options)[2:-2])
                        #print(rreeee)



                        options = (df['codreq'].unique())

                        add  = str('PROGRAMADO')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        #print(adwe)
                        #st.info(dfu2)

                        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                        #st.info(dfu2)
                        ### un ejemplo para texto
                        #st.info(desobsordtrab)
                        #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{dfunom}</p>', unsafe_allow_html=True)

                        with st.form(key='my_form', clear_on_submit=True):
                        
                            col1, col2, col3 = st.columns(3)



                            with col1:
                                st.markdown("**Numero de tickets**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{dfu2}</p>', unsafe_allow_html=True)

                                #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                            with col2:
                                #st.markdown("**Codigo de cliente**")
                                lenCodigoclienteinp = st.text_input("**Codigo de cliente**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                                #lenCodigocliente = len(codcli)
                                #print(lenArea_CRM)
                                #if lenArea_CRM
                                #if lenCodigocliente > 1:
                                #    st.markdown("**Codigo de cliente**")
                                #    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)
                                #else:
                                #    lenCodigoclienteinp = st.text_input("**Codigo de cliente**")
                                

                            with col3:
                                st.markdown("**Fecha de Ticket**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                            with col1:

                                    Tecno = st.selectbox(
                                        "**Tecnologia**",
                                        (
                                            "GPON",
                                            "HFC",
                                        ),
                                        key="filter_type3",
                                        help="""
                                        Ten encuenta tu accion `Ticket` inf.
                                        """,
                                    )

                            with col2:
                                #st.markdown("**Telefono**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)
                                lenTelefono = st.text_input("**Telefono**")

                            with col3:
                                #st.markdown("**Telf Ref**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)
                                lenTelfRef = st.text_input("**Telf Ref**")

                            with col1:
                                #st.markdown("**Nodo**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)
                                lenNodo = st.text_input("**Nodo**")

                            with col2:
                                st.markdown("**CategTier 2**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                            with col3:
                                st.markdown("**Observacion**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                            with col1:
                                #st.markdown("**Cuestomerid crm**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)
                                lenCuestomerid = st.text_input("**Cuestomerid crm**")

                            with col2:
                                st.markdown("**Area crm**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)

                                #lenArea_CRM = len(Area_CRM)
                                ##print(lenArea_CRM)
                                ##if lenArea_CRM
                                #if lenArea_CRM > 1:
                                #    st.markdown("**Area crm**")
                                #    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                                #else:
                                #    lenArea_CRMinp = st.text_input("**Area crm**")


                            #with col3:
                            #    #st.markdown("**Observacion 2**")
                            #    #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                            #    lenObservacion2 = st.text_input("**Observacion 2**")

                            with col1:
                                lencodofcadm = st.text_input("**codofcadm**")

                            with col2:
                                lendesdtt = st.text_input("**desdtt**")

                            with col3:
                                lenservicioAfectado = st.text_input("**servicioAfectado**")

                            lennomcliente = st.text_input("**Nombre_Cliente**")

                            lenObservacion2 = st.text_area("Observación", key="text")

                            col1, col2, col3 , col4, col5 = st.columns(5)

                            with col1:
                                pass
                            with col2:
                                pass
                            with col4:
                                pass
                            with col5:
                                pass
                            with col3 :
                                submitted = st.form_submit_button("✍🏻Enviar")

                            if submitted == True:
                                dt1 = len(lenCodigoclienteinp)
                                dt2 = len(lenTelefono)
                                dt3 = len(lenTelfRef)
                                dt4 = len(lenNodo)
                                dt5 = len(lenCuestomerid)
                                dt6 = len(lenObservacion2)
                                dt7 = len(lencodofcadm)
                                dt8 = len(lendesdtt)
                                dt9 = len(lenservicioAfectado)

                                #https://stackoverflow.com/questions/16522111/python-syntax-for-if-a-or-b-or-c-but-not-all-of-them
                                #if (dt1 and dt2 and dto) > 0:
                                if dt1 > 0 and dt2 > 0 and  dt3 > 0 and  dt4 > 0 and  dt5 > 0 and  dt6 > 0 and  dt7 > 0 and  dt8 > 0 and  dt9 > 0:
                                #if dt1, dt2  > 0:
                                    if Tecno != page:
                                        sql = "UPDATE bdtickets SET codcli = %s, tiptecnologia_x = %s, numtelefvoip = %s, TELEFONO_REFERENCIA_1_CRM = %s, codnod = %s, CUSTOMERID_CRM__c = %s, desobsordtrab = %s, codofcadm = %s, desdtt = %s, servicioAfectado = %s, nomcli = %s, ESTADO='PENDIENTE', GESTOR='', FEC_PROG='' ,FEC_CERRAR='' ,ACCION='' ,OBS='' ,ACTIVO='0'  WHERE codreq = %s"
                                        val = (lenCodigoclienteinp, Tecno, lenTelefono, lenTelfRef, lenNodo, lenCuestomerid, lenObservacion2, lencodofcadm, lendesdtt, lenservicioAfectado, lennomcliente, rreeee)
                                        #print(lenCodigoclienteinp)
                                        #print(rreeee)
                                        cursor.execute(sql, val)
                                        cnxn.commit()
                                        st.experimental_rerun()
                                    else:
                                        sql = "UPDATE bdtickets SET codcli = %s, tiptecnologia_x = %s, numtelefvoip = %s, TELEFONO_REFERENCIA_1_CRM = %s, codnod = %s, CUSTOMERID_CRM__c = %s, desobsordtrab = %s, codofcadm = %s, desdtt = %s, servicioAfectado = %s, nomcli = %s  WHERE codreq = %s"
                                        val = (lenCodigoclienteinp, Tecno, lenTelefono, lenTelfRef, lenNodo, lenCuestomerid, lenObservacion2, lencodofcadm, lendesdtt, lenservicioAfectado, lennomcliente, rreeee)
                                        #print(lenCodigoclienteinp)
                                        #print(rreeee)
                                        cursor.execute(sql, val)
                                        cnxn.commit()
                                        st.experimental_rerun()

                                else:
                                    #st.error('👀 TIENES QUE ESCRIBIR EN TODOS LOS INPUT👀 ')
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,MistyRose, MistyRose);color:BLACK;font-size:18px;border-radius:2%;"><b>😡👀 TE FALTA INGRESAR LOS DATOS REQUERIDOS 👀😡</b></p>', unsafe_allow_html=True)

                            #PONER COLOR A LOS INPUT TRABAJA CON CSS
                            def local_css(file_name):
                                with open(file_name) as f:
                                    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

                            def remote_css(url):
                                st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

                            def icon(icon_name):
                                st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

                            local_css("style.css")
                            #remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
                    else:
                        #TODO SIVERVPARA BARRA AZUL
                        my_bar = st.progress(0)
                        ## fecha para programar y cerrar
                        date = datetime.now()
                        tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                        #print(tiempo) # DD Month, YYYY HH:MM:SS

                        options = (df2['codreq'].unique())

                        add  = str('CERRAR')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                        sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s WHERE codreq = %s AND ESTADO='PROGRAMADO'"
                        val = (add, nom, adwe)
                        cursor.execute(sql, val)


                        options = (df['codreq'].unique())

                        add  = str('PROGRAMADO')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        #st.info(dfu2)

                        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                        #st.info(dfu2)
                        ### un ejemplo para texto
                        #st.info(desobsordtrab)
                        #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{dfunom}</p>', unsafe_allow_html=True)


                        
                        col1, col2, col3 = st.columns(3)



                        with col1:
                            st.markdown("**Numero de tickets**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{dfu2}</p>', unsafe_allow_html=True)

                            #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                        with col2:
                            st.markdown("**Codigo de cliente**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                            

                        with col3:
                            st.markdown("**Fecha de Ticket**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                        with col1:
                            st.markdown("**Tecnologia**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tiptecnologia_x}</p>', unsafe_allow_html=True)


                        with col2:
                            st.markdown("**Telefono**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)


                        with col3:
                            st.markdown("**Telf Ref**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)


                        with col1:
                            st.markdown("**Nodo**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)

                        with col2:
                            st.markdown("**CategTier 2**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                        with col3:
                            st.markdown("**Observacion**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                        with col1:
                            st.markdown("**Cuestomerid crm**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)

                        with col2:
                            st.markdown("**Area crm**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                        
                        with col3:
                            st.markdown("**Observacion 2**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                        
                        with col1:
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            textogestion = "Realizar Actividades💻"
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:Black;font-size:22px;border-radius:2%;">{textogestion}</p>', unsafe_allow_html=True)
                        with col1:
                            filter_type3 = st.selectbox(
                                "Accion",
                                (
                                    "71_REVERIFICA SIN DEFECTO",
                                    "7B_SOLUCION EN LINEA",
                                    "7C_TEMA COMERCIALES",
                                    "7D_GENERA NUEVO REQ",
                                    #"7E_NO SE UBICA CLITE",
                                    "7F_REQ MAL GENERADO",
                                    "Requiere Visita Tecnica",
                                    "En espera",
                                ),
                                key="filter_type3",
                                help="""
                                Ten encuenta tu accion `Ticket` inf.
                                """,
                            )

                        with col1:
                            try:
                                if st.button("📞No se ubica cliente"):


                                    mens = (df2['MENSAJE'].unique())
                                    mens = (str(mens)[2:-2])

                                    if mens > '0':
                                        numllamada = (df2['LLAMADA'].unique())
                                        numllamada = (str(numllamada)[2:-2])
                                        #print(numllamada)
                                        sumu = int(numllamada) + 1
                                        #print(sumu)
                                        if sumu <= 2:
                                            sumu = int(numllamada) + 1
                                        #if filter_type3 == "7E_NO SE UBICA CLITE":
                                            date = datetime.now()
                                            tiempohr = (date.strftime("%Y-%m-%d %H:%M:%S"))
                                            ahora = datetime.strptime(tiempohr, '%Y-%m-%d %H:%M:%S')
                                            dentro_de_1_hora = ahora + timedelta(hours=1)
                                            tiempohr = str(dentro_de_1_hora.strftime("%d-%m-%Y %H:%M:%S"))
                                            #print(tiempohr)
                                            sql1 = "UPDATE bdtickets SET ESTADO = %s, FEC_PROG = %s,ACTIVO = '0',ACCION = '7E_NO SE UBICA CLITE', LLAMADA = %s WHERE codreq = %s"
                                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                                            val1 = ('PENDIENTE', tiempohr, sumu ,dfu2)
                                            cursor.execute(sql1, val1)
                                            cnxn.commit()
                                        if sumu == 3:
                                        #if filter_type3 == "7E_NO SE UBICA CLITE":
                                            date = datetime.now()
                                            tiempohr = (date.strftime("%Y-%m-%d %H:%M:%S"))
                                            ahora = datetime.strptime(tiempohr, '%Y-%m-%d %H:%M:%S')
                                            dentro_de_1_hora = ahora + timedelta(hours=1)
                                            tiempohr = str(dentro_de_1_hora.strftime("%d-%m-%Y %H:%M:%S"))
                                            #print(tiempohr)
                                            sql1 = "UPDATE bdtickets SET ESTADO = %s,GESTOR = '', FEC_PROG = %s,ACTIVO = '0',ACCION = '', LLAMADA = '0' WHERE codreq = %s"
                                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                                            val1 = ('PENDIENTE',tiempohr, dfu2)
                                            cursor.execute(sql1, val1)
                                            cnxn.commit()
                                    else:
                                        st.error('Primero tienes que enviar SMS⚠️')
                            except Error as e:
                                print('Gian', e)
                

                        st.write("")
                        #title = st.text_input("INGRESA TU GESTION")
                        raw_text = st.text_area("Observación", key="text")
                        #form = st.form(key='text')
                        #print(input)
                        def clear_text():
                            st.session_state["text"] = ""
                            
                        st.button("🗑️Limpiar ", on_click=clear_text)
                            
                        #st.button("clear text input", on_click=clear_text)

                        #st.button("Inicio")
                        col1, col2, col3 , col4, col5 = st.columns(5)

                        with col1:
                            pass
                        with col2:
                            pass
                        with col4:
                            pass
                        with col5:
                            pass
                        with col3 :

                            sql = """
                            SELECT * FROM bdtickets  WHERE ACCION = 'En espera'
                            """
                            esperadt = pd.read_sql(sql, cnxn)
                            esperadt2 = esperadt[esperadt['GESTOR'] == name]
                            #espera = esperadt2['codreq']
                            estoesp = int(len(esperadt2))
                            
                            #print(estoesp)

                            if estoesp <= 2:
                                
                                if st.button("✔️Cerrar"):
                                    #def __init__(self):
                                    #    st.experimental_rerun()

                                    sql1 = "UPDATE bdtickets SET ACCION = %s, OBS = %s, FEC_CERRAR = %s WHERE codreq = %s AND ACTIVO = '1' "
                                    #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                                    val1 = (filter_type3,raw_text,tiempo ,dfu2)
                                    cursor.execute(sql1, val1)
                                    #time.sleep(1)

                                    #caching.clear_cache()
                                    #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                                    #st.info(dfu)
                                    sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s, FEC_PROG = %s, ACTIVO = '1' WHERE codreq = %s AND ACTIVO = '0' "
                                    val = (add, nom, tiempo, adwe)
                                    cursor.execute(sql, val)
                                    cnxn.commit()
                                    #cursor.close()
                                    #cnxn.close()
                                        ###TODO IMPORTANTE ES PARA REFRESCAR LA PAGINA
                                        #st.experimental_rerun()
                                        #st.legacy_caching.clear_cache()
                                        #st.legacy_caching.clear_cache()
                                    #import pyautogui
                                    #pyautogui.hotkey("ctrl","F5")
                                    #st.experimental_singleton.clear()
                                    st.balloons()
                                    time.sleep(0.75)
                                    st.experimental_rerun()

                                    #

                                # st.experimental_rerun()
                                ## fondo total
                                def add_bg_from_url():
                                    st.markdown(
                                        f"""
                                        <style>
                                        .stApp {{
                                            background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                                            background-attachment: fixed;
                                            background-size: cover
                                        }}
                                        </style>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                add_bg_from_url() 

                            else:
                                st.error('Tienes 3 tickets en esepra ⚠️')


                if  genre == 'Finalizar':

                    #TODO SIVERVPARA BARRA AZUL
                    my_bar = st.progress(0)
                    ## fecha para programar y cerrar
                    date = datetime.now()
                    tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                    #print(tiempo) # DD Month, YYYY HH:MM:SS

                    options = (df2['codreq'].unique())

                    add  = str('CERRAR')
                    nom = str(name)
                    adwe = (str(options)[2:-2])
                    #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                    sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s WHERE codreq = %s AND ESTADO='PROGRAMADO'"
                    val = (add, nom, adwe)
                    cursor.execute(sql, val)


                    options = (df['codreq'].unique())

                    add  = str('PROGRAMADO')
                    nom = str(name)
                    adwe = (str(options)[2:-2])
                    #st.info(dfu2)

                    #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                    #st.info(dfu2)
                    ### un ejemplo para texto
                    #st.info(desobsordtrab)
                    #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{dfunom}</p>', unsafe_allow_html=True)


                    
                    col1, col2, col3 = st.columns(3)



                    with col1:
                        st.markdown("**Numero de tickets**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{dfu2}</p>', unsafe_allow_html=True)

                        #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Codigo de cliente**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                    with col3:
                        st.markdown("**Fecha de Ticket**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Tecnologia**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tiptecnologia_x}</p>', unsafe_allow_html=True)


                    with col2:
                        st.markdown("**Telefono**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)


                    with col3:
                        st.markdown("**Telf Ref**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Nodo**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**CategTier 2**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                    with col3:
                        st.markdown("**Observacion**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                    with col1:
                        st.markdown("**Cuestomerid crm**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Area crm**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown("**Observacion 2**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                    
                    with col1:
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        textogestion = "Realizar Actividades💻"
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:Black;font-size:22px;border-radius:2%;">{textogestion}</p>', unsafe_allow_html=True)
                    with col1:
                        filter_type3 = st.selectbox(
                            "Accion",
                            (
                                "71_REVERIFICA SIN DEFECTO",
                                "7B_SOLUCION EN LINEA",
                                "7C_TEMA COMERCIALES",
                                "7D_GENERA NUEVO REQ",
                                "7E_NO SE UBICA CLITE",
                                "7F_REQ MAL GENERADO",
                                "Requiere Visita Tecnica",
                            ),
                            key="filter_type3",
                            help="""
                            Ten encuenta tu accion `Ticket` inf.
                            """,
                        )


                    st.write("")
                    #title = st.text_input("INGRESA TU GESTION")
                    raw_text = st.text_area("Observación", key="text")
                    #form = st.form(key='text')
                    #print(input)
                    def clear_text():
                        st.session_state["text"] = ""
                        
                    st.button("🗑️Limpiar ", on_click=clear_text)
                        
                    #st.button("clear text input", on_click=clear_text)

                    #st.button("Inicio")
                    col1, col2, col3 , col4, col5 = st.columns(5)

                    with col1:
                        pass
                    with col2:
                        pass
                    with col4:
                        pass
                    with col5:
                        pass
                    with col3 :
                        
                        if st.button("😮‍💨Fin"):
                            #def __init__(self):
                            #    st.experimental_rerun()

                            sql1 = "UPDATE bdtickets SET ACCION = %s, OBS = %s, FEC_CERRAR = %s WHERE codreq = %s AND ACTIVO = '1' "
                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                            val1 = (filter_type3,raw_text,tiempo ,dfu2)
                            cursor.execute(sql1, val1)
                            cnxn.commit()

                            sql1 = "UPDATE bdtickets SET ESTADO = %s,GESTOR = '', FEC_PROG = '',ACTIVO = '0', LLAMADA = '0',ACCION ='' WHERE GESTOR = %s AND ACCION = '7E_NO SE UBICA CLITE'"
                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                            val1 = ('PENDIENTE', name)
                            cursor.execute(sql1, val1)
                            cnxn.commit()

                            #cursor.close()
                            #cnxn.close()
                                ###TODO IMPORTANTE ES PARA REFRESCAR LA PAGINA
                                #st.experimental_rerun()
                                #st.legacy_caching.clear_cache()
                                #st.legacy_caching.clear_cache()
                            #import pyautogui
                            #pyautogui.hotkey("ctrl","F5")
                            #st.experimental_singleton.clear()
                            st.experimental_rerun()


                xs = ['Cardenas', 'LLLERENAL', 'Hinostroza', 'Argomedo', 'VIERA']
                bs = (username in xs)
                if  genre == 'Dashboard':
                    if bs == True:
                    #if  'Cardenas' == username:      #
                        st.markdown("""
                            <iframe title="Gastion19" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=0c6caef7-27cf-4548-849c-1970f2d9b0bf&autoAuth=true&ctid=9744600e-3e04-492e-baa1-25ec245c6f10" frameborder="0" allowFullScreen="true"></iframe>
                        """, unsafe_allow_html=True)

                        # st.experimental_rerun()
                        ## fondo total
                        def add_bg_from_url():
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                                    background-attachment: fixed;
                                    background-size: cover
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        add_bg_from_url() 
                        
                if  genre == 'Analisis':
                    st.text("Cuadro de gestion individual!!!") 

                    st.success("Total tickets cerradas: " + " " + canti) 
                    ### programado
                    sql = """
                    SELECT GESTOR, codreq, FEC_PROG FROM bdtickets WHERE  ESTADO="PROGRAMADO" ;
                    """
                    df = pd.read_sql(sql, cnxn)
                    dfg = df[df['GESTOR'] == name]
                    #print(dfg)
                    #date = datetime.now()
                    #tcanti = (date.strftime("%Y-%m-%d"))
                ##### cantidad de programadas
                    #dfp = dfg
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
                    cantipro = str(len(dfg))
                    #print(cantipro)
                    st.info("Toltal tickets programado: " + " " + cantipro) 
                ##3 tranferir
                    sql = """
                    SELECT GESTOR, codreq, FEC_PROG FROM bdtickets WHERE  ACCION="7E_NO SE UBICA CLITE" ;
                    """
                    df = pd.read_sql(sql, cnxn)
                    dfg = df[df['GESTOR'] == name]
                    #print(dfg)
                    #date = datetime.now()
                    #tcanti = (date.strftime("%Y-%m-%d"))
                ##### cantidad de tranferir
                    #dfp = dfg
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
                    cantipro = str(len(dfg))
                    #print(cantipro)
                    #print("Tranferir" + " " + cantipro)
                    st.warning("Total tickest por llamar: " + " " + cantipro)

                    sql = """
                    SELECT * FROM bdtickets  WHERE ACCION = 'En espera' ;
                    """
                    df = pd.read_sql(sql, cnxn)
                    dfg = df[df['GESTOR'] == name]
                    #print(dfg)
                    #date = datetime.now()
                    #tcanti = (date.strftime("%Y-%m-%d"))
                ##### cantidad de tranferir
                    #dfp = dfg
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
                    cantipro = str(len(dfg))
                    #print(cantipro)
                    #print("Tranferir" + " " + cantipro)
                    st.error("Total tickest En espera: " + " " + cantipro)

                if  genre == 'En espera':

                    sql = """
                    SELECT * FROM bdtickets  WHERE ACCION = 'En espera'
                    """
                    esperadt = pd.read_sql(sql, cnxn)
                    esperadt2 = esperadt[esperadt['GESTOR'] == name]
                    espera = esperadt2['codreq']
                    
                    #print(espera)

                    filtro = st.selectbox(
                        "Tickets",
                        (espera
                        ),
                        key="filter_type3",
                        help="""
                        Ten encuenta tu accion `Ticket` inf.
                        """,
                    )

                    dtes = esperadt2[esperadt2['codreq'] == filtro]

                    nomcli = dtes['nomcli']
                    nomcli = (nomcli.to_string(index=False))


                    tk = dtes['codreq']
                    tk = (tk.to_string(index=False))
                    codcli = dtes['codcli']
                    codcli = (codcli.to_string(index=False))
                    fec_regist = dtes['fec_regist']
                    fec_regist = (fec_regist.to_string(index=False))
                    tiptecnologia_x = dtes['tiptecnologia_x']
                    tiptecnologia_x = (tiptecnologia_x.to_string(index=False))
                    numtelefvoip = dtes['numtelefvoip']
                    numtelefvoip = (numtelefvoip.to_string(index=False))
                    TELEFONO_REFERENCIA_1_CRM = dtes['TELEFONO_REFERENCIA_1_CRM']
                    TELEFONO_REFERENCIA_1_CRM = (TELEFONO_REFERENCIA_1_CRM.to_string(index=False))
                    codnod = dtes['codnod']
                    codnod = (codnod.to_string(index=False))
                    Categorization_Tier2 = dtes['Categorization_Tier2']
                    Categorization_Tier2 = (Categorization_Tier2.to_string(index=False))
                    desmotv = dtes['desmotv']
                    desmotv = (desmotv.to_string(index=False))
                    CUSTOMERID_CRM__c = dtes['CUSTOMERID_CRM__c']
                    CUSTOMERID_CRM__c = (CUSTOMERID_CRM__c.to_string(index=False))
                    Area_CRM = dtes['Area_CRM']
                    Area_CRM = (Area_CRM.to_string(index=False))
                    desobsordtrab = dtes['desobsordtrab']
                    desobsordtrab = (desobsordtrab.to_string(index=False))
        

                    #TODO SIVERVPARA BARRA AZUL
                    my_bar = st.progress(0)
                    ## fecha para programar y cerrar
                    date = datetime.now()
                    tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                    #print(tiempo) # DD Month, YYYY HH:MM:SS


                    #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                    #st.info(dfu2)
                    ### un ejemplo para texto
                    #st.info(desobsordtrab)
                    #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{nomcli}</p>', unsafe_allow_html=True)


                    
                    col1, col2, col3 = st.columns(3)



                    with col1:
                        st.markdown("**Numero de tickets**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tk}</p>', unsafe_allow_html=True)

                        #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Codigo de cliente**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                    with col3:
                        st.markdown("**Fecha de Ticket**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Tecnologia**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tiptecnologia_x}</p>', unsafe_allow_html=True)


                    with col2:
                        st.markdown("**Telefono**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)


                    with col3:
                        st.markdown("**Telf Ref**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Nodo**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**CategTier 2**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                    with col3:
                        st.markdown("**Observacion**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                    with col1:
                        st.markdown("**Cuestomerid crm**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Area crm**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown("**Observacion 2**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                    
                    with col1:
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        textogestion = "Realizar Actividades💻"
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:Black;font-size:22px;border-radius:2%;">{textogestion}</p>', unsafe_allow_html=True)
                    with col1:

                        filter_type3 = st.selectbox(
                            "Accion",
                            (
                                "71_REVERIFICA SIN DEFECTO",
                                "7B_SOLUCION EN LINEA",
                                "7C_TEMA COMERCIALES",
                                "7D_GENERA NUEVO REQ",
                                #"7E_NO SE UBICA CLITE",
                                "7F_REQ MAL GENERADO",
                                "Requiere Visita Tecnica",
                            ),
                            help="""
                            Ten encuenta tu accion `Ticket` inf.
                            """,
                        )


                    st.write("")
                    #title = st.text_input("INGRESA TU GESTION")
                    raw_text = st.text_area("Observación", key="text")
                    #form = st.form(key='text')
                    #print(input)
                    def clear_text():
                        st.session_state["text"] = ""
                        
                    st.button("🗑️Limpiar ", on_click=clear_text)
                        
                    #st.button("clear text input", on_click=clear_text)

                    #st.button("Inicio")
                    col1, col2, col3 , col4, col5 = st.columns(5)

                    with col1:
                        pass
                    with col2:
                        pass
                    with col4:
                        pass
                    with col5:
                        pass
                    with col3 :


                        if st.button("😮‍💨Fin"):
                            #def __init__(self):
                            #    st.experimental_rerun()

                            sql1 = "UPDATE bdtickets SET ACCION = %s, OBS = %s, FEC_CERRAR = %s WHERE codreq = %s AND ACTIVO = '1' "
                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                            val1 = (filter_type3,raw_text,tiempo ,tk)
                            cursor.execute(sql1, val1)
                            cnxn.commit()
                            #cursor.close()
                            #cnxn.close()
                                ###TODO IMPORTANTE ES PARA REFRESCAR LA PAGINA
                                #st.experimental_rerun()
                                #st.legacy_caching.clear_cache()
                                #st.legacy_caching.clear_cache()
                            #import pyautogui
                            #pyautogui.hotkey("ctrl","F5")
                            #st.experimental_singleton.clear()
                            st.experimental_rerun()


            except Error as e:
                print('디비 관련 에러 발생', e)
            
            finally : 
                # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
                #    커서와 커넥션을 모두 닫아준다.
                cursor.close()
                cnxn.close()
                #print('MYSQL 커넥션 종료')

            # para los botones horizontal
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            ## fondo total
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url() 
            try:

                ## botones en general
                primaryColor = st.get_option("theme.primaryColor")
                s = f"""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Atma:wght@600&display=swap');
                div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; }}
                <style>
                """
                st.markdown(s, unsafe_allow_html=True)

                ## borrar nombres de la pagina
                hide_streamlit_style = """
                            <style>
                            #MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}
                            header {visibility: hidden;}
                            </style>
                            """
                st.markdown(hide_streamlit_style, unsafe_allow_html=True)

                ## fondo total
                def add_bg_from_url():
                    st.markdown(
                        f"""
                        <style>
                        .stApp {{
                            background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                            background-attachment: fixed;
                            background-size: cover
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
                add_bg_from_url() 
                ### para la barra
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
            except Exception as e:
                pass

            ## borrar nombres de la pagina
            hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
            st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

        ## borrar nombres de la pagina
            hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
            st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

            st.markdown(
                """
                <style>

                header .css-1595djx e8zbici2{
                display: flex;
                flex-direction: column;
                align-items: center;
                }

                header .logo-text{
                    margin: 0;
                    padding: 10px 26px;
                    font-weight: bold;
                    color: rgb(60, 255, 0);
                    font-size: 0.8em;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <header class="css-1595djx e8zbici2">
                    <p class="logo-text">App Alarmas 👨🏻‍💻Giancarlos .C</p>
                </header>
                """,
                unsafe_allow_html=True
            )
            ###
            ####
            ####
            ####
            ######
            ######
        primaryColor = st.get_option("theme.primaryColor")
        s = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Atma:wght@600&display=swap');
        div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; }}
        <style>
        """
        st.markdown(s, unsafe_allow_html=True)

        ## borrar nombres de la pagina
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        ## fondo total
        def add_bg_from_url():
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                    background-attachment: fixed;
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        add_bg_from_url()

        #### fondo al costado
        def sidebar_bg(side_bg):
            side_bg_ext = 'jpg'
            st.markdown(
                f"""
                <style>
                [data-testid="stSidebar"] > div:first-child {{
                    background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
                }}
                </style>
                """,
                unsafe_allow_html=True,
                )
            side_bg = 'nooa.jpg'
            sidebar_bg(side_bg)

        if bs == False:
            from PIL import Image
            image = Image.open('pngegg.png')
            st.image(image, caption='Personal autorizado')

    xs = ['Cardenas', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot', 'YERSON', 'Roberto']
    #xs = ['Cardenas', 'LLLERENAL', 'Hinostroza', 'Argomedo', 'VIERA']
    bs = (username in xs)
    if selected == "Contact":
        if bs == True:

            #st.title(f"You have selected {selected}")
            #st.title(f"Hola {name} estamos en proceso de esta opcion...😮‍💨👨🏻‍💻")

            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,white, white);color:navy;font-size:24px;border-radius:2%;"><b>ENVIAR MENSAJE GESTION</b></p>', unsafe_allow_html=True)


            with st.form(key='my_form', clear_on_submit=True):

                    import streamlit as st
                    import streamlit as st
                    from streamlit_option_menu import option_menu
                    import pickle
                    from pathlib import Path
                    import pandas as pd
                    import numpy as np
                    #from soupsieve import select  # pip install pandas openpyxl
                    import streamlit_authenticator as stauth  # pip install streamlit-authenticator
                    ############################################ OCULTAR INFROMACION NO IMPORTANTE
                    import base64
                    import mysql.connector
                    from mysql.connector import Error
                    #import pyodbc
                    import streamlit as st
                    ############################################ OCULTAR INFROMACION NO IMPORTANTE
                    import warnings
                    warnings.filterwarnings('ignore')
                    #########################################3333
                    ##########################
                    import time
                    from datetime import datetime
                    from datetime import timedelta
                    import gspread
                    import re


                    col1, col2, col3 = st.columns(3)

                    with col1:
                        tick = st.text_input('Tickets')
                    with col2:
                        celu = st.text_input('Numero')

                        

                    mensaje = st.selectbox(
                        "Mensaje",
                        (
                            "SMS1",
                            "SMS2",
                        ),
                        key="filter_type8",
                        help="""
                        Ten encuenta tu accion `Ticket` inf.
                        """,
                    )


                    #TODO SIVERVPARA BARRA AZUL
                    #celu = '925266696'
                    #print(celu)

                    st.balloons()
                # Every form must have a submit button.

                    submitted = st.form_submit_button("✉️Enviar")


                    if submitted == True:

                        with st.spinner('Enviado mensaje...'):

                            date = datetime.now()
                            tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))

                            cnxn = mysql.connector.connect( host="localhost",
                                                            port="3306",
                                                            user="root",
                                                            passwd="CARDENAS47465810",
                                                            db="bdtickets"
                                                            )
                            cursor = cnxn.cursor()

                            #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                            sql = """
                            SELECT codreq, CUSTOMERID_CRM__c, servicioAfectado, MENSAJE FROM bdtickets WHERE codreq = %s ;
                            """
                            ##TODO SIEMPRE PONER LA COMA
                            cursor.execute(sql, (tick,))
                            # fetch result
                            record = cursor.fetchall()
                            #print(record)
                            #cursor.close()
                            #cnxn.close()

                            gian = pd.DataFrame(record)
                            gian.columns = ['codreq', 'CUSTOMERID_CRM__c', 'servicioAfectado', 'MENSAJE']
                            #for row in record:
                            #    print("GESTOR = ", row[0], )
                            #    print("codreq = ", row[1])
                            #    print("FEC_CERRAR = ", row[2])
                            #dfg = gian[gian['GESTOR'] == 'Giancarlos Cardenas']

                            tick =gian["codreq"]
                            tick = (tick.to_string(index=False))

                            servi =gian["servicioAfectado"]
                            servi = (servi.to_string(index=False))

                            codcli =gian["CUSTOMERID_CRM__c"]
                            codcli = (codcli.to_string(index=False))

                            numllamada = (gian['MENSAJE'].unique())
                            numllamada = (str(numllamada)[2:-2])
                            #print(numllamada)
                            sumu = int(numllamada) + 1


                            sql = "INSERT INTO bdmensaje (codreq, FECHA_ENV, SMS) VALUES (%s, %s, %s)"
                            val = (tick, tiempo, mensaje)
                            cursor.execute(sql, val)
                            #cnxn.commit()
                            sql1 = "UPDATE bdtickets SET MENSAJE = %s WHERE codreq = %s"
                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                            val1 = (sumu, tick)
                            cursor.execute(sql1, val1)

                            cnxn.commit()
                            cursor.close()
                            cnxn.close()
                            #print(dfunom)

                            import streamlit as st
                            import glob
                            import os
                            import time

                            import streamlit as st
                            from selenium import webdriver
                            from selenium.webdriver.chrome.options import Options
                            from selenium.webdriver.support.wait import WebDriverWait
                            from selenium.webdriver.common.by import By

                            options = Options()
                            options.add_argument("--headless")
                            options.add_argument("--no-sandbox")
                            options.add_argument("--disable-dev-shm-usage")
                            options.add_argument("--disable-gpu")
                            options.add_argument("--disable-features=NetworkService")
                            options.add_argument("--window-size=1920x1080")
                            options.add_argument("--disable-features=VizDisplayCompositor")

                            

                            #def delete_selenium_log():
                            #    if os.path.exists('selenium.log'):
                            #        os.remove('selenium.log')


                            #def show_selenium_log():
                            #    if os.path.exists('selenium.log'):
                            #        with open('selenium.log') as f:
                            #            content = f.read()
                            #            st.code(content)


                            # not required anymore:
                            # def get_chromedriver_path():
                            #     results = glob.glob('/**/chromedriver', recursive=True)  # workaround on streamlit sharing
                            #     return results[0]
                            #st.button("Inicio")

                            st.balloons()

                            

                            driver = webdriver.Chrome(options=options, service_log_path='selenium.log')

                            username = 'caramburu_TDP'
                            passwordd = 'WebSys29*T*'
                            driver.get("https://auth.movistaradvertising.com/login?logout")
                            time.sleep(1)

                            #pyautogui.hotkey("ctrl","F5")

                            

                            xpath = driver.find_element("xpath", '//INPUT[@id="username"]')
                            xpath.send_keys(username)
                            time.sleep(2)

                            xpath = driver.find_element("xpath", '//INPUT[@id="password"]')
                            xpath.send_keys(passwordd)
                            time.sleep(2)


                            xpath = driver.find_element("xpath", '//BUTTON[@type="submit"][text()="Ingresar"]')
                            xpath.click()
                            time.sleep(4)


                            xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                            xpath.click()
                            time.sleep(6)

                            xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                            xpath.click()
                            time.sleep(4)

                            #celu = '925266696'
                            #mensaje = 'Listoooossdddssss'

                            xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                            xpath.send_keys(celu)
                            time.sleep(6)

                            if 'SMS1' == mensaje:

                                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                xpath.send_keys(f"Hola, intentamos contactarte para solucionar la avería en tu {servi} {codcli}, estaremos contactandote nuevamente, Movistar.")
                                time.sleep(6)


                                xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                xpath.click()
                                time.sleep(6)

                                xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                xpath.click()
                                time.sleep(5)

                                driver.quit()

                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)
                                #st.success('Mensaje enviado')
                                st.balloons()
                                #st.experimental_rerun()

                                col1, col2, col3 = st.columns(3)

                                with col1:
                                    st.markdown("**Numero de tickets**")
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                            

                                with col2:
                                    st.markdown("**Numero de codcli**")
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                            

                                with col3:
                                    st.markdown("**Servi**")
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)

                            
                            if 'SMS2' == mensaje:


                                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                xpath.send_keys(f"Hola, intentamos contactarte para validar que tu {servi} {codcli} , ya se encuentra operativo, por favor realizar las validaciones, Movistar")
                                time.sleep(6)


                                xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                xpath.click()
                                time.sleep(6)

                                xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                xpath.click()
                                time.sleep(5)

                                driver.quit()

                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)

                                #st.success('Mensaje enviado')
                                st.balloons()
                                #st.experimental_rerun()
                                col1, col2, col3 = st.columns(3)

                                with col1:
                                    st.markdown("**Numero de tickets**")
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                            

                                with col2:
                                    st.markdown("**Numero de codcli**")
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                            

                                with col3:
                                    st.markdown("**Servi**")
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)




                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')
                    st.sidebar.markdown('')

                    st.sidebar.markdown(
                    '<p class="big-font"; style="text-align:center;color:Lime;font-size:16px;border-radius:2%;">©👨🏻‍💻Giancarlos .C</p>', unsafe_allow_html=True
                    )
                    ## fondo total
                    def add_bg_from_url():
                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url("https://cdn.pixabay.com/photo/2020/05/15/17/55/box-5174459_960_720.jpg 1x, https://cdn.pixabay.com/photo/2020/05/15/17/55/box-5174459_1280.jpg");
                                background-attachment: fixed;
                                background-size: cover
                            }}
                            </style>
                            """,
                            unsafe_allow_html=True
                        )
                    add_bg_from_url()

        if bs == False:
            from PIL import Image
            image = Image.open('pngegg.png')
            st.image(image, caption='Personal autorizado')
        ## fondo total
        def add_bg_from_url():
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("https://cdn.pixabay.com/photo/2020/05/15/17/55/box-5174459_960_720.jpg 1x, https://cdn.pixabay.com/photo/2020/05/15/17/55/box-5174459_1280.jpg");
                    background-attachment: fixed;
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        add_bg_from_url()



    ## borrar nombres de la pagina
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


