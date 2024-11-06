import fastapi

class User():
    id: int
    name: str
    nickname: str
    age: int


basedata = {"users":[
    User(id=1, name='Vsevolod', nickname='seva1337', age=19),
    User(id=2, name='Alexey', nickname='leha12', age=54)
],}