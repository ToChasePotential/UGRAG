import sys
import os
import time

from .base import BaseAdapter
from llm_client import deepseek_generate


class UnionGraphAdapter(BaseAdapter):

    name = "UnionGraph-RAG"


    def __init__(self):

        current_dir = os.path.dirname(
            os.path.abspath(__file__)
        )

        root_dir = os.path.dirname(
            os.path.dirname(current_dir)
        )

        uniongraph_path = os.path.join(
            root_dir,
            "UnionGraph-RAG",
            "chugao_fixed_v6",
            "chugao"
        )

        if uniongraph_path not in sys.path:
            sys.path.insert(
                0,
                uniongraph_path
            )

        from main import uniongraph_rag_pipeline

        self.pipeline = uniongraph_rag_pipeline



    def generate(self, sample):

        start = time.time()


        docs = []

        for d in sample.documents:

            if isinstance(d, dict):

                docs.append(
                    d.get("text", "")
                )

            else:

                docs.append(
                    str(d)
                )


        # UnionGraph evidence organization

        result = self.pipeline(

            x_ins="",

            x_doc=docs,

            x_que=sample.question,

            llm_generate=None

        )


        # 获取组织后的证据

        evidence = str(result)



        # DeepSeek生成最终答案

        prompt = f"""

Answer the question using the evidence.

Evidence:
{evidence}


Question:
{sample.question}


Only output the final answer.

"""


        llm_result = deepseek_generate(
            prompt
        )


        latency = time.time() - start



        return {

            "answer":
                llm_result["answer"],

            "evidence":
                result,

            "input_tokens":
                llm_result.get(
                    "input_tokens",
                    0
                ),

            "output_tokens":
                llm_result.get(
                    "output_tokens",
                    0
                ),

            "latency":
                latency
        }