import streamlit as st
import pickle
import pandas as pd

file = pickle.load(open("rfc.pkl",'rb'))

st.title('Bank Customers')
st.sidebar.header('Interviewee\'s Data')

#creating a function for the values
def report():
    country = st.sidebar.selectbox('Select country', ['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
    if(country == 'Kenya'):
        country = 0,
    elif(country == 'Rwanda'):
        country = 1,
    elif(country == 'Tanzania'):
        country = 2,
    else:
        country = 3
    location_type = st.sidebar.selectbox('Select location_type', ('Rural', 'Urban'))
    if(location_type == 'Rural'):
        location_type = 0,
    else:
        location_type = 1
    cellphone_access = st.sidebar.selectbox('Does the interviewee have cellphone access?', ('Yes','No'))
    if(cellphone_access == 'Yes'):
        cellphone_access = 1,
    else:
        cellphone_access = 0
    gender_of_respondent = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    if(gender_of_respondent == 'Male'):
        gender_of_respondent = 1,
    else:
        gender_of_respondent = 0
    marital_status = st.sidebar.selectbox('Marital Status', ('Married/Living together', 'Widowed', 'Single/Never Married',
       'Divorced/Seperated', 'Dont know'))
    if(marital_status == 'Married/Living together'):
        marital_status = 2,
    elif(marital_status == 'Widowed'):
        marital_status = 4,
    elif(marital_status == 'Single/Never Married'):
        marital_status = 3,
    elif(marital_status == 'Divorced/Seperated'):
        marital_status = 0,
    else:
        marital_status = 1
    education_level = st.sidebar.selectbox('Education Level', ('Secondary education', 'No formal education',
       'Vocational/Specialised training', 'Primary education',
       'Tertiary education', 'Other/Dont know/RTA'))
    if(education_level == 'Secondary education'):
        education_level = 3,
    elif(education_level == 'No formal education'):
        education_level = 0,
    elif(education_level == 'Vocational/Specialised training'):
        education_level = 5,
    elif(education_level == 'Primary education'):
        education_level = 2,
    elif(education_level == 'Tertiary education'):
        education_level = 4,
    else:
        education_level = 1
    job_type = st.sidebar.selectbox('Select job type', ('Self employed', 'Government Dependent','Formally employed Private', 'Informally employed',
       'Formally employed Government', 'Farming and Fishing', 'Remittance Dependent', 'Other Income',
       'Dont Know/Refuse to answer', 'No Income'))
    if(job_type == 'Self employed'):
        job_type = 9,
    elif(job_type == 'Government Dependent'):
        job_type = 4,
    elif(job_type == 'Formally employed Private'):
        job_type = 3,
    elif(job_type == 'Informally employed'):
        job_type = 5,
    elif(job_type == 'Formally employed Government'):
        job_type = 2,
    elif(job_type == 'Farming and Fishing'):
        job_type = 1,
    elif(job_type == 'Remittance Dependent'):
        job_type = 8,
    elif(job_type == 'Dont Know/Refuse to answer'):
        job_type = 0,
    elif(job_type == 'Other Income'):
        job_type = 7,
    else:
        job_type = 6

    # creating a dictionary of the values
    report_data = {
        'country': country,
        'location_type': location_type,
        'cellphone_access': cellphone_access,
        'gender_of_respondent': gender_of_respondent,
        'marital_status': marital_status,
        'education_level': education_level,
        'job_type': job_type
    }
    report_data = pd.DataFrame(report_data, index = [0])
    return report_data
user_data = report()

st.subheader('Interviewee data summary')
st.write(user_data)

bank_account = file.predict(user_data)
if (st.sidebar.button('Predict Probability to Own an Account')):
    st.text("Interviewee probability to own a bank account is {}.".format(bank_account))


st.subheader('Probability to Own a Bank Account')
if(bank_account == 1):
    st.success('The interviewee will likely have a bank account')
else:
    st.warning('The interviewee doesnt have or use a bank account')
