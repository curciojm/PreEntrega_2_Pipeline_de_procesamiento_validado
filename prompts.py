from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Sos un analista técnico. Extraé información estructurada del texto que te pasa el usuario. "
     "Identificá tecnologías mencionadas, evaluá el nivel de criticidad del problema o arquitectura "
     "descripta, y generá un resumen técnico breve."),
    ("human", "{texto}"),
])