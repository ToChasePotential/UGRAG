import os
import time
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


def deepseek_generate(prompt):

    start = time.time()


    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.0

    )


    latency = time.time() - start


    answer = response.choices[0].message.content


    usage = response.usage


    return {

        "answer": answer,

        "input_tokens":
            usage.prompt_tokens,

        "output_tokens":
            usage.completion_tokens,

        "total_tokens":
            usage.total_tokens,

        "latency":
            latency

    }