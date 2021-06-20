import docker


PYFAAS_VERSION = "0.0.1"
PYFAAS_NAME = "PyfaaS"


# noinspection SpellCheckingInspection
class PyfaaS:
    def __init__(self):
        self.docker_client = docker.from_env()
        self.container_default_labels = {"PyfaaS_version": self.get_version(),
                                         "PyfaaS_schedule": "@none",
                                         "PyfaaS_source": "local"}

    def hello(self, subj='world'):
        self.docker_client.containers.run("alpine", f"echo hello, {subj}!  This is {self}",
                                          labels=fn.container_default_labels,
                                          name="pyfaas_hello",
                                          remove=True,
                                          detach=True)

    @staticmethod
    def get_version():
        return PYFAAS_VERSION

    @staticmethod
    def get_name():
        return PYFAAS_NAME

    def __str__(self):
        return f"{self.get_name()} - v{self.get_version()} [{len(self.list_containers())} Containers]"

    def list_containers(self, list_all=False):
        return self.docker_client.containers.list(filters={'label': list(self.container_default_labels.keys())},
                                                  all=list_all)

    def clean_up_containers(self, running=False):
        for container in self.list_containers(list_all=True):
            container.remove()


if __name__ == "__main__":
    fn = PyfaaS()
    fn.hello(subj='Docker')
    print(fn)
    fn.docker_client.containers.run("alpine", "echo hello, world!",
                                    labels=fn.container_default_labels,
                                    detach=True)
    print(','.join([c.attrs['Name'] for c in fn.list_containers(list_all=True)]))
    fn.clean_up_containers(running=True)
