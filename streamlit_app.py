import streamlit as st
import pandas as pd

# locale.setlocale(locale.LC_ALL, "en_US")

# file = st.file_uploader(“Please choose a file”)

# if file is not None:
#   bytes_data = file.getvalue()
#   st.write(bytes_data)
#   stringio = StringIO(file.getvalue().decode("latin1")) #(when i tried utf-8 i got cant convert utf-8 at a axx position. so i changed it to latin1 but now i am getting above metioned error)
#   st.write(stringio)
#   #To read file as string:
#   string_data = stringio.read()
#   st.write(string_data)
#   #Can be used wherever a "file-like" object is accepted:
#   df= pd.read_spss(file)


def resistance(s):
     color='#fcdcdc' if s.interpretation=='Resistant' else ''
     return ['background-color: {}'.format(color)]*len(s)
def null_row(s):
     size=1px if s.interpretation=='' else size=12px
     return ['line-height: {}'.format(color)]*len(s)

df_style=df.style.\
     apply(resistance,axis=1).\
     apply(height,axis=1)
                       
st.table(df_style)
st.dataframe(df_style)
