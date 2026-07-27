import ollama


def ask_qwen(prompt: str) -> str:
    """
    Send a prompt to the local Qwen model and return the response.
    """

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]