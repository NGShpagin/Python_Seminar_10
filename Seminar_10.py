from tkinter import *
import requests

root = Tk()
root.title("Калькулятор валют")
root.geometry('400x100')

values = ['RUB', 'USD', 'EUR', 'JYP', 'CNY']
value_1 = StringVar()
value_1.set(f"Выберите валюту")
value_1_drop = OptionMenu(root, value_1, *values)
value_1_drop.grid(row=1, column=0)
value_1_entry = Entry(root, width=15, relief='raised')
value_1_entry.grid(row=2, column=0)

into_lbl = Label(root, text='>>>', borderwidth=2)
into_lbl.grid(row=1, column=1)
into2_lbl = Label(root, text='>>>', borderwidth=2)
into2_lbl.grid(row=2, column=1)

value_2 = StringVar()
value_2.set(f"Выберите валюту")
value_2_drop = OptionMenu(root, value_2, *values)
value_2_drop.grid(row=1, column=2, ipadx=10, ipady=5)

result_lbl = Label(root, bg='white', fg='black', width=15, relief='raised')
result_lbl.grid(row=2, column=2)


def convert(value1, value2):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={value1}&to_currency={value2}&apikey=DPACWXWIWZ4COOOF'
    r = requests.get(url)
    data = r.json()
    value = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    our_value = float(value_1_entry.get())
    result = value * our_value
    result_lbl.configure(text=f'{result}')


convert_btn = Button(root, text='Конвертировать', width=15, command=lambda: convert(value_1.get(), value_2.get()))
convert_btn.grid(row=3, column=0, columnspan=3)

root.mainloop()
