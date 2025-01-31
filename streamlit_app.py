import streamlit as st
import openai

st.set_page_config(page_title="Kaomoji AI",page_icon="😶",layout="centered")
st.title("kaomoji ai")
st.write("Unleash the power of adorable text faces with our AI-powered kaomoji generator! Whether you’re feeling (╯°□°）╯︵ ┻━┻ or (｡♥‿♥｡), our app crafts the perfect expressive kaomoji for every mood. ")

# User API Key Input
openai_api_key = st.text_input("Enter your OpenAI API Key, which you can get [here](https://platform.openai.com/account/api-keys). ", type="password")

# Input text box
user_input = st.text_area("How are you feeling ('-')?", "")

# OpenAI API call function
def get_emojis(api_key, text):
    prompt = f"Return a single kaomoji that best represents the emotion conveyed in the following text: \n'{text}'\n\nOnly output the kaomoji without any explanation."
    try:
        client = openai.OpenAI(api_key=api_key)  # Create OpenAI client
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Ensure the correct model name
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Generate button
if st.button("(/￣ー￣)/~~☆’.･.･:★’.･.･:☆"):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key (눈_눈)")
    elif user_input.strip():
        with st.spinner("(╭ರ_•́)"):
            emoji_output = get_emojis(openai_api_key, user_input)
            st.subheader(emoji_output)
    else:
        st.warning("Please tell me your feeling (⇀‸↼‶)")

# Footer
st.markdown("<div style='text-align:center'>Built by Mitchell Tsai (˵ •̀ ᴗ •́ ˵ ) ✧ | © 2025 All Rights Reserved | Powered by OpenAI & Streamlit</div>", unsafe_allow_html=True)