from schemas import get_model, EntidadesTecnicas
from prompts import prompt

# Orquestación
def build_chain(provider: str = "openai"):
    model = get_model(provider)
    structured_model = model.with_structured_output(EntidadesTecnicas)

    chain = (prompt | structured_model).with_retry(
        stop_after_attempt=3,
        wait_exponential_jitter=True,
    )
    return chain

##########################################################################
analysis = RunnableParallel(sentiment=sentiment_chain, topic=topic_chain)
# Hacelo con runeable a ver que onda
##########################################################################