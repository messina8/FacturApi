from fastapi import FastAPI

from Invoicer import Invoicer
from Sale import Sale

app = FastAPI()
invoicer = Invoicer()


@app.get("/")
async def home():
    return {'Welcome message': 'El Rio Software: Invoicer'}


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


