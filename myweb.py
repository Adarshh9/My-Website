import streamlit as st
from streamlit_lottie import st_lottie
import requests 
from PIL import Image

st.set_page_config(page_title='My Webpage', page_icon=':tada:', layout='wide')

def load_lotties(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lotties("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")


with st.container(): 
    st.subheader('Hi, I am Adarsh :wave:')
    st.title('A Data Analyst From INDIA 🇮🇳')
    st.write('I am passionate about finding ways to use Python and streamlit to be more efficient and effective.')

with st.container():
    st.write('___')
    left_column,right_column = st.columns(2)
    with left_column:
        st.title('WHAT I DO')
        st.write('I am student at Thakur College Of Engineering And Technology')
        st.write('I am studying in Artificial Inteligence and Data Science')
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    
image1 = Image.open('index.jpeg')
image2 = Image.open('index1.jpeg')

with st.container():
    st.write('__________')
    st.header('My Projects')
    st.write('##')
    
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(image1,width=450)
    with text_col:
        st.header('JARVIS AI')
        st.write('It is a software that recoognize the user voice and do the instructed work.')
        st.write('It plays music. It opens website. It opens apps.')
        st.write('[Learn More>](https://github.com/Adarshh9/JARVIS-AI)')

with st.container():
    st.write('##')
    
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(image2, width=450)
    with text_col:
        st.header('Library Management Software')
        st.write('It manipulates the data of book.')
        st.write('It adds book. It shows books.')
        st.write('[Learn More>](https://github.com/Adarshh9/python-project/tree/main/Library%20Management%20Software)')

with st.container():
    st.write('-----')
    st.subheader("Get in touch with me !")
    st.write('##')
    contact_form =  """
            <form action="https://formsubmit.co/ashadarsh926@email.com" method="POST">
                 <input type="hidden" name="captcha" value ="false">
                 <input type="text" name="name" placeholder="Your name here" required>
                 <input type="email" name="email" placeholder="Your email here"required>
                 <textarea name="message" placeholder="Your message here" required></textarea>
                 <button type="submit">Send</button>
            </form> 
    
                        """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()