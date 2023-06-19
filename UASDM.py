import pickle
import streamlit as st

dementia_model = pickle.load(open('dementia_dataset.sav','rb'))

st.title('Prediksi Perilaku Pengidap Penyakit Dementia Berdasarkan Kondisi Kesehatan')
st.caption('Rahmat Ogi Sutiyono | 19/06/2023')
st.write('\n')

col1, col2=st.columns(2)
with col1 :
    Visit = st.number_input('Input visit Pasien :')
with col2 :
    MRDelay = st.number_input('Input MRDelay Pasien :')
with col2 :
    Gender = st.number_input('Input Gender Pasien :')
with col1 :
    Age = st.number_input('Input Age pasien :')
with col2 :
     EDUC= st.number_input('input EDUC Pasien :')
with col1 :
    CDR = st.number_input('Input CDR Pasien :')
with col2 :
   eTIV = st.number_input('Input Tahun Kelahiran Pasien :')
with col1 :
    nWBV = st.number_input('Input nWBV Pasien  :')
with col2 :
    ASF = st.number_input('Input ASF Pasien :')

dementia_diagnosis = ''

if st.button('Test Pengidap Penyakit Dementia') :
    dementia_prediction = dementia_model.predict([[Visit,MRDelay,Gender,Age,EDUC,CDR,eTIV,nWBV,ASF]])

    if(dementia_prediction[0] == 0):
        dementia_diagnosis = 'Pasien tidak Pengidap Dementia'
    else :
        dementia_diagnosis = 'Pasien Pengidap Dementia'

    st.success(dementia_diagnosis)