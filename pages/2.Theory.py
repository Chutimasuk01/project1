import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="Chutima Datascience Project",
    page_icon= ":bar_chart:",
)

st.header("ทฤษฎีที่เก่ี่ยวข้อง")
st.subheader("1.เหมืองข้อมูล ")
st.write("เหมืองข้อมูล (Data Mining) เป็นกระบวนการที่ใช้เทคนิคและเครื่องมือต่าง ๆ เพื่อค้นหาความรู้หรือแบบแผนที่ซ่อนอยู่ในข้อมูลที่มีปริมาณมาก โดยทำการวิเคราะห์ข้อมูลเพื่อค้นหาความสัมพันธ์, ลักษณะ, หรือลูกแบบที่สามารถนำมาใช้ประโยชน์ได้")

st.subheader("2.เพื่อนบ้านที่ใกล้ที่สุด ")
st.write("เพื่อนบ้านที่ใกล้ที่สุด (K-Nearest Neighbors / KNN) เป็นวิธีการใน Machine Learning ที่ใช้ในการจัดหมวดหมู่ข้อมูล (Classification) โดยพิจารณาความคล้ายคลึงของข้อมูล เมื่อมีข้อมูลใหม่เข้ามา โดยหลักการของ KNN คือการใช้ข้อมูลที่มีอยู่เพื่อการจำแนกประเภทข้อมูลใหม่ๆ โดยพิจารณาความคล้ายคลึงของข้อมูลใกล้เคียงที่สุด (nearest neighbors) โดยใช้วิธีการวัดระยะห่างเช่น Euclidean distance หรือ Manhattan distance ระหว่างข้อมูลที่สนใจกับข้อมูลในชุดข้อมูลที่มีอยู่แล้ว")

st.subheader("3.การสุ่มป่าไม้ ")
st.write("เการสุ่มป่าไม้(Random Forest) เป็นเทคนิคใน Machine Learning ที่ใช้วิธีการสร้างโมเดลหลายต้นไม้ Decision Tree เพื่อทำนายผลลัพธ์ที่ถูกต้อง โดยที่แต่ละต้นไม้จะถูกสร้างจากการสุ่มตัวอย่างข้อมูลและลักษณะของข้อมูลในแต่ละต้นไม้ และผลลัพธ์ที่ได้จะถูกรวมกันเพื่อให้ได้ผลลัพธ์สุดท้าย")

st.subheader("4.เครือข่ายประสาทเทีย ")
st.write("เครือข่ายประสาทเทียม (artificial neuron network: ANN) เป็นโมเดลคณิตศาสตร์ที่จำลองโครงสร้างและการทำงานของเครือข่ายประสาทในสมองมนุษย์. ANN ประกอบด้วยหน่วยประสาทเทียม (artificial neurons) ที่จำลองหน่วยประสาทในสมองและการเชื่อมต่อระหว่างหน่วยประสาทเหล่านั้น ๆ เพื่อประมวลผลข้อมูล")

st.subheader("5.กระบวนการแปลงข้อมูล ")
st.write("กระบวนการแปลงข้อมูล (Data Transformation) คือการแก้ไขหรือลบข้อมูลที่ผิดพลาดและไม่เกี่ยวข้อง, และจัดเรียงข้อมูลเข้าระบบให้อยู่ใน format ที่สะดวกต่อการวิเคราะห์ มีหลายวิธีเช่น")
st.write("คะแนนมาตรฐาน ")
st.write("ค่าเฉลี่ย")
st.write("รากที่สอง")
st.balloons()
