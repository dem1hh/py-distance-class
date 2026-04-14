from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_km: Distance | int | float) -> Distance:
        if isinstance(other_km, Distance):
            return Distance(self.km + other_km.km)
        if isinstance(other_km, (int, float)):
            return Distance(self.km + other_km)
        return NotImplemented

    def __iadd__(self, other_km: Distance | int | float) -> Distance:
        if isinstance(other_km, Distance):
            self.km += other_km.km
            return self
        if isinstance(other_km, (int, float)):
            self.km += other_km
            return self
        return NotImplemented

    def __mul__(self, other_km: int | float) -> Distance:
        if isinstance(other_km, (int, float)):
            return Distance(self.km * other_km)
        return NotImplemented

    def __rmul__(self, other_km: int | float) -> Distance:
        return self.__mul__(other_km)

    def __truediv__(self, other_km: int | float) -> Distance:
        if isinstance(other_km, (int, float)):
            result = round(self.km / other_km, 2)
            return Distance(result)
        return NotImplemented

    def __lt__(self, other_km: Distance | int | float) -> bool:
        if isinstance(other_km, Distance):
            return self.km < other_km.km

        if isinstance(other_km, (int, float)):
            return self.km < other_km
        return NotImplemented

    def __gt__(self, other_km: Distance | int | float) -> bool:
        if isinstance(other_km, Distance):
            return self.km > other_km.km

        if isinstance(other_km, (int, float)):
            return self.km > other_km
        return NotImplemented

    def __eq__(self, other_km: Distance | int | float) -> bool:
        if isinstance(other_km, Distance):
            return self.km == other_km.km

        if isinstance(other_km, (int, float)):
            return self.km == other_km
        return NotImplemented

    def __le__(self, other_km: Distance | int | float) -> bool:
        if isinstance(other_km, Distance):
            return self.km <= other_km.km
        if isinstance(other_km, (int, float)):
            return self.km <= other_km
        return NotImplemented

    def __ge__(self, other_km: Distance | int | float) -> bool:
        if isinstance(other_km, Distance):
            return self.km >= other_km.km
        if isinstance(other_km, (int, float)):
            return self.km >= other_km
        return NotImplemented
