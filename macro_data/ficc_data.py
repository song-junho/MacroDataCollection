import yfinance as yf
from tqdm import tqdm
import pandas as pd
import pickle
from fredapi import Fred
from PublicDataReader import Ecos
from .config import API_KEY, DATA_INFO


class FiccData:

    def __init__(self):

        self.fred = Fred(api_key=API_KEY["FRED"])
        self.ecos = Ecos(API_KEY["ECOS"])
        self.ficc_info = DATA_INFO["FICC_INFO"]
        self.dict_ficc_data = {}

    def get_ficc_data(self, ticker, ticker_info):

        df = pd.DataFrame()

        if ticker_info["release"] == "fred":
            df = self.fred.get_series(ticker)

            # 전처리
            df = pd.DataFrame(df)
            df.index.name = 'date'
            df = df.rename(columns={0: 'val'})

        elif ticker_info["release"] == "yahoo":
            df = yf.Ticker(ticker).history(period="max")

            # 전처리
            df = df.reset_index(drop=False)
            df["Date"] = pd.to_datetime(df["Date"].dt.strftime("%Y-%m-%d"))
            df = df[["Date", "Close"]].rename(columns={"Date": "date", "Close": "val"})
            df = df.set_index("date")

        elif ticker_info["release"] == "eos":

            df = self.ecos.get_statistic_search(통계표코드=ticker_info["stat_cd"], 통계항목코드1=ticker, 주기=ticker_info["freq"].upper(),
                                          검색시작일자="20000101", 검색종료일자="20230701")
            df = df[["시점", "값"]].rename(columns={"시점": "date", "값": "val"})
            df = df.set_index("date")

        return df

    def collect(self):

        for ficc in self.ficc_info.keys():

            for ticker in tqdm(self.ficc_info[ficc].keys()):
                ticker_info = self.ficc_info[ficc][ticker]
                df = self.get_ficc_data(ticker, ticker_info)
                self.dict_ficc_data[ticker] = df

    def save(self):

        with open(r"D:\MyProject\MyData\MacroData\FiccData.pickle", 'wb') as fw:
            pickle.dump(self.dict_ficc_data, fw)

    def run(self):

        self.collect()
        self.save()
