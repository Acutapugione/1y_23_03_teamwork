from .. import app

@app.template_filter()
def price_format(price): 
    rounded_price = round(price, 3)
    formated_price = f"₮{rounded_price:.3}"
    return formated_price
