from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import Se
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_clothing_brand_name_and_items(clothing_style):
    # Chain 1: Clothing Brand Name
    prompt_template_name = PromptTemplate(
        input_variables=['clothing_style'],
        template="I want to start a clothing brand focused on {clothing_style}. Suggest a catchy and creative name for it."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="brand_name")

    # Chain 2: Related Keywords/Categories
    prompt_template_items = PromptTemplate(
        input_variables=['brand_name'],
        template="""Suggest some related keywords or product categories for {brand_name}. 
                Return them as a comma-separated string (e.g., "T-shirts, Dresses, Jeans")."""
    )

    keywords_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="keywords")

    chain = SequentialChain(
        chains=[name_chain, keywords_chain],
        input_variables=['clothing_style'],
        output_variables=['brand_name', "keywords"]
    )

    response = chain({'clothing_style': clothing_style})
    return response

if __name__ == "__main__":
    print(generate_clothing_brand_name_and_items("Streetwear"))
