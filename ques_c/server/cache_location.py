from dataclasses import dataclass


@dataclass
class CacheLocation:
    city: str
    connection_url: str
    coord: tuple

    def to_dict(self):
        return {"city": self.city, "connection_url": self.connection_url}

    def __str__(self):
        return str(self.to_dict())

