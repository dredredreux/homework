import fastapi
import pydantic

class User(pydantic.BaseModel):
    id: int
    name: str
    nickname: str
    age: int

app = fastapi.FastAPI()


basedata = {"users":[
    User(id=1, name='Vsevolod', nickname='seva1337', age=19),
    User(id=2, name='Alexey', nickname='leha12', age=54)
],}


@app.get('/users')
def read_basedata():
    return basedata

@app.post('/user/create')
def create_user(user: User):
    basedata['users'].append(user)
    return {'user created': user}

@app.put('/user/{user_id}')
def update_user(user_id: int, user: User = fastapi.Body()):
    for index, u in enumerate(basedata['users']):
        if u.id == user_id:
            basedata['users'][index] = user
            return user
        
@app.delete('/user/{user_id}')
def delete_user_id(user_id: int = fastapi.Path()):
    for index, u in enumerate(basedata['users']):
        if u.id == user_id:
            del basedata['users'][index]
            return basedata