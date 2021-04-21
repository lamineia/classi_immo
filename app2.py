import streamlit as st
import pickle



random_f=pickle.load(open('gradient_boosting_model.pkl','rb'))


def predict_loan(num):
    if num==0:
        return 'Bad'
    elif num==1:
        return 'Good'
    else:
        return 'Virginica'
def main():
    st.title("Iris Classification")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Random Forest', 'Decision Tree']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    sl=st.slider('Select Sepal Length', 0.0, 10.0)
    sw=st.slider('Select Sepal Width', 0.0, 10.0)
    pl=st.slider('Select Petal Length', 0.0, 10.0)
    pw=st.slider('Select Petal Width', 0.0, 10.0)
    inputs=[[sl,sw,pl,pw]]
    if st.button('Classify'):
        if option=='Random Forest':
            st.success(predict_loan(random_f.predict(inputs)))
        else:
            st.success(predict_loan(decision_t.predict(inputs)))

if __name__=='__main__':
    main()