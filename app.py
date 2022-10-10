import mysql.connector
#import pyodbc
import pandas as pd
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
st.set_page_config(layout="wide")
st.title("GESTION bdtickets CUADRO PENDIENTES💻")

st.sidebar.image("logo2.png", width=290)


#######
## TODO CONECTION A LA BASE DE DATOS MYSQL
#######


cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="b550dc65be0b71",
                                passwd="a3fa9457",
                                db="heroku_af31a2d889c5388"
                                )
cursor = cnxn.cursor()
#cursor.execute("SELECT  * FROM bdtickets WHERE fec_regist = (SELECT MIN(fec_regist )  FROM bdtickets where ESTADO = 'PENDIENTE' )")
#data = cursor.fetchall()
#df = pd.DataFrame(data)

print("listo")
### EXTARER DATOS
sql = """
SELECT  *
FROM bdtickets
WHERE fec_regist = (SELECT MIN(fec_regist )  FROM bdtickets where ESTADO = 'PENDIENTE' );
"""
df = pd.read_sql(sql, cnxn)
df = df[df['ESTADO'] == 'PENDIENTE'].head(1)
#df = df[df['codofcadm'] == 'GIANCARLOS']
#df = df.head(1)
#print(df)

dfu =df["codreq"].head(1)
dfu = (dfu.to_string(index=False))
#print(df)
#df = df[df.year.isin([2008, 2009])]


###########
### EXTARER DATOS
sql2 = """
SELECT  *
FROM bdtickets
WHERE fec_regist = (SELECT MIN(fec_regist )  FROM bdtickets where ESTADO = 'PROGRAMADO' );
"""
df2 = pd.read_sql(sql2, cnxn)
df2 = df2[df2['ESTADO'] == 'PROGRAMADO'].head(1)
#df = df[df['codofcadm'] == 'GIANCARLOS']
#df = df.head(1)
#print(df)


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
print(desobsordtrab)
#df = df[df.year.isin([2008, 2009])]


try:

    genre = st.radio(
        "What's your favorite movie genre",
        ('Desnsar', 'Cerrar y Descansar', 'Programar'))

    if  genre == 'Programar':

        options = (df2['codreq'].unique())

        add  = str('CERRAR')
        nom = "GIANCARLOS"
        adwe = (str(options)[2:-2])
        sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s WHERE codreq = %s"
        val = (add, nom, adwe)
        cursor.execute(sql, val)
        cnxn.commit()

        options = (df['codreq'].unique())

        add  = str('PROGRAMADO')
        nom = "GIANCARLOS"
        adwe = (str(options)[2:-2])
        #st.info(dfu2)

        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
        #st.info(dfu2)
        ### un ejemplo para texto
        #st.info(desobsordtrab)
        #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:24px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)


        
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
            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,BLACK, BLACK);color:white;font-size:24px;border-radius:2%;">{textogestion}</p>', unsafe_allow_html=True)
        with col1:
            filter_type3 = st.selectbox(
                "Accion",
                (
                    "contains",
                    "equals",
                    "notContains",
                    "notEquals",
                    "includingRegex",
                    "excludingRegex",
                ),
                key="filter_type3",
                help="""
                Note that if you use Regex in your filter, you must follow the `RE2` syntax.
                """,
            )

        st.write("")
        title = st.text_input("INGRESA TU GESTION")
        print(title)

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



            if(st.button("✔️Cerrar")):
                #caching.clear_cache()

                sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s WHERE codreq = %s"
                val = (add, nom, adwe)
                cursor.execute(sql, val)
                cnxn.commit()
                cursor.close()
                cnxn.close()
                #esto refresca la carga
                st.experimental_rerun()




    if  genre == 'Cerrar y Descansar':

        st.text("Welcome To GeeksForGeeks!!!") 

        "Select The Region",
        options = (df2['codreq'].unique())

        add  = str('CERRAR')
        nom = "GIANCARLOS"
        adwe = (str(options)[2:-2])

        st.markdown("Columns inside form")
        sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s WHERE codreq = %s"
        val = (add, nom, adwe)
        cursor.execute(sql, val)
        cnxn.commit()

        st.write("DESVANSAR")

        st.success("CERRADO") 
        
        st.info("Programado") 
        
        st.warning("LLamar") 
        
        st.error("Blnaco") 

except Exception as e:
    pass


# para los botones horizontal
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)






