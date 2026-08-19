# Pipeline de Procesamiento Validado (Pre-Entrega 2)

Proyecto correspondiente a la Pre-Entrega 2 del curso de AI Engineering.

## Descripción

Pipeline de extracción de entidades técnicas a partir de texto no estructurado utilizando LangChain y Pydantic.

El proyecto implementa:

- Extracción estructurada de información técnica desde texto libre.
- Validación de las respuestas mediante modelos Pydantic.
- Clasificación del nivel de criticidad mediante un Enum.
- Generación de un resumen técnico.
- Composición de cadenas mediante LangChain Expression Language (LCEL).
- Uso de `ChatPromptTemplate` para mantener el prompt modular.
- Generación de salidas estructuradas mediante `.with_structured_output()`.
- Ejecución asíncrona mediante `.ainvoke()`.
- Manejo de errores y reintentos automáticos mediante `.with_retry()`.
- Logs para observar el procesamiento, la validación y los posibles errores.

Actualmente se incluyen implementaciones para:

- OpenAI
- Anthropic
- Gemini

## Requisitos

- Python 3.12+
- API keys de los proveedores que se quieran utilizar.

## Tecnologías utilizadas

- Python
- asyncio
- Pydantic
- LangChain
- LangChain Core
- LangChain OpenAI
- LangChain Anthropic
- LangChain Google GenAI
- OpenAI API
- Anthropic API
- Google Gemini API

## Variables de entorno

El proyecto utiliza las siguientes variables de entorno:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY`

Crear un archivo `.env` a partir de `.env.example` y completar las API keys correspondientes.

Las API keys reales no se incluyen en el repositorio.

## Ejecución

El script principal procesa dos textos de prueba:

1. Un texto técnico con información explícita sobre una arquitectura de software.
2. Un texto ambiguo para comprobar el comportamiento del pipeline frente a información poco específica.

Para ejecutar el pipeline:

```bash
python main.py
```

## Experimentación con concurrencia

Se incluye `main_concurrent.py` como una experimentación adicional sobre el pipeline principal.

Este script utiliza `asyncio.gather()` para ejecutar concurrentemente las cadenas correspondientes a OpenAI, Anthropic y Gemini sobre un mismo texto. Se utiliza `return_exceptions=True` para permitir que un error en un proveedor no interrumpa la ejecución de los demás


Para ejecutarla:

```bash
python main_concurrent.py
```

## Estructura del proyecto

```
├── .env.example         # Ejemplo de variables de entorno
├── .gitignore
├── chain.py             # Construcción de la cadena LCEL y lógica de reintentos
├── logging_config.py    # Configuración del sistema de logs
├── main_concurrent.py   # Experimentación adicional con concurrencia
├── main.py              # Punto de entrada principal y prueba del pipeline
├── models.py            # Configuración y selección de los modelos LLM
├── prompt_config.py     # ChatPromptTemplate utilizado por el pipeline
├── README.md
├── requirements.txt     # Dependencias del proyecto
└── schemas.py           # Modelos y validaciones con Pydantic
```

## Sobre el código

El proyecto fue desarrollado tomando como referencia:

- Código base proporcionado por el profesor como guía para la Pre-Entrega 2.
- Ejemplos y contenidos incluidos en el temario de la plataforma sobre LangChain y LCEL.
- Documentación oficial y recursos disponibles en Internet.
- ChatGPT como herramienta de asistencia durante el desarrollo.