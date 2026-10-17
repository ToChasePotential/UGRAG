import os
import subprocess



models = [

    "LLM_without_Retrieval",

    "NaiveRAG",

    "GraphRAG",

    "LightRAG",

    "FaithfulRAG",

    "TH-RAG",

    "S2G-RAG",

    "Q-RAG",

    "HippoRAG2",

    "UnionGraph-RAG"

]



datasets = {


    "musique_ans":
    {
        "file":
        "datasets/musique_ans_dev_head.jsonl",

        "answer":
        "datasets/musique_ans_answer.jsonl"
    },


    "musique_full":
    {
        "file":
        "datasets/musique_full_dev_head.jsonl",

        "answer":
        "datasets/musique_full_answer.jsonl"
    },


    "wiki":
    {
        "file":
        "datasets/wiki_dev_head.jsonl",

        "answer":
        "datasets/wiki_answer.jsonl"
    },


    "hotpotqa":
    {
        "file":
        "datasets/train-00000-of-00002.head389.jsonl",

        "answer":
        "datasets/hotpotQA_answer.jsonl"
    }

}




def is_finished(model, dataset):


    output_file = (

        "outputs/"
        + model
        + "/"
        + dataset
        + "/predictions.jsonl"

    )


    if not os.path.exists(output_file):

        return False



    with open(
        output_file,
        encoding="utf-8"
    ) as f:

        lines = f.readlines()



    # 500条认为完成

    if len(lines) >= 500:

        return True


    return False





for model in models:


    for dataset, config in datasets.items():


        print("\n==============================")



        if is_finished(
            model,
            dataset
        ):


            print(
                "Skip finished:",
                model,
                dataset
            )

            continue



        print(
            "Running:",
            model,
            dataset
        )



        cmd = [


            "python",


            "run_experiment.py",



            "--model",

            model,



            "--dataset",

            dataset,



            "--file",

            config["file"],



            "--answer_file",

            config["answer"],



            "--limit",

            "500"


        ]



        try:


            subprocess.run(

                cmd,

                check=True

            )


        except subprocess.CalledProcessError:


            print(

                "FAILED:",

                model,

                dataset

            )



print("\n==============================")

print("ALL FINISHED")