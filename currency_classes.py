
class Result:
    def __init__(self, result, conversion_flow):
        self.result = result
        self.conversion_flow = conversion_flow


class USD:

    resultArchive = []

    def __init__(self, user_input, exchange_rate=3.28):
        self.user_input = user_input
        self.exchange_rate = exchange_rate
        self.conversion_value = exchange_rate * user_input
        self.result = Result(round(self.conversion_value, 2), "USD to ILS")
        self.resultArchive.append(f"{self.result.result}, {self.result.conversion_flow}")


class ILS:
    resultArchive = []

    def __init__(self, user_input, exchange_rate=0.28):
        self.user_input = user_input
        self.exchange_rate = exchange_rate
        self.conversion_value = user_input * exchange_rate
        self.result = Result(round(self.conversion_value, 2), "ILS to USD")
        self.resultArchive.append(f"{self.result.result}, {self.result.conversion_flow}")
