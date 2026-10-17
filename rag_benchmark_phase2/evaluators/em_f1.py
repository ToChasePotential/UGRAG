import re
import string


def normalize_answer(s):

    if s is None:
        return ""

    s = s.lower()

    s = "".join(
        ch for ch in s
        if ch not in string.punctuation
    )

    s = re.sub(
        r"\b(a|an|the)\b",
        " ",
        s
    )

    s = " ".join(s.split())

    return s



def exact_match(pred, gold):

    return int(
        normalize_answer(pred)
        ==
        normalize_answer(gold)
    )



def f1(pred, gold):

    pred_tokens = normalize_answer(pred).split()
    gold_tokens = normalize_answer(gold).split()

    if len(pred_tokens)==0 and len(gold_tokens)==0:
        return 1

    if len(pred_tokens)==0 or len(gold_tokens)==0:
        return 0


    common = set(pred_tokens) & set(gold_tokens)


    if len(common)==0:
        return 0


    precision = len(common)/len(pred_tokens)

    recall = len(common)/len(gold_tokens)


    return 2*precision*recall/(precision+recall)