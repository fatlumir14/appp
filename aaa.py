import streamlit as st

st.set_page_config(page_title="Apple Pie", layout = "wide", page_icon=":heart:")
st.subheader ("Hey, you made it!!!")
st.title("Date Night?")
st.write ("Are you apple pie? Because every time I see you, I forget my diet. However, date first, regrets later?")

with st.container():
    st.write("---")
    st.header("Your Response")
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


st.write ("Come again tomorrow, you might be in for a surprise!!")        
