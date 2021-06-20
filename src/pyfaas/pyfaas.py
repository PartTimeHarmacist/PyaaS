import docker
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler
from sys import stdout, stderr

PYFAAS_VERSION = "0.0.1"
PYFAAS_NAME = "PyfaaS"

logger = logging.getLogger(__name__)
pyfaas_log_file_path = Path('.') / 'log' / 'pyfaas.log'
pyfaas_log_file_path.parent.mkdir(parents=True, exist_ok=True)
pyfaas_log_handlers = []

# Stream Logger
pyfaas_stream_logger = logging.StreamHandler(stream=stdout)
pyfaas_log_handlers.append(pyfaas_stream_logger)

# File Logger
pyfaas_file_logger = RotatingFileHandler(
    filename=pyfaas_log_file_path,
    mode='a',
    maxBytes=(2**20) * 5,  # 2**20 = 1 Megabyte in base 2.  (2**20) * 3 would be 3 megabytes, etc.
    backupCount=5,
    encoding='utf-8',
    delay=False
)
pyfaas_log_handlers.append(pyfaas_file_logger)


# Handler Standardization
pyfaas_logging_formatter = logging.Formatter(
    fmt='[%(asctime)s - %(name)s] [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

for handler in pyfaas_log_handlers:
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(pyfaas_logging_formatter)
    logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


# noinspection SpellCheckingInspection
class PyfaaS:
    def __init__(self):
        self.docker_client = docker.from_env()
        self.container_default_labels = {"PyfaaS_version": self.get_version(),
                                         "PyfaaS_schedule": "@none",
                                         "PyfaaS_source": "local"}
        logger.debug("PyfaaS module initialized.")

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
    logger.debug("Main thread called.")
    fn = PyfaaS()
    fn.hello(subj='Docker')
    logger.info(f"PyfaaS version {fn} initialized successfully.")
    fn.docker_client.containers.run("alpine", "echo hello, world!",
                                    labels=fn.container_default_labels,
                                    detach=True)
    logger.info(f"Found the following PyfaaS tagged containers: "
                f"{','.join([c.attrs['Name'] for c in fn.list_containers(list_all=True)])}")
    fn.clean_up_containers(running=True)
