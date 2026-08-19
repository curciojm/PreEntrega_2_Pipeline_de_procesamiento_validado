# Experimentación con concurrencia para ejecutar los tres modelos en paralelo.
# Se utiliza asyncio.gather() para permitir que una falla individual
# no impida obtener los resultados de los demás modelos.

from chain import build_chain
import asyncio

# Cadenas independientes
chain_openai = build_chain("openai")
chain_anthropic = build_chain("anthropic")
chain_gemini = build_chain("gemini")

providers = ["openai", "anthropic", "gemini"]


async def main():

    texto_ejemplo = """
        Nuestra API en FastAPI está devolviendo timeouts intermitentes. El caché en Redis
        parece saturarse en picos de tráfico y las conexiones a PostgreSQL se agotan
        porque el pool está mal dimensionado. Esto está afectando a usuarios en producción.
    """

    texto_ambiguo = (
        "El sistema anda medio raro últimamente, no sé bien qué está pasando."
    )

    resultados = await asyncio.gather(
        chain_openai.ainvoke({"texto": texto_ejemplo}),
        chain_anthropic.ainvoke({"texto": texto_ejemplo}),
        chain_gemini.ainvoke({"texto": texto_ejemplo}),
        return_exceptions=True,
    )

    for provider, resultado in zip(providers, resultados):
        if isinstance(resultado, Exception):
            print(f"\n--- {provider.upper()} falló: {resultado} ---\n")
        else:
            print(f"\n--- {provider.upper()} ---\n")
            print(resultado.model_dump_json(indent=2))

    resultados = await asyncio.gather(
        chain_openai.ainvoke({"texto": texto_ambiguo}),
        chain_anthropic.ainvoke({"texto": texto_ambiguo}),
        chain_gemini.ainvoke({"texto": texto_ambiguo}),
        return_exceptions=True,
    )

    for provider, resultado in zip(providers, resultados):
        if isinstance(resultado, Exception):
            print(f"\n--- {provider.upper()} falló: {resultado} ---\n")
        else:
            print(f"\n--- {provider.upper()} ---\n")
            print(resultado.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())