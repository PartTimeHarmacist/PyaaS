# noinspection SpellCheckingInspection
class PyfaaS:
    def __init__(self):
        pass

    @staticmethod
    def hello(subj='world'):
        print(f"Hello, {subj}!")


if __name__ == "__main__":
    PyfaaS.hello()
