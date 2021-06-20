import docker


PYFAAS_VERSION = "0.0.1"


# noinspection SpellCheckingInspection
class PyfaaS:
    def __init__(self):
        self.docker_client = docker.from_env()
        self.container_default_labels = {"PyfaaS_version": self.get_version(),
                                         "PyfaaS_schedule": "@none",
                                         "PyfaaS_source": "local"}

    @staticmethod
    def hello(subj='world'):
        print(f"Hello, {subj}!")

    @staticmethod
    def get_version():
        return PYFAAS_VERSION

    def list_containers(self):
        return self.docker_client.containers.list(filters={'label': self.container_default_labels.keys()})


if __name__ == "__main__":
    PyfaaS.hello()
    fn = PyfaaS()
    fn.list_containers()
