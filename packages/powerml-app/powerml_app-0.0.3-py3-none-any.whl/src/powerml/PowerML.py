import requests
import json
from powerml.utils.run_ai import run_ai


class PowerML:
    def __init__(self, config):
        self.config = config
        self.key = self.config["key"]
        print(self.key)

    def predict(self,
                prompt: str = "Say this is a test",
                stop: str = "",
                model: str = "llama",
                max_tokens: int = 128,
                temperature: int = 0,
                ) -> str:
        params = {
            "prompt": prompt,
            "model": model,
            "max_tokens": max_tokens,
            "stop": stop,
            "temperature": temperature,
        }
        # if the model is one of our models, then hit our api
        return run_ai(prompt,
                      max_tokens=max_tokens,
                      api="powerml",
                      model=model,
                      stop=stop,
                      temperature=temperature,
                      key=self.key,
                      )

    def fit(self,
            data: list[str],
            model: str = "llama"):
        # Upload filtered data to train api
        headers = {
            "Authorization": "Bearer " + self.key,
            "Content-Type": "application/json", }
        response = requests.post(
            headers=headers,
            url="https://api.staging.powerml.co/v1/train",
            json={
                "dataset": self.__make_dataset_string(data),
                "model": model
            })
        return response.json()

    def __make_dataset_string(self, training_data):
        dataset = "\n".join(
            [json.dumps({"prompt": item.replace("\n", "\\n")}) for item in training_data])
        return dataset
