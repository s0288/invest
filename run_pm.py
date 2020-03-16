#!/usr/bin/python3.6
# coding: utf8

# read user data
import pandas as pd

# prepare and run papermill code
import datetime
import papermill as pm
import os

stocks = ['^GDAXI', '^GSPC', 'KORI.PA', 'BKD', 'DVA', 'GEN', 'CSU', 'ADUS', 'ALK', '0293.HK', 'WIZZ.L', 'AF.PA', 'LHA.DE', 'CZR', '0308.HK', 'MAR', 'WYND', 'RCL', 'NCLH', 'DB', 'GS', 'SEB-A.ST', 'NDA-SE.ST', 'AMZN', 'FB', 'GOOG', 'AAPL', 'NFLX', 'MUV2.MI', 'CS.PA', 'ALV.DE', 'ING', 'ETSY']
# remove fullstops
names = [stock.replace(".", "").lower() for stock in stocks]

# remove stock_returns.pkl, if it exists already
if os.path.isfile('stock_returns.pkl'):
    os.remove("stock_returns.pkl")
    print("File Removed!")



# create jupyter notebook for stock
for i, row in enumerate(stocks):
    name = names[i]
    stock = stocks[i]

    try:
        print(f"creating jupyter notebook for {stock}")
        output_ipynb = "./stocks/" + str(name) + '.ipynb'
        os.system(f"jupyter trust {output_ipynb}")
        pm.execute_notebook('corona_invest.ipynb', output_ipynb, parameters = dict(ticker=stock))

    except Exception as e:
        print(f"error creating notebook for {stock}: {e}")
    # download html file without input code from jupyter notebook
    try:
        print('converting jupyter notebook to html...')
        ## add /home/s0288/.virtualenvs/my-virtualenv/bin/ to specify directory of virtual env for subprocess - reverts to default python 2.7 otherwise!
        nbconverttohtml_nocode ="/Users/Alex/anaconda3/envs/notadiet/bin/jupyter nbconvert --to html ./stocks/" + str(name) + ".ipynb --no-input"
        os.system(nbconverttohtml_nocode)
    except Exception as e:
        print(f'error creating html file for {stock}')

