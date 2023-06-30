
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open("C:/Users/HP/Desktop/project1/diabetes_model.sav","rb"))

heart_disease_model=pickle.load(open("C:/Users/HP/Desktop/project1/heart_model_rf.sav","rb"))
breast_cancer_model=pickle.load(open("C:/Users/HP/Desktop/project1/breast_model.sav","rb"))


selected=option_menu(menu_title="Multiple Disease Prediction System using ML",
                    options=["Diabetes",
                    "Heart",
                    "Breast"],
                    
                    
                    default_index=0,
                    orientation="vertical")
if (selected=="Diabetes"):
    st.title("Diabetes Prediction System using ML")
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)



    
    
if (selected=="Heart"):
    st.title("Heart Disease Prediction System using ML")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
     # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
if (selected=="Breast"):
    st.title("Breast CancerPrediction System using ML")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = st.number_input("radius_mean")
        
    with col2:
        texture_mean = st.number_input("texture_mean")
        
    with col3:
        perimeter_mean = st.number_input("perimeter_mean")
    with col1:
        area_mean = st.number_input("area_mean")
        
    with col2:
        smoothness_mean = st.number_input("smoothness_mean")
    
    with col3:
        compactness_mean = st.number_input("compactness_mean")
    with col1:
        concavity_mean= st.number_input("concavity_mean")
        
    with col2:
        concave_points_mean = st.number_input("concave points_mean")
        
    with col3:
        symmetry_mean = st.number_input("symmetry_mean")
        
    with col1:
        fractal_dimension_mean = st.number_input("fractal_dimension_mean")
        
    with col2:
        radius_se= st.number_input("radius_se")
        
    with col3:
        texture_se= st.number_input("texture_se")
    with col1:
        perimeter_se= st.number_input("perimeter_se")
        
    with col2:
        area_se= st.number_input("area_se")
        
    with col3:
        smoothness_se= st.number_input("smoothness_se")
    
    with col1:
        compactness_se= st.number_input("compactness_se")
        
    with col2:
        concavity_se= st.number_input("concavity_se")
        
    with col3:
        concave_points_se= st.number_input("concave points_se")
    with col1:
        symmetry_se = st.number_input("symmetry_se")
        
    with col2:
        fractal_dimension_se= st.number_input("fractal_dimension_se")
        
    
    with col3:
        radius_worst= st.number_input("radius_worst")
    with col1:
        texture_worst= st.number_input("texture_worst")
        
    with col2:
        perimeter_worst= st.number_input("perimeter_worst")
        
    with col3:
        area_worst= st.number_input("area_worst")
    with col1:
        smoothness_worst= st.number_input("smoothness_worst")
        
        
    with col2:
        compactness_worst= st.number_input("compactness_worst")
        
    with col3:
        concavity_worst= st.number_input("concavity_worst")
    with col1:
        concave_points_worst= st.number_input("concave points_worst")
        
    with col2:
        symmetry_worst= st.number_input("symmetry_worst")
        
    with col3:
        fractal_dimension_worst= st.number_input("fractal_dimension_worst")
        
    breast_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Prediction Test Result'):
        breast_prediction = breast_cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])                          
    
        if (breast_prediction[0] == 1):
          breast_diagnosis = 'The Breast cancer is Malignant'
        else:
          breast_diagnosis = 'The Breast Cancer is Benign'
        
    st.success(breast_diagnosis)