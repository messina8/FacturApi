from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

import frontend
from Invoicer import Invoicer
from Sale import Sale
from User import User, fake_decode_token, fake_users_db

app = FastAPI()
invoicer = Invoicer()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.get("/auth/")
async def auth(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'token': token}


@app.post("/new_sale/")
async def new_sale(sale: Sale):
    await invoicer.new_sale(sale)
    return {'sale added'}


@app.get("/get_sales/")
async def get_sales():
    sales_list = await invoicer.get_sales()
    sales = {}
    for n, i in enumerate(sales_list, 1):
        sales[n] = i
    return sales


@app.get("/create_invoice/{index}")
async def create_invoice(index: int):
    sales_list = await invoicer.get_sales()
    sale = sales_list[index]
    sale.create_invoice()
    return sale


frontend.init(app, invoicer)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.0', port=8000)
