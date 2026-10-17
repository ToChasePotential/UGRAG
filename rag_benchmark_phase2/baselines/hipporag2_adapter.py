import time

from .base import BaseAdapter
from llm_client import deepseek_generate



class HippoRAG2Adapter(BaseAdapter):

    name = "HippoRAG2"



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

You are HippoRAG2.

Use memory-inspired retrieval reasoning
to answer the question based on evidence.


Evidence:

{context}


Question:

{sample.question}


Only output the final answer.

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