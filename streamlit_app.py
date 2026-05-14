import streamlit as st
import google.generativeai as genai

# إعدادات واجهة مستشارك في التأمينات والمعاشات
st.set_page_config(page_title="مستشارك في التأمينات والمعاشات", layout="wide")

# تفعيل المفتاح السري الخاص بسيادتكم
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# استخدام الإصدار الأحدث المستقر (لحل مشكلة الخطأ التقني 404)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# واجهة البرنامج بهويتك المهنية
st.title("⚖️ مستشارك في التأمينات والمعاشات")
st.subheader("الإدارة العامة للشؤون القانونية - ديوان عام منطقة البحيرة")
st.write("تحت إشراف الأستاذ/ وليد حماد")

# منطقة رفع ملفات الـ PDF
uploaded_file = st.file_uploader("ارفع ملف القانون أو التعليمات (PDF)", type="pdf")

# منطقة السؤال والتحليل القانوني
user_input = st.text_input("اكتب سؤالك القانوني هنا:")

if user_input and uploaded_file:
    with st.spinner('جاري فحص المستندات واستخراج الرأي القانوني...'):
        try:
            pdf_data = uploaded_file.read()
            # إرسال الملف والسؤال للذكاء الاصطناعي
            response = model.generate_content([
                "أنت خبير قانوني في التأمينات والمعاشات المصرية. أجب بدقة من واقع الملف المرفق.",
                {"mime_type": "application/pdf", "data": pdf_data},
                user_input
            ])
            st.markdown("### 📝 الرد القانوني:")
            st.success(response.text)
        except Exception as e:
            st.error(f"حدث خطأ تقني: {e}")
elif user_input and not uploaded_file:
    st.warning("رجاءً ارفع ملف الـ PDF أولاً ليتمكن البرنامج من تحليله.")

st.markdown("---")
st.caption("مع تحيات وليد حماد - الإدارة العامة للشؤون القانونية")
