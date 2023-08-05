from typing import Any
from abc import ABC, abstractmethod

from pika import BlockingConnection

from .types import Subjects

class AbstractPublisher(ABC):
    @property
    @abstractmethod
    def subject(self) -> Subjects | str:
        raise NotImplementedError()

    @abstractmethod
    def publish(self, data: Any):
        pass

    def __init__(self, connection: BlockingConnection):
        self.channel = connection.channel()  # Start a channel.
        self.channel.queue_declare(queue=self.subject)  # Declare a queue.
