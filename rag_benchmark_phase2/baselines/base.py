from abc import ABC, abstractmethod


class BaseAdapter(ABC):

    name = "base"

    def __init__(self, config=None):
        self.config = config or {}

    @abstractmethod
    def generate(self, sample):
        """
        输入:
            sample:
                question
                documents

        输出:
            dict:
            {
                answer,
                evidence,
                input_tokens,
                output_tokens,
                latency
            }
        """
        pass