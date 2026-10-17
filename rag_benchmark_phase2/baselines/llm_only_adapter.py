from .base import BaseAdapter
from llm_client import deepseek_generate


class LLMOnlyAdapter(BaseAdapter):

    name = "LLM_without_Retrieval"

    def generate(self, sample):

        prompt = f"""
Answer the question directly.

Question:
{sample.question}

Answer:
"""

        result = deepseek_generate(prompt)

        return {
            "answer": result["answer"],
            "evidence": [],
            "input_tokens": result["input_tokens"],
            "output_tokens": result["output_tokens"],
            "latency": result["latency"]
        }