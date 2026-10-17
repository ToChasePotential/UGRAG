import os
import json
import pandas as pd


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


datasets = [
    "musique_ans",
    "musique_full",
    "wiki",
    "hotpotqa"
]


results = []


for dataset in datasets:

    for model in models:

        file = os.path.join(
            "outputs",
            model,
            dataset,
            "predictions.jsonl"
        )

        if not os.path.exists(file):
            print("Missing:", file)
            continue


        ems = []
        f1s = []


        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                item = json.loads(line)

                ems.append(
                    item.get("EM",0)
                )

                f1s.append(
                    item.get("F1",0)
                )


        results.append({

            "Dataset":dataset,

            "Model":model,

            "EM":
                round(
                    sum(ems)/len(ems)*100,
                    2
                ),

            "F1":
                round(
                    sum(f1s)/len(f1s)*100,
                    2
                )

        })


df = pd.DataFrame(results)


df.to_csv(
    "EM_F1_results.csv",
    index=False
)


print(df)

print("\nSaved EM_F1_results.csv")