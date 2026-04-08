import os

def get_ai_response(agent_id, user_input):
    # นี่คือการจำลองการส่ง Prompt ไปยัง AI (สามารถเชื่อมต่อ API จริงได้ที่นี่)
    
    prompts = {
        1: "คุณคือ Mordee Concierge ต้อนรับคนไข้อย่างอบอุ่น...",
        2: "คุณคือ Triage Specialist ตรวจสอบ Red Flag (อาการวิกฤต)...",
        3: "คุณคือ Clinical Triage Analyst ตัดสินใจว่าควรพบหมอหรือดูแลตัวเอง...",
        4: "คุณคือ Diagnostic Classifier วิเคราะห์แผนกเฉพาะทาง...",
        5: "คุณคือ Matchmaker แนะนำหมอ 3 ท่านที่เหมาะสม...",
        6: "คุณคือ Medical Scribe สรุปการคุยเป็น SOAP Note...",
        7: "คุณคือ Medical Coder สกัดรหัส ICD-10...",
        8: "คุณคือ Pharmacology Assistant ร่างใบสั่งยา...",
        9: "คุณคือ Health Coach สร้าง Recovery Roadmap...",
        10: "คุณคือ Insurance Consultant แนะนำแผนประกันที่คุ้มค่า..."
    }
    
    selected_prompt = prompts.get(agent_id, "Agent ไม่ทำงาน")
    # ตัวอย่าง Return ค่ากลับ (ในงานจริงต้องส่ง prompt + user_input ไปที่ API)
    return f"**[AI Agent {agent_id} Response]**\n\nวิเคราะห์ข้อมูล: {user_input}\n\n(ผลลัพธ์จำลองตามหน้าที่ของ Agent)"
