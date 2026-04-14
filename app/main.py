class Distance:
    # Write your code here
    def __init__(self, km: int) -> None:
        self.km = km
    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, otherKm):
        if isinstance(otherKm, Distance):
            return Distance(self.km + otherKm.km)
        if isinstance(otherKm, (int, float)):
            return Distance(self.km + otherKm)
        return NotImplemented

    def __iadd__(self, otherKm):
        if isinstance(otherKm, Distance):
            self.km += otherKm.km
            return self
        if isinstance(otherKm, (int, float)):
            self.km += otherKm
            return self
        return NotImplemented

    def __mul__(self, otherKm):
        if isinstance(otherKm, (int, float)):
            return Distance(self.km * otherKm)
        return NotImplemented

    def __rmul__(self, otherKm):
        return self.__mul__(otherKm)

    def __truediv__(self, otherKm):
        if isinstance(otherKm, (int, float)):
            result = round(self.km / otherKm, 2)
            return Distance(result)
        return NotImplemented

    def __lt__(self, otherKm):
        if isinstance(otherKm, Distance):
            return self.km < otherKm.km

        if isinstance(otherKm, (int, float)):
            return self.km < otherKm
        return NotImplemented

    def __gt__(self, otherKm):
        if isinstance(otherKm, Distance):
            return self.km > otherKm.km

        if isinstance(otherKm, (int, float)):
            return self.km > otherKm
        return NotImplemented

    def __eq__(self, otherKm):
        if isinstance(otherKm, Distance):
            return self.km == otherKm.km

        if isinstance(otherKm, (int, float)):
            return self.km == otherKm
        return NotImplemented

    def __le__(self, otherKm):
        if isinstance(otherKm, Distance):
            return self.km <= otherKm.km
        if isinstance(otherKm, (int, float)):
            return self.km <= otherKm
        return NotImplemented

    def __ge__(self, otherKm):
        if isinstance(otherKm, Distance):
            return self.km >= otherKm.km
        if isinstance(otherKm, (int, float)):
            return self.km >= otherKm
        return NotImplemented
