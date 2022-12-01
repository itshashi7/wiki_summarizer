import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Content Generator", page_icon=":speech_balloon:", layout = "wide")
st.title("Content Generator")
st.write("> Generate content from wikipedia articles.\n\n> Shorten the content as your wish.")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_S9kP4W.json") 

lottie_info = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_jlyeehso.json") 

lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_v7gj8hb1.json")

with st.container():
    left_column,right_column =st.columns(2)
    with left_column:
        st.sidebar.subheader("Guide")
        expander = st.sidebar.expander('How to Generate',expanded=False)
        with expander:
            st_lottie(lottie_info, height =50, key="info")
            st.subheader("Input Link: ")
            st.info("Input a wikipedia link related to the content you wish to generate.")  
            st.subheader("Summarize slider: ")
            st.info("Here you can pick the level from 1 to 10. \n\n> 1 being low summerized content. \n\n> 10 being highly summerized content. \n\n> You can pick any level between the range.")  
            st.subheader("Content")
            st.info("Finally you can view the content which is generator from Content section.")  
        
        contact_form = """
        <form action="https://formsubmit.co/itzhashi7@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Details of your problem"></textarea>
     <button type="submit">Send</button>
</form> 
""" 
        st.sidebar.subheader("Contact")
        with st.sidebar:
            st_lottie(lottie_contact, height =200, key="contact")
        st.sidebar.write(contact_form,unsafe_allow_html=True)  
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        local_css("style.css")
            
        
        
        
        st.markdown("---")
        with st.form("my_form"):
            linkFromUser = st.text_input('Paste the link here:')
            summarizationLevel = st.slider('Summarize: ', 1, 10,5)
            if(summarizationLevel==1):  
                percent=0.01
            elif(summarizationLevel==100):  
                percent=0.1
            else:
                percent=summarizationLevel/100
        

            # Every form must have a submit button.
            submitted = st.form_submit_button("Generate")
        
    with right_column:
        
        st_lottie(lottie_coding, height =550, key="wikipedia")
        
with st.container():
    
     st.markdown("---")
     st.header("Content: ")
     if submitted:
       
        import main
        import hydralit_components as hc
        import time
        with hc.HyLoader('',hc.Loaders.pulse_bars,):
           main.generate(linkFromUser,percent)
        f = open(r"output.txt",encoding="utf8")
        st.write(f.read())
