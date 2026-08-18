from schemas import EntidadesTecnicas
from models import get_model
from logging_config import logger
from chain import build_chain
import asyncio  


# Orquestación
async def process_text(text: str, provider: str = "openai") -> EntidadesTecnicas:
        chain = build_chain(provider)
        logger.info(f"[{provider}] Procesando texto ({len(text)} caracteres)...\n")

        try:
            resultado = await chain.ainvoke({"texto": text})
            logger.info(f"[{provider}] ✅ Extracción validada: {resultado.model_dump()}\n")
            return resultado
        except Exception as e:
            logger.error(f"[{provider}] ❌ Falló tras reintentos: {e}\n")
            raise


async def main():
    texto_ejemplo = """
        Nuestra API en FastAPI está devolviendo timeouts intermitentes. El caché en Redis
        parece saturarse en picos de tráfico y las conexiones a PostgreSQL se agotan
        porque el pool está mal dimensionado. Esto está afectando a usuarios en producción.
        """
    texto_ambiguo = "El sistema anda medio raro últimamente, no sé bien qué está pasando."

    for provider in ["openai", "anthropic", "gemini"]:
        try:
            resultado = await process_text(texto_ejemplo, provider=provider)
            print(f"\n--- {provider.upper()} ---\n")
            print(resultado.model_dump_json(indent=2))
        except Exception as e:
            print(f"\n--- {provider.upper()} falló: {e} ---\n")

    for provider in ["openai", "anthropic", "gemini"]:
        try:
            resultado = await process_text(texto_ambiguo, provider=provider)
            print(f"\n--- {provider.upper()} ---\n")
            print(resultado.model_dump_json(indent=2))
        except Exception as e:
            print(f"\n--- {provider.upper()} falló: {e} ---\n")        

if __name__ == "__main__":
    asyncio.run(main())