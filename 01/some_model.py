"""
predict_message_mood
"""
class SomeModel:
    """
    реализация не важна
    """
    def predict(self, message: str) -> float:
        return 0.5


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    """
    :param message:
    :param model:
    :param bad_thresholds:
    :param good_thresholds:
    :return: str
    """
    if not isinstance(message, str):
        raise TypeError
    prediction = model.predict(message)

    if prediction < bad_thresholds:
        res = "неуд"
    elif prediction > good_thresholds:
        res = "отл"
    else:
        res = "норм"
    return res

