import os

root = "outputs"

for model in os.listdir(root):
    model_path = os.path.join(root, model)

    if not os.path.isdir(model_path):
        continue

    print("\n", "="*30)
    print(model)

    for dataset in os.listdir(model_path):
        file = os.path.join(
            model_path,
            dataset,
            "predictions.jsonl"
        )

        if os.path.exists(file):
            size = os.path.getsize(file)

            if size > 0:
                print(dataset, "DONE", size, "bytes")
            else:
                print(dataset, "EMPTY")
        else:
            print(dataset, "MISSING")