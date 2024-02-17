import streamlit as st

st.set_page_config(page_title="HEY", layout = "wide")
st.subheader ("Hi, this is Fatlum")
st.title("What would you like to do tonight?")
st.write ("Are you down for dinner")
st.write ("I am really pump up for it")

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
        