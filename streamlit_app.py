import streamlit as st

def calendarForm(mindate,maxdate):
    with col2:
        with st.form(key="metercalendar",clear_on_submit=True):
            sd = st.date_input('Select a Start Date (Earliest date is shown)',value=mindate,min_value=mindate,max_value=maxdate,key='startDate')
            ed = st.date_input('Select an End Date (Latest date is shown)',value=maxdate,min_value=mindate,max_value=maxdate,key='endDate')
            submitBtn = st.form_submit_button('Get Hourly Consumption',on_click=getHourly,args=(sd,ed))

def getHourly(sd,ed):
    col3.write('---'+str(sd)+'----'+str(ed))



# import pandas as pd
# import streamlit as st
# import numpy as np
# # "---"
# b = np.array([(1.2,1,2.2), (1.1,2,1.2)], dtype=float)
# df = pd.DataFrame(b)
# st.write(df)  # 👈 Draw the dataframe


# import streamlit as st
# import pandas as pd

# # locale.setlocale(locale.LC_ALL, "en_US")

# # file = st.file_uploader(“Please choose a file”)

# # if file is not None:
# #   bytes_data = file.getvalue()
# #   st.write(bytes_data)
# #   stringio = StringIO(file.getvalue().decode("latin1")) #(when i tried utf-8 i got cant convert utf-8 at a axx position. so i changed it to latin1 but now i am getting above metioned error)
# #   st.write(stringio)
# #   #To read file as string:
# #   string_data = stringio.read()
# #   st.write(string_data)
# #   #Can be used wherever a "file-like" object is accepted:
# #   df= pd.read_spss(file)


# def resistance(s):
#      color='#fcdcdc' if s.interpretation=='Resistant' else ''
#      return ['background-color: {}'.format(color)]*len(s)
# def null_row(s):
#      size=1px if s.interpretation=='' else size=12px
#      return ['line-height: {}'.format(color)]*len(s)

# df_style=df.style.\
#      apply(resistance,axis=1).\
#      apply(height,axis=1)
                       
# st.table(df_style)
# st.dataframe(df_style)
