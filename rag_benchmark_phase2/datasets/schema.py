
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Sample:
    dataset:str
    sample_id:str
    question:str
    documents:List[Dict[str,Any]]
    reference_answer:str=""
    supporting_facts:list=field(default_factory=list)
