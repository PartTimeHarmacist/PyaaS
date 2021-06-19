import docker


# noinspection SpellCheckingInspection
class PyfaaS:
    def __init__(self):
        self.docker_client = docker.from_env()

    @staticmethod
    def hello(subj='world'):
        print(f"Hello, {subj}!")

    def list_containers(self):
        print(self.docker_client.containers())


if __name__ == "__main__":
    PyfaaS.hello()
    fn = PyfaaS()
    fn.list_containers()
