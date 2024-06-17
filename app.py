import streamlit as st
import cohere
from colorama import init, Fore, Style

init()

# Set your Cohere API key here
api_key = 'set your api here.'
co = cohere.Client(api_key)

def generate_response(prompt, temperature=0.8):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=1000,
        temperature=temperature
    )
    return response.generations[0].text.strip()

def format_response(response):
    words = response.split()
    important_chars = ['important'] 

    formatted_text = []
    for word in words:
        if any(char in word.lower() for char in important_chars):
            formatted_text.append(f"{Fore.RED}{Style.BRIGHT}{word}{Style.RESET_ALL}")
        else:
            formatted_text.append(word)

    return ' '.join(formatted_text)

# web application start from here.
def main():
    st.title("Cohere Text Generation with Streamlit")

   
    prompt = st.text_area("Ask me anything:")
    if st.button("Generate Response"):
        with st.spinner("Generating..."):
            response = generate_response(prompt)
            st.success("Response generated!")
            st.subheader("Response:")
            formatted_response = format_response(response)
            st.markdown(formatted_response, unsafe_allow_html=True) 
            
if __name__ == "__main__":
    main()
