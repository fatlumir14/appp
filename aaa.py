import streamlit as st

st.set_page_config(page_title="Only For You", layout = "wide", page_icon=":heart:")
st.subheader ("I am happy to see you here")
st.title("Date Night?")
st.write ("I have been thinking about you, would you like to go out in a date?")

with st.container():
    st.write("---")
    st.header("Your response")
    st.write ("##")
    contact_form="""
    <form action= "https://formsubmit.co/ffatlumrexhepi@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value ="false">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your response" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
        
