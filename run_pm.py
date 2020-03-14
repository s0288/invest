#!/usr/bin/python3.6
# coding: utf8

# read user data
import pandas as pd

# prepare and run papermill code
import datetime
import papermill as pm
import os

stocks = ['KORI.PA'] #, 'BKD', 'DVA', 'GEN', 'CSU', 'ADUS', 'ALK', '0293.HK', 'UAL', 'WIZZ.L', 'AF.PA', 'LHA.DE', 'ACR.SG', 'CZR', 'CNTY', '0308.HK', 'MAR', 'WYND', 'TUI1.DE', 'CCL', 'RCL', 'NCLH', 'DB', 'CBK.DE', 'GS', 'SEB-A.ST', 'NDA-SE.ST', 'AMZN', 'FB', 'GOOG', 'AAPL']
# remove fullstops
stocks = [stock.replace(".", "").lower() for stock in stocks]

# create jupyter notebook for stock

for stock in stocks:
    try:
        print(f"creating jupyter notebook for {stock}")
        output_ipynb = str(stock) + '.ipynb'
        os.system(f"jupyter trust {output_ipynb}")
        pm.execute_notebook('corona_invest.ipynb', output_ipynb, parameters = dict(ticker=stock))

    except Exception as e:
        print(f"error creating notebook for {stock}: {e}")
    # # download html file without input code from jupyter notebook
    # try:
    #     print('converting jupyter notebook to html...')
    #     ## add /home/s0288/.virtualenvs/my-virtualenv/bin/ to specify directory of virtual env for subprocess - reverts to default python 2.7 otherwise!
    #     nbconverttohtml_nocode ="/home/s0288/.virtualenvs/my-virtualenv/bin/jupyter nbconvert --ExecutePreprocessor.kernel_name=python3.6 --template=nbextensions --to=html ./stocks/" + str(stock) + ".ipynb --no-input"
    #     os.system(nbconverttohtml_nocode)
    # except Exception as e:
    #     print(f'error creating html file for {stock}')

