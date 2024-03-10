import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import ctransformers


#function to get response from the llama 2 model

def getLlamaResponse(input_text,no_words,blog_style):
    
    ### LLama2 model
    llm = ctransformers.CTransformers(model="D:\Llama 2 Project\models\llama-2-7b-chat.Q8_0.gguf",
                                      model_file='llama',
                                      config={'max_new_tokens': 256,'temperature':0.01}
                                      )

    # Prompt Template
    template =  """
                Write a blog for {blog_style} job profile on the topic "{input_text}" within {no_words} words.
                """
    
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                            template=template)
    
    # Generate the response from the model
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    # print(response)
    return response

st.set_page_config( page_title="Generate Blogs",
                    page_icon="✍️", 
                    layout="centered", 
                    initial_sidebar_state="collapsed" )

st.header("Generate Blogs")

input_text = st.text_input("Enter the Blog Topic")
##creating 2 more columns for addional feilds
col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Number of words")

with col2:
    blog_style = st.selectbox("Writing the blog for",["Researchers","Data Scientists","Engineers","Common People"])


submit = st.button("Generate Blog")


# Final response
if submit:
    st.write(getLlamaResponse(input_text,no_words,blog_style))