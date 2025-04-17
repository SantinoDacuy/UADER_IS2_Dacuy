"""
Programa cliente para interactuar con modelos de lenguaje a través de la API de Together.
Este programa permite al usuario realizar consultas, recuperar consultas anteriores con
la tecla de flecha hacia arriba, y muestra las respuestas formateadas.
"""

import os
import platform
import sys

# Configuración para el manejo de historial de comandos según el sistema operativo
if platform.system() == 'Windows':
    try:
        import pyreadline3  # noqa: F401
    except ImportError:
        print("AVISO: Se recomienda instalar pyreadline3 para habilitar el historial de comandos:")
        print("pip install pyreadline3")
else:
    try:
        import readline  # noqa: F401
    except ImportError:
        print("AVISO: El módulo readline no está disponible en este sistema.")
        print("La funcionalidad de historial podría no funcionar correctamente.")

try:
    from together import Together
except ImportError:
    print("ERROR: No se pudo importar la biblioteca 'together'.")
    print("Instálela con: pip install together")
    sys.exit(1)


def configure_api_client():
    """
    Configura y retorna el cliente de la API Together.
    """
    api_key = os.environ.get("TOGETHER_API_KEY")
    if not api_key:
        print("No se encontró la variable de entorno TOGETHER_API_KEY")
        print("Configúrela con: set TOGETHER_API_KEY=tu_api_key (en Windows CMD)")
        sys.exit(1)

    return Together(api_key=api_key)


def get_completion(client, prompt, model="mistralai/Mixtral-8x7B-Instruct-v0.1"):
    """
    Envía una consulta al modelo de Together AI y devuelve la respuesta.
    """
    formatted_prompt = f"You: {prompt}"
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": formatted_prompt}
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as exc:  # noqa: BLE001
        print(f"Error al comunicarse con Together API: {exc}")
        return None


def get_user_input():
    """
    Solicita y obtiene la entrada del usuario.
    """
    try:
        return input("Ingrese su consulta (o presione flecha arriba para editar la anterior): ")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario")
        sys.exit(0)
    except Exception as exc:  # noqa: BLE001
        print(f"Error al obtener la consulta: {exc}")
        return ""


def process_query(user_input):
    """
    Procesa y valida la consulta del usuario.
    """
    try:
        if user_input.lower() in ['exit', 'quit', 'salir']:
            print("Finalizando programa...")
            return False

        if not user_input.strip():
            print("La consulta está vacía. Intente de nuevo.")
            return False

        print(f"You: {user_input}")
        return True

    except Exception as exc:  # noqa: BLE001
        print(f"Error inesperado al procesar la consulta: {exc}")
        return False


def main():
    """
    Función principal que ejecuta el ciclo de interacción con el usuario.
    """
    client = configure_api_client()

    while True:
        user_input = get_user_input()

        if not process_query(user_input):
            continue

        try:
            response = get_completion(client, user_input)
            if response is None:
                raise ConnectionError("No se pudo obtener respuesta del modelo")
            print(f"chatGPT: {response}")
        except ConnectionError as exc:
            print(f"Error de conexión: {exc}")
        except Exception as exc:  # noqa: BLE001
            print(f"Error inesperado al obtener respuesta: {exc}")


if __name__ == "__main__":
    main()
