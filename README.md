# Multiple-Disease-Prediction-Web-Application-using-Machine-Learning
This project is a web application that allows users to predict multiple diseases, including Diabetes, Heart Disease, and Breast Cancer, using machine learning models. 

**Project Structure**:
web_app.py: The main Python script that contains the code for the web application.
diabetes_model.sav: A trained machine learning model for diabetes prediction (pickle file).
heart_model_rf.sav: A trained machine learning model for heart disease prediction (pickle file).
breast_model.sav: A trained machine learning model for breast cancer prediction (pickle file).

**Requirements:**
   Python 3.x ,
   Jupyter Notebook ,
   Streamlit ,
   scikit-learn ,
   NumPy ,
   Pandas 

**Setup:**
1. Install the required dependencies by running the following command in your terminal or command prompt:
 -> pip install streamlit
 -> pip install scikit-learn
 -> pip install numpy
 -> pip install pandas
2. Place the web_app.py file and the three pickle files (diabetes_model.sav, heart_model_rf.sav, and breast_model.sav) in the same   
   directory.
   
**How to Run:**
Open your terminal or command prompt.
Navigate to the directory where the files are located.
Run the following command:
   _ **streamlit run web_app.py**__
The web application will start, and you will be provided with a URL to access the application locally. Open the URL in your web browser.

**How to Use:**
1. The web application will open with a title "Multiple Disease Prediction System using ML."
2. You can choose from three options: "Diabetes," "Heart," or "Breast."
3. Select the disease you want to predict by clicking on the corresponding option.
4. After selecting the disease, input the required data in the provided fields. The input fields will vary depending on the selected disease.
5. Click on the corresponding prediction button ("Diabetes Test Result," "Heart Disease Test Result," or "Breast Cancer Prediction Test Result").
6. The prediction result will be displayed below the prediction button.

**Roadmap:**
There are several possible enhancements that can be made to this project, including:
1. Adding more disease prediction options and corresponding machine learning models.
2. Improving the user interface and design of the web application.
3. Implementing data validation and error handling for user inputs.
4. Deploying the application to a web server for online access.
5. Adding additional features such as data visualization or personalized recommendations based on predictions.

**Contribution:**
Contributions to this project are welcome. If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request on the project's GitHub repository.

**Disclaimer:**
This application is intended for educational and informational purposes only. The prediction results should not be considered as medical advice. For accurate medical diagnoses and advice, consult a qualified healthcare professional.

**Contact:**
For any inquiries or questions, feel free to contact Madhavi Kapil at madhavikapil123@gmail.com.
