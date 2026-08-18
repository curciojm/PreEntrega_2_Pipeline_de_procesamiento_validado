import logging
from schemas import EntidadesTecnicas
from main import build_chain

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pipeline_extraccion")


async def process_text(text: str, provider: str = "openai") -> EntidadesTecnicas:
    chain = build_chain(provider)
    logger.info(f"[{provider}] Procesando texto ({len(text)} caracteres)...")

    try:
        resultado = await chain.ainvoke({"texto": text})
        logger.info(f"[{provider}] ✅ Extracción validada: {resultado.model_dump()}")
        return resultado
    except Exception as e:
        logger.error(f"[{provider}] ❌ Falló tras reintentos: {e}")
        raise