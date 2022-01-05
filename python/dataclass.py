from dataclasses import dataclass,field

@dataclass
class Vector:
    x: int
    y: int

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)


print(Vector(1,2)+Vector(2,1))
print(Vector(2,2)-Vector(2,1))


@dataclass
class DataClassWithDefaults:
    immutable: str = field(default="This is the defaault value")
    mutable: list = field(default_factory=list)

print(DataClassWithDefaults())
print(DataClassWithDefaults("Hello"))
print(DataClassWithDefaults("Hello",['1','2']))
