import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

# Load environment variables (set OPENAI_API_KEY and OPENAI_API_BASE in .env)
load_dotenv()

# Configure Azure OpenAI Service API
openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_base)

api_base = openai.api_base
api_version = openai.api_version
index_name: str = "embeddings"
model: str = os.getenv('OPENAI_EMBEDDINGS_ENGINE_DOC', "text-embedding-ada-002")
deployment_name: str = os.getenv("OPENAI_ENGINE", os.getenv("OPENAI_ENGINES", "text-davinci-003"))
deployment_type: str = os.getenv("OPENAI_DEPLOYMENT_TYPE", "Text")
temperature: float = float(os.getenv("OPENAI_TEMPERATURE", 0.7))
max_tokens: int = int(os.getenv("OPENAI_MAX_TOKENS", -1))
prompt = PROMPT if custom_prompt == '' else PromptTemplate(template=custom_prompt, input_variables=["summaries", "question"])
vector_store_type = os.getenv("VECTOR_STORE_TYPE")