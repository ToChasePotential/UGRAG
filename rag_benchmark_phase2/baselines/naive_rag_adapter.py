from .base import BaseAdapter
from llm_client import deepseek_generate


class NaiveRAGAdapter(BaseAdapter):

    name = "NaiveRAG"


    def generate(self, sample):

        # =========================
        # 简单RAG：
        # 使用所有候选文档作为context
        # 后续再替换成embedding+top-k
        # =========================

        documents = []

        for doc in sample.documents:

            text = doc.get(
                "text",
                ""
            )

            if text:
                documents.append(text)


        context = "\n\n".join(
            documents
        )


        prompt = f"""
You are a question answering system.

Use the following retrieved documents
to answer the question.

Documents:
{context}


Question:
{sample.question}


Please answer directly.
"""


        result = deepseek_generate(
            prompt
        )


        return {

            "answer":
                result["answer"],

            "evidence":
                documents,

            "input_tokens":
                result["input_tokens"],

            "output_tokens":
                result["output_tokens"],

            "latency":
                result["latency"]
        }