import streamlit as st
from agents import get_ai_response

# 1. ตั้งค่าหน้าตาแอป
st.set_page_config(page_title="Mordee AI Prototype", layout="wide")

# 2. ส่วน Sidebar (Navigation)
st.sidebar.title("🩺 Mordee Platform")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Dashboard", "AI Test Lab (10 Agents)", "Patient Records"])

# 3. หน้า AI Test Lab (ส่วนที่คุณต้องโชว์อาจารย์)
if page == "AI Test Lab (10 Agents)":
    st.header("🧪 Multi-Agent AI System Test Lab")
    st.write("ส่วนทดสอบฟังก์ชัน AI ทั้ง 10 รูปแบบตามแผนงาน Mordee")

    # แบ่งกลุ่ม Agent เป็น 2 คอลัมน์
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔹 Front-end & Triage")
        # ทดสอบ Agent 1-5
        agent_choice = st.selectbox("เลือก Agent ที่ต้องการทดสอบ:", 
                                     [1, 2, 3, 4, 5], 
                                     format_func=lambda x: f"Agent {x}: {['Concierge', 'Triage', 'Analyst', 'Classifier', 'Matchmaker'][x-1]}")
        
        user_input = st.text_area("กรอกอาการหรือข้อมูลคนไข้:", placeholder="เช่น มีไข้สูง ปวดหัวรุนแรง...")
        if st.button("ประมวลผล AI"):
            result = get_ai_response(agent_choice, user_input)
            st.info(result)

    with col2:
        st.subheader("🔸 Post-Consultation")
        # ทดสอบ Agent 6-10
        agent_choice_2 = st.selectbox("เลือก Agent ที่ต้องการทดสอบ:", 
                                       [6, 7, 8, 9, 10], 
                                       format_func=lambda x: f"Agent {x}: {['Scribe', 'Coder', 'Pharmacology', 'Health Coach', 'Insurance'][x-6]}")
        
        user_input_2 = st.text_area("กรอกข้อมูลหลังการตรวจ:", placeholder="เช่น ผลการคุยกับหมอ, สรุปอาการ...")
        if st.button("ประมวลผล AI (Backend)"):
            result = get_ai_response(agent_choice_2, user_input_2)
            st.success(result)

else:
    st.title("Mordee Dashboard")
    st.write("ยินดีต้อนรับเข้าสู่ระบบจัดการสุขภาพอัจฉริยะ")
