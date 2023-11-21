import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="Chutima Datascience Project",
    page_icon= ":bar_chart:",
)

st.header("การทำนายคุณสมบัติในการขอสินเชื่อบ้าน 🏦 🌃 ")
st.image('pic/home.jpg')

st.subheader("1.หลักการและเหตุผล")
st.write("การพิจารณาที่บุคคลว่าสามารถสมัครสินเชื่อบ้านได้หรือไม่ มีผลต่อการเริ่มต้นทำชีวิตใหม่หรือขยายกิจการ การเช็คความเสี่ยงของผู้กู้ยืม และการประเมินความสามารถในการชำระหนี้เป็นขั้นตอนสำคัญของกระบวนการอนุมัติสินเชื่อบ้าน หากผู้กู้สามารถเตรียมตัวสำหรับการรับพิจารณาเพื่ออนุมัติจะทำให้มีโอกาสในการได้รับการอนุมัติมากขึ้น ")

st.subheader("2.วัตถุประสงค์")
st.write("1.เพื่อใช้เทคนิคเหมืองข้อมูลในการแปลงชุดข้อมูลการขอสินเชื่อบ้านให้อยู่ในรูปแบบที่เหมาะสมกับเทคนิคที่นำมาใช้ใช้จำแนกประเภทข้อมูล")
st.write("2.เพื่อเปรียบเทียบประสิทธิภาพของการจำแนกประเภทการขอสินเชื่อบ้านของชุดข้อมูลการแปลงข้อมูลในรูปแบบต่างๆ")
st.write("3.เพื่อใช้ประสิทธิภาพที่ดีที่สุดสำหรับนำไปพัฒนาเป็นระบบต้นแบบสำหรับสนับสนุนการพิจารณาคุณสมบัติการขอสินเชื่อบ้าน")
st.balloons()