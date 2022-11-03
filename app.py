import pickle
from pathlib import Path
import pandas as pd
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

#TODO CONECTION A MYSQL
cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="b70d451b4ff985",
                                passwd="68b102d9",
                                db="heroku_9ca78643f8fb80d"
                                )
cursor = cnxn.cursor()

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
names = ['Giancarlos Cardenas', 'Genesis Medrano', 'Luis Llerena', 'DIANA BERNEDO', 'VIVIAN CERVERA', 'CAROL CHUNGA', 'LAURA VIERA', 'MERCEDES RAYMUNDO', 'MONTES CABANILLAS', 'RENZO RIMARACHIN', 'LORENA BENAVIDES', 'NANCY YEREN', 'GIULIANA BELLIDO', 'CARMEN HUAMANCHUMO', 'GABRIEL SANTA ANA', 'CARMEN POMA REYES', 'JOSE ECHEVARRIA', 'YORMAN MORI', 'ENZO PAULINO', 'GUSTAVO SALCEDO', 'KAREN MAYORCA', 'LESLIE PRUDENCIO', 'BARBARA HUAMANCHUMO', 'Jose Ricardo', 'Eber Hinostroza', 'Bot cardenas', 'YERSON HINOSTROZA', 'Roberto Faustor']
usernames = ['Cardenas', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot', 'YERSON', 'Roberto']

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
    tcanti = (date.strftime("%Y-%d-%m"))
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
            ('Programar', 'Finalizar', 'Analisis', 'Dashboard'))

        if  genre == 'Programar':
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
                    ),
                    key="filter_type3",
                    help="""
                    Ten encuenta tu accion `Ticket` inf.
                    """,
                )
            with col1:
                try:
                    if st.button("📞No se ubica cliente"):
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
            date = datetime.now()
            tcanti = (date.strftime("%Y-%m-%d"))
        ##### cantidad de programadas
            dfp = dfg
            dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
            dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
            cantipro = str(len(dfp[dfp['FEC_PROG'] == tcanti]))
            st.info("Toltal tickets Programado: " + " " + cantipro) 
           ##3 tranferir
            sql = """
            SELECT GESTOR, codreq, FEC_PROG FROM bdtickets WHERE  ACCION="Requiere Visita Tecn" ;
            """
            df = pd.read_sql(sql, cnxn)
            dfg = df[df['GESTOR'] == name]
            date = datetime.now()
            tcanti = (date.strftime("%Y-%m-%d"))
        ##### cantidad de tranferir
            dfp = dfg
            dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
            dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
            cantipro = str(len(dfp[dfp['FEC_PROG'] == tcanti]))
            #print("Tranferir" + " " + cantipro)
            st.warning("Total tickest tranferidos: " + " " + cantipro)

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
