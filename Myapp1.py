import streamlit as st

st.title('ตรวจสอบคุณสมบัติการขอสินเชื่อบ้าน')
st.header('นางสาวชุติมา สุขสมัย')
st.subheader('สาขาวิชาวิทยากรข้อมูล')
st.markdown('---')

col1, col2 =st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/chu.jpg')


html_1="""
<div style="background-color:#73C6B6 ;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลการขอสินเชื่อบ้าน</h5></center>
</div>
"""
st.markdown(html_1,unsafe_allow_html=True)
st.markdown("")

import pandas as pd

dt=pd.read_csv('data/Root1.csv')
st.write(dt.head(10))

dt1 = dt['Gender'].sum()
dt2 = dt['Married'].sum()
dt3 = dt['Dependents'].sum()
dt4 = dt['Education'].sum()
dt5 = dt['Self_Employed'].sum()
dt6 = dt['ApplicantIncome'].sum()
dt7 = dt['CoapplicantIncome'].sum()
dt8 = dt['LoanAmount'].sum()
dt9 = dt['Loan_Amount_Term'].sum()
dt10 = dt['Credit_History'].sum()

dx = [dt1, dt2, dt3, dt4,dt5,dt6,dt7,dt8,dt9,dt10]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10"])

if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("not show bar chart")
else :
     st.button("not show bar chart")

html_2 = """
<div style="background-color:#FFBF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายการขอสินเชื่อบ้าน</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")
#ptlen = st.slider("กรุณาเลือกข้อมูล petal.length",0,10)
#ptwd = st.slider("กรุณาเลือกข้อมูล petal.width",0,10)

Gender = st.text_input("กรุณาเลือกข้อมูล Gender")
Married= st.text_input("กรุณาเลือกข้อมูล Married")
Dependents=st.number_input("กรุณาเลือกข้อมูล Dependents")
Education= st.text_input("กรุณาเลือกข้อมูล Education")
Self_Employed= st.text_input("กรุณาเลือกข้อมูล elf_Employed")
ApplicantIncome= st.number_input("กรุณาเลือกข้อมูล ApplicantIncome")
CoapplicantIncome= st.number_input("กรุณาเลือกข้อมูล CoapplicantIncome")
LoanAmount= st.number_input("กรุณาเลือกข้อมูล LoanAmount")
Loan_Amount_Term= st.number_input("กรุณาเลือกข้อมูล Loan_Amount_Term")

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if st.button("ทำนายผล"):
    #ทำนาย
   #dt = pd.read_csv("./data/iris.csv")  
   X = dt.drop('variety', axis=1) #เลือกคอลัมที่เอามาทำงาน
   y = dt.variety   #คอลัมคำตอบ

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)
        #ข้อมูลสำหรับการจำแนกข้อมูล
   x_input = np.array([[ptlen, ptwd, splen, spwd]])
        #เอา input ไปทดสอบ
   st.write(Knn_model.predict(x_input))
   out=Knn_model.predict(x_input)  #ผลลัพธ์

   if out[0]=="Setosa":
      #st.image("./pic/iris.jpg")
      st.header("Setosa")
   elif out[0]=="Versicolor":
      #st.image("./pic/iris2.jpg")
      st.header("Versicolor")
   else:
      #st.image("./pic/iris3.jpg")  
      st.header("Verginiga")
   st.button("ไม่ทำนาย")
else:
   st.button("ไม่ทำนาย")