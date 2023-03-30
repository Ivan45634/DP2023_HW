import random

class SomeModel:
    def predict(self, message: str) -> float:
        random.seed(message)
        prediction = random.random()
        print(prediction)
        return prediction

def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    prediction = model.predict(message)

    if prediction < bad_thresholds:
        res = "неуд"
    elif prediction > good_thresholds:
        res = "отл"
    else:
        res = "норм"
    return res
