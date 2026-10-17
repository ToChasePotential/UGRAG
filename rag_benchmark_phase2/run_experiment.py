from datasets.loader import load_jsonl


from baselines.llm_only_adapter import LLMOnlyAdapter
from baselines.naive_rag_adapter import NaiveRAGAdapter
from baselines.graphrag_adapter import GraphRAGAdapter
from baselines.lightrag_adapter import LightRAGAdapter
from baselines.faithfulrag_adapter import FaithfulRAGAdapter
from baselines.th_rag_adapter import THRAGAdapter
from baselines.s2g_rag_adapter import S2GRAGAdapter
from baselines.q_rag_adapter import QRAGAdapter
from baselines.hipporag2_adapter import HippoRAG2Adapter
from baselines.uniongraph_adapter import UnionGraphAdapter


from evaluators.em_f1 import exact_match, f1


import argparse
import json
import os



def get_model(name):

    models = {

        "LLM_without_Retrieval":
            LLMOnlyAdapter,

        "NaiveRAG":
            NaiveRAGAdapter,

        "GraphRAG":
            GraphRAGAdapter,

        "LightRAG":
            LightRAGAdapter,

        "FaithfulRAG":
            FaithfulRAGAdapter,

        "TH-RAG":
            THRAGAdapter,

        "S2G-RAG":
            S2GRAGAdapter,

        "Q-RAG":
            QRAGAdapter,

        "HippoRAG2":
            HippoRAG2Adapter,

        "UnionGraph-RAG":
            UnionGraphAdapter

    }


    if name not in models:

        raise ValueError(
            f"Unknown model: {name}"
        )


    return models[name]()



def load_finished_ids(output_file):

    """
    读取已经完成的样本id
    """

    finished = set()


    if not os.path.exists(output_file):

        return finished


    if os.path.getsize(output_file) == 0:

        return finished


    with open(
        output_file,
        "r",
        encoding="utf8"
    ) as f:


        for line in f:

            try:

                data = json.loads(line)

                finished.add(
                    data["id"]
                )

            except:

                continue


    return finished




def main():


    parser = argparse.ArgumentParser()


    parser.add_argument(
        "--dataset",
        required=True
    )


    parser.add_argument(
        "--file",
        required=True
    )


    parser.add_argument(
        "--model",
        required=True
    )


    parser.add_argument(
        "--limit",
        type=int,
        default=None
    )


    parser.add_argument(
        "--answer_file",
        default=None
    )


    args = parser.parse_args()



    samples = load_jsonl(

        args.file,

        args.dataset,

        args.answer_file

    )



    if args.limit is not None:

        samples = samples[:args.limit]



    print(
        "Dataset:",
        args.dataset
    )


    print(
        "Samples:",
        len(samples)
    )


    print(
        "Running:",
        args.model
    )



    model = get_model(
        args.model
    )



    output_dir = os.path.join(

        "outputs",

        args.model,

        args.dataset

    )


    os.makedirs(

        output_dir,

        exist_ok=True

    )



    output_file = os.path.join(

        output_dir,

        "predictions.jsonl"

    )



    # ==========================
    # 读取已经完成的样本
    # ==========================

    finished_ids = load_finished_ids(
        output_file
    )


    print(
        "Already finished:",
        len(finished_ids)
    )



    # ==========================
    # 追加写入，不覆盖
    # ==========================

    with open(

        output_file,

        "a",

        encoding="utf8"

    ) as f:



        for i, sample in enumerate(samples):


            # ----------------------
            # 跳过已经完成的数据
            # ----------------------

            if sample.sample_id in finished_ids:


                print(
                    "Skip:",
                    sample.sample_id
                )


                continue



            print(
                "\n================"
            )


            print(
                "Sample:",
                i+1
            )


            print(
                "Question:",
                sample.question
            )



            try:


                result = model.generate(

                    sample

                )



                answer = result.get(

                    "answer",

                    ""

                )



                record = {


                    "dataset":

                        args.dataset,


                    "model":

                        args.model,


                    "id":

                        sample.sample_id,


                    "question":

                        sample.question,


                    "prediction":

                        answer,


                    "reference_answer":

                        sample.reference_answer,


                    "EM":

                        exact_match(

                            answer,

                            sample.reference_answer

                        ),



                    "F1":

                        f1(

                            answer,

                            sample.reference_answer

                        ),



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

                        result.get(

                            "latency",

                            0

                        )

                }



                f.write(

                    json.dumps(

                        record,

                        ensure_ascii=False

                    )

                    + "\n"

                )


                # 立即保存

                f.flush()



                print(
                    record
                )



            except Exception as e:


                print(
                    "FAILED:",
                    sample.sample_id,
                    e
                )


                continue




    print(
        "\nFinished"
    )


    print(
        "Saved:",
        output_file
    )




if __name__ == "__main__":

    main()