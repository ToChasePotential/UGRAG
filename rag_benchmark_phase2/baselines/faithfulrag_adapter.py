import time

from .base import BaseAdapter
from llm_client import deepseek_generate



class FaithfulRAGAdapter(BaseAdapter):

    name = "FaithfulRAG"



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

You are a faithful question answering system.

Answer ONLY using the provided evidence.

Evidence:

{context}


Question:

{sample.question}


Give a concise answer.

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