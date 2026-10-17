import json

from .schema import Sample



def load_answers(answer_file):

    answers = {}


    if answer_file is None:
        return answers



    with open(
        answer_file,
        encoding="utf8"
    ) as f:


        for line in f:


            if not line.strip():
                continue


            x = json.loads(line)


            answer = x.get(
                "golden_answers",
                []
            )


            if isinstance(answer, list):

                if len(answer) > 0:

                    answers[x["id"]] = answer[0]


            else:

                answers[x["id"]] = answer



    return answers





def load_jsonl(
        path,
        dataset,
        answer_file=None
):


    answer_map = load_answers(
        answer_file
    )


    data = []



    with open(
        path,
        encoding="utf8"
    ) as f:


        for line in f:


            if not line.strip():
                continue


            x = json.loads(line)



            docs = []



            for i, c in enumerate(
                x.get("context", [])
            ):


                docs.append({

                    "doc_id":
                        c.get(
                            "docments",
                            str(i)
                        ),

                    "chunk_id":
                        i,

                    "text":
                        c.get(
                            "text",
                            ""
                        )

                })



            sample_id = x.get(
                "id"
            )



            data.append(

                Sample(

                    dataset=dataset,

                    sample_id=sample_id,

                    question=x.get(
                        "question",
                        ""
                    ),

                    documents=docs,

                    reference_answer=
                        answer_map.get(
                            sample_id,
                            ""
                        ),

                    supporting_facts=[]

                )

            )



    return data