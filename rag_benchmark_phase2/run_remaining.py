import os
import subprocess



# ==========================
# 模型列表
# ==========================

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


# ==========================
# 数据集列表
# ==========================

datasets = [

    "musique_ans",
    "musique_full",
    "wiki",
    "hotpotqa"

]



# ==========================
# 真实数据路径
# ==========================

dataset_files = {


    "musique_ans":

        "datasets/musique_ans_answer.jsonl",


    "musique_full":

        "datasets/musique_full_answer.jsonl",


    "wiki":

        "datasets/wiki_answer.jsonl",


    "hotpotqa":

        "datasets/hotpotQA_answer.jsonl"

}




# ==========================
# 判断任务是否完成
# ==========================

def is_finished(model, dataset):


    result_file = os.path.join(

        "outputs",

        model,

        dataset,

        "predictions.jsonl"

    )


    # 文件不存在

    if not os.path.exists(result_file):

        return False



    # 空文件

    if os.path.getsize(result_file) < 100:

        return False



    # 检查是否有有效内容

    try:

        with open(

            result_file,

            "r",

            encoding="utf8"

        ) as f:


            line = f.readline()


            if line.strip():

                return True



    except:

        return False



    return False





# ==========================
# 开始执行
# ==========================


failed_tasks = []



for model in models:


    for dataset in datasets:



        if is_finished(model, dataset):


            print(

                "SKIP:",

                model,

                dataset

            )


            continue




        print("\n" + "="*50)

        print(

            "RUN:",

            model,

            dataset

        )

        print("="*50)




        cmd = [


            "python",


            "run_experiment.py",



            "--dataset",

            dataset,



            "--model",

            model,



            "--file",

            dataset_files[dataset],



            "--limit",

            "999999"

        ]



        result = subprocess.run(cmd)



        if result.returncode != 0:


            print(

                "FAILED:",

                model,

                dataset

            )


            failed_tasks.append(

                (model, dataset)

            )




# ==========================
# 输出总结
# ==========================


print("\n\n==========================")

print("Remaining experiment finished")

print("==========================")



if failed_tasks:


    print("\nFailed tasks:")


    for item in failed_tasks:

        print(

            item[0],

            item[1]

        )


else:


    print(

        "All tasks completed successfully."

    )