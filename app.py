import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.joblib')

st.title('Prediksi Harga Rumah')

luas = st.number_input('Luas Rumah (m2)', 50, 500)
kamar_tidur = st.number_input('Jumlah Kamar Tidur', 1, 10)
kamar_mandi = st.number_input('Jumlah Kamar Mandi', 1, 10)

if st.button('Prediksi'):
    features = np.array([[luas, kamar_tidur, kamar_mandi]])
    prediksi = model.predict(features)
    st.success(f'Perkiraan harga rumah: {prediksi[0]:.0f} juta')
