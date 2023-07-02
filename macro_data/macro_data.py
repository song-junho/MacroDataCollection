import yfinance as yf
from tqdm import tqdm
import pandas as pd
import pickle
from fredapi import Fred
from PublicDataReader import Ecos
from .config import API_KEY, DATA_INFO
import calendar
from datetime import datetime


class MacroData:

    def __init__(self):

        self.fred = Fred(api_key=API_KEY["FRED"])
        self.ecos = Ecos(API_KEY["ECOS"])
        self.dict_macro_data = {

            "FICC_INFO" : {
                "fixed_income" : {}
                , "currency" : {}
                , "comoddity" : {}
            }

            ,"ECONOMIC_INFO" : {
                "global": {}
                , "usa" : {}
                , "korea" : {}
                , "china" : {}
                , "eu" : {}
            }
        }

    def get_data(self, ticker, ticker_info):

        df = pd.DataFrame()

        if ticker_info["release"] == "fred":
            df = self.fred.get_series(ticker)

            # 전처리
            df = pd.DataFrame(df)
            df.index.name = 'date'
            df = df.rename(columns={0: 'val'})

            # 일자 eom 형식으로 전처리
            if ticker_info["freq"] != "d":
                df = df.reset_index()
                df["date"] = df["date"].apply(lambda x: x.strftime('%Y%m%d'))
                df["date"] = df["date"].apply(
                    lambda x: x[:4] + "-" + x[4:6] + "-" + str(calendar.monthrange(int(x[:4]), int(x[4:6]))[1]))
                df["date"] = pd.to_datetime(df["date"])

                df = df.set_index('date')

        elif ticker_info["release"] == "yahoo":
            df = yf.Ticker(ticker).history(period="max")

            # 전처리
            df = df.reset_index(drop=False)
            df["Date"] = pd.to_datetime(df["Date"].dt.strftime("%Y-%m-%d"))
            df = df[["Date", "Close"]].rename(columns={"Date": "date", "Close": "val"})
            df = df.set_index("date")

        elif ticker_info["release"] == "eos":

            today = datetime.today()

            if ticker_info["freq"] == "d":

                start_date = '20000101'

                end_date = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2)

            elif ticker_info["freq"] == "m":

                start_date = '200001'

                end_date = str(today.year) + str(today.month).zfill(2)

            elif ticker_info["freq"] == "q":

                start_date = '2000Q1'

                end_date = str(today.year + 1) + "Q4"

            df = self.ecos.get_statistic_search(통계표코드=ticker_info["stat_cd"], 통계항목코드1=ticker, 주기=ticker_info["freq"].upper(),
                                          검색시작일자=start_date, 검색종료일자=end_date)

            df = df[["시점", "값"]].rename(columns={"시점": "date", "값": "val"})

            df["val"] = df["val"].astype("float")

            # 일자 데이터 형변환
            if (ticker_info["freq"] == "d") or (ticker_info["freq"] == "m"):

                df["date"] = df["date"].apply(
                    lambda x: x[:4] + "-" + x[4:6] + "-" + str(calendar.monthrange(int(x[:4]), int(x[4:6]))[1]))

                df["date"] = pd.to_datetime(df["date"])

            elif ticker_info["freq"] == "q":

                pass

        return df

    def collect(self, macro_type):

        data_info = DATA_INFO[macro_type]

        for sub_class in data_info.keys():

            for ticker in tqdm(data_info[sub_class].keys()):
                ticker_info = data_info[sub_class][ticker]
                df = self.get_data(ticker, ticker_info)
                self.dict_macro_data[macro_type][sub_class][ticker] = df

    def save(self):

        with open(r"D:\MyProject\MyData\MacroData\MacroData.pickle", 'wb') as fw:
            pickle.dump(self.dict_macro_data, fw)

    def run(self):

        self.collect("FICC_INFO")
        self.collect("ECONOMIC_INFO")
        self.save()
