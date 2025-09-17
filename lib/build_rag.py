
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

template = """You are an assistant for an education institute called EduProvider.  
Use the provided CONTEXT to answer the user’s question clearly and concisely. 

Rules:
- Give one clear, concise answer only.  
- If the CONTEXT contains the answer, provide it directly.  
- Do NOT show reasoning, analysis, or explanations of what the context does/does not include.  
- If the CONTEXT does not contain the answer or the question is unrelated to courses, admissions, or student support, 
  politely redirect the user to call EduProvider at +1-333-111-2345.  
- Never prefix with 'Assistant:' or 'Answer:'. Just respond directly.  

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""

# Reusable text template for prompts
PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

def build_rag(vs):
    retriever = vs.as_retriever(search_kwargs={"k": 4}) # Retrieve the top 4 most relevant documents
    llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0) # LLM model with temperature 0 for deterministic responses

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff", # dump all retrieved documents into the prompt
        chain_type_kwargs={"prompt": PROMPT} # the prompt template defined above
        # fetches the revelant documents and uses the prompt template defined above to generate the final answer
    )
    return qa
