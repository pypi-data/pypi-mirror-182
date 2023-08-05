import os
import sys


def testPowerMLFitAndPredict():
    from powerml import PowerML
    config = {"powerml": {"key": "cb01626747049cb05e1132c4f88b412c5ee8d169"}}
    powerml = PowerML(config)

    data = ["item2", "item3"]
    model_details = powerml.fit(data, "llama")
    assert model_details is not None

    response = powerml.predict("test")
    assert response != ""


def testPowerMLPredict():
    from powerml import PowerML
    config = {"powerml": {"key": "cb01626747049cb05e1132c4f88b412c5ee8d169"}}
    powerml = PowerML(config)
    testPrompt = "hello there"
    response = powerml.predict(prompt=testPrompt)
    assert response != ""


def testPowerMLPredictNoConfig():
    from powerml import PowerML
    powerml = PowerML()
    testPrompt = "hello there"
    response = powerml.predict(prompt=testPrompt)
    assert response != ""


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(
        os.path.realpath(__file__))), "src")
    sys.path.append(path)
    # from powerml.utils.run_ai import run_ai
    # response = run_ai()
    # print(response)

    # from powerml.fuzzy.more_like_this import more_like_this
    # text = more_like_this(
    #     'AI: Hi, what can we make fresh for you today?\nCX: Chicken Cheddar Quesadilla.', n=1)

    # testPowerMLPredictNoConfig()
    # testPowerMLPredict()
    testPowerMLFitAndPredict()
