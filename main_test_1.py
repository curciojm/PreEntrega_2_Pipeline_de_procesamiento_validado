# TEST 1:
# Salida para los tres proveedores

from logs import process_text
from schemas import get_model, EntidadesTecnicas
from prompts import prompt
import asyncio

# Orquestación
def build_chain(provider: str = "openai"):
    model = get_model(provider)
    structured_model = model.with_structured_output(EntidadesTecnicas)

    chain = (prompt | structured_model).with_retry(
        stop_after_attempt=3,
        wait_exponential_jitter=True,
    )
    return chain

async def main():

    texto_ejemplo = """
    Nuestra API en FastAPI está devolviendo timeouts intermitentes. El caché en Redis
    parece saturarse en picos de tráfico y las conexiones a PostgreSQL se agotan
    porque el pool está mal dimensionado. Esto está afectando a usuarios en producción.
    """

    for provider in ["openai", "anthropic", "gemini"]:
        try:
            resultado = await process_text(texto_ejemplo, provider=provider)
            print(f"\n--- {provider.upper()} ---")
            print(resultado.model_dump_json(indent=2))
        except Exception as e:
            print(f"\n--- {provider.upper()} falló: {e} ---")


if __name__ == "__main__":
    asyncio.run(main())