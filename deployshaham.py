import streamlit as st
from PIL import Image
import pickle

model=pickle.load(open('diabetes_model.save','rb'))
scalar=pickle.load(open('diabetes_scaler.save','rb'))
encod=pickle.load(open('diabetics_encoder.save','rb'))
encod1=pickle.load(open('diabetics_encoder1.save','rb'))


def navigate_to(page):
    st.session_state.current_page = page

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

with st.sidebar:
    st.title('navigation')

    if st.button("home"):
        navigate_to("home")

    if st.button("symptoms"):
        navigate_to("symptoms")

    if st.button("complications"):
            navigate_to("complications") 

    if st.button("management and treatment"):
            navigate_to("management and treatment")      
   
    if st.button("prevention"):
            navigate_to("prevention")  

    if st.button("check whats your diabetics"):
            navigate_to(("check whats your diabetics")) 

if st.session_state.current_page == "home":
   st.title('Diabetics prediction')
   img = Image.open ("shahamsugar.jpg" )
   st.image(img, width=500)
   st.write()
   st.write(':point_right: diabetes is a disease tht occurs when your blood glucose,also is too high')
   st.write(':point_right: glucose is your bodys main source of energy.your body can make glucose but it also comes from the food you eat')
   st.write(':point_right: insulin is a hormone made by pancreas that helps glucose get into your body'
             "glucose then say your body and dosen't reach your cells.")
   st.write(':point_right: diabetes raises the risk for damage to the eyes,kedneys,nerves')

elif st.session_state.current_page == "symptoms" :
    st.title( 'symptoms of Diabetes')
    st.write("1. Increased thirst andhunger")
    st.write("2. Frequent urination")
    st.write("3. Unexplained weight loss")
    st.write("4. Fatigue")
    st.write("5. Blurred vision")
    st.write("6. Slow-healing sores")
    st.write("7. Frequent infections")

elif st.session_state.current_page == "complications":
    st. title( 'complications of Diabetes')
    st.write("If poorly managed, diabetes can lead to complications such as:") 
    st.write("1. Cardiovascular disease (heart attack, stroke)")
    st.write("2. Neuropathy (nerve damage)") 
    st.write("3. Nephropathy (kidney damage)")
    st.write("4. Retinopathy (eye damage leading to blindness)") 
    st.write("5. Foot problems (infections, ulcers)")

elif st.session_state.current_page == "management and treatment":
    st.title( 'management and treatment')
    st.write(":point_right: diet and Exercise: A balanced diet and regular physical activity are crucial for managing diets and diabetis. focus on alling whole grains, lean proteins, healthy fats, and plenty of fruits and vegetables. regular exercise can help improve insulin sensitivity and control blood sugar levels.")
    st.write(":point_right: Medications: Bepending on the type, medications can include insulin.")
    st.write(":point_right: Blood Sugar Menitoring: Regular monitoring of blood glucose level")
    st.write(":point_right: Education and Support: Education on diabetes management and support")

elif st.session_state.current_page == "prevention":
    st.title('prevention of diabetes')
    st.write("1.maintane a healthy weight")
    st.write("2.Follow a balanced diet rich in fruits, vegetables, whole grains, and lean ")
    st.write("3.exercise regularly")
    st.write("4.avoid tobacco use")
    st.write("5.limit alcohol consumption")
    st.write('Early detection and proper management are key to preventing complications asssociated')

elif st.session_state.current_page == "check whats your diabetics":
    st.title('diabetics prediction')
    
    Gender=st.radio('gender',['Female','Male'])
    gen=encod.transform([Gender])[0]

    age=st.text_input('age','text here')

    hypertension=st.radio('hypertension',['yes','no'])
    if hypertension=='yes':
        hypertension=1
    else:
        hypertension=0   

    heart_disease=st.radio('heart_disease',['yes','no'])
    if heart_disease=='yes':
        heart_disease=1
    else:
        heart_disease=0

    smoking_history=st.selectbox('smoking_history',['not current','former','no info','current','never','ever'])

    smoke_encod=encod1.transform([smoking_history])[0]


    bmi=st.text_input('BMI','text here')
    HbA1c_level=st.text_input('HbA1c_level','text here')
    bgl=st.text_input('blood glucose level','text here')      

    features=[gen,age,hypertension,heart_disease,smoke_encod,bmi,HbA1c_level,bgl]

    predict=st.button('click')
    if predict:
        pred=model.predict(scalar.transform([features]))

        if pred==1:
            st.header('indcating the presence of diabetes')
        else:
            st.header('no diabetes')