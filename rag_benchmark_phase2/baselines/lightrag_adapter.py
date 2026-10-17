import time

from .base import BaseAdapter
from llm_client import deepseek_generate



class LightRAGAdapter(BaseAdapter):

    name = "LightRAG"



    def generate(self, sample):

        start = time.time()


        context = ""


        for doc in sample.documents:

            if isinstance(doc, dict):

                context += (
                    doc.get("text", "")
                    + "\n"
                )

            else:

                context += (
                    str(doc)
                    + "\n"
                )


        prompt = f"""
Answer the question using the following knowledge.

Knowledge:
{context}

Question:
{sample.question}

Only output the answer.
"""


        result = deepseek_generate(
            prompt
        )


        return {

            "answer":
                result["answer"],

            "evidence":
                context,

            "input_tokens":
                result.get(
                    "input_tokens",
                    0
                ),

            "output_tokens":
                result.get(
                    "output_tokens",
                    0
                ),

            "latency":
                time.time()-start
        }