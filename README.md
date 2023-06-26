# MacroDataCollection
> Macro 데이터 수집
> 1. Ficc Data , 2. Economic Data

### 1. Ficc Data
 - 종류: 채권(FixedIncome) , 통화(Currency) , 원자재(Comoddity)
 - 출처: Fred API , EOS(한은) API , YahooFinance

```json
{
    "FICC_INFO" : {
        "fixed_income": {

            "T10Y2Y": {
                "name": "미국채 스프레드(10y-2y)"
                , "freq": "d"
                , "release": "fred"
            }
            , "T10Y3M": {
                "name": "미국채 스프레드(10y-3m)"
                , "freq": "d"
                , "release": "fred"
            }
            , "T10YFF": {
                "name": "미국채 스프레드(10y-FF)"
                , "freq": "d"
                , "release": "fred"
            }
            , "DGS30": {
                "name": "미국채 (30y)"
                , "freq": "d"
                , "release": "fred"
            }
            , "DGS20": {
                "name": "미국채 (20y)"
                , "freq": "d"
                , "release": "fred"
            }
            , "DGS10": {
                "name": "미국채 (10y)"
                , "freq": "d"
                , "release": "fred"
            }
            , "DGS2": {
                "name": "미국채 (2y)"
                , "freq": "d"
                , "release": "fred"
            }
            , "DGS3MO": {
                "name": "미국채 (3M)"
                , "freq": "d"
                , "release": "fred"
            }
            , "FF": {
                "name": "Fed 기준금리"
                , "freq": "w"
                , "release": "fred"
            }
            , "BAMLHE00EHYIOAS": {
                "name": "Euro High Yield Index"
                , "freq": "d"
                , "release": "fred"
            }
            , "BAMLH0A0HYM2": {
                "name": "US High Yield Index Option-Adjusted Spread"
                , "freq": "d"
                , "release": "fred"
            }
            , "BAMLH0A2HYBEY": {
                "name": "Single-B US High Yield Index"
                , "freq": "d"
                , "release": "fred"
            }
            , "BAMLH0A1HYBBEY": {
                "name": "BB US High Yield Index"
                , "freq": "d"
                , "release": "fred"
            }
            , "BAMLH0A3HYCEY": {
                "name": "CCC & Lower US High Yield Index"
                , "freq": "d"
                , "release": "fred"
            }
            , "0101000": {"stat_cd": "722Y001", "name": "한국은행 기준금리", "freq": "d", "release": "eos"}
            , "010190000": {"stat_cd": "817Y002", "name": "국고채(1년)", "freq": "d", "release": "eos"}
            , "010200000": {"stat_cd": "817Y002", "name": "국고채(3년)", "freq": "d", "release": "eos"}
            , "010200001": {"stat_cd": "817Y002", "name": "국고채(5년)", "freq": "d", "release": "eos"}
            , "010210000": {"stat_cd": "817Y002", "name": "국고채(10년)", "freq": "d", "release": "eos"}
            , "010220000": {"stat_cd": "817Y002", "name": "국고채(20년)", "freq": "d", "release": "eos"}
            , "010230000": {"stat_cd": "817Y002", "name": "국고채(30년)", "freq": "d", "release": "eos"}
            , "010240000": {"stat_cd": "817Y002", "name": "국고채(50년)", "freq": "d", "release": "eos"}
            , "010300000": {"stat_cd": "817Y002", "name": "회사채(3년, AA-)", "freq": "d", "release": "eos"}
            , "010310000": {"stat_cd": "817Y002", "name": "회사채(3년, AA-, 민평)", "freq": "d", "release": "eos"}
            , "010320000": {"stat_cd": "817Y002", "name": "회사채(3년, BBB-)", "freq": "d", "release": "eos"}

        },

        "currency": {

            "DTWEXBGS": {
                "name": " U.S. Dollar Index"
                , "freq": "d"
                , "release": "fred"
            }
            , "DEXUSEU": {
                "name": "U.S. Dollars to Euro Spot Exchange Rate"
                , "freq": "d"
                , "release": "fred"
            }
            , "DEXCHUS": {
                "name": "Chinese Yuan Renminbi to U.S. Dollar Spot Exchange Rate"
                , "freq": "d"
                , "release": "fred"
            }
            , "DEXJPUS": {
                "name": "Japanese Yen to U.S. Dollar Spot Exchange Ratee"
                , "freq": "d"
                , "release": "fred"
            }
            , "DEXKOUS": {
                "name": "South Korean Won to U.S. Dollar Spot Exchange Rate"
                , "freq": "d"
                , "release": "fred"
            }

        },

        "comoddity": {

            "PPIACO": {
                "name": "Producer Price Index by Commodity: All Commodities"
                , "freq": "m"
                , "release": "fred"
            }
            , "WPU0911": {
                "name": "Producer Price Index by Commodity: Pulp, Paper, and Allied Products: Wood Pulp"
                , "freq": "m"
                , "release": "fred"
            }
            , "WPU061": {
                "name": "Producer Price Index by Commodity: Chemicals and Allied Products: Industrial Chemicals"
                , "freq": "m"
                , "release": "fred"
            }
            , "WPU10": {
                "name": "Producer Price Index by Commodity: Metals and Metal Products"
                , "freq": "m"
                , "release": "fred"
            }
            , "WPU012": {
                "name": "Producer Price Index by Commodity: Farm Products: Grains"
                , "freq": "m"
                , "release": "fred"
            }
            , "PNRGINDEXM": {
                "name": "Global price of Energy index"
                , "freq": "m"
                , "release": "fred"
            }

            , "GC=F": {
                "name": "future gold"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "HRC=F": {
                "name": "future hot_coil"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "HG=F": {
                "name": "future copper"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "ALI=F": {
                "name": "future aluminium"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "CL=F": {
                "name": "future wti"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "NG=F": {
                "name": "natural_gas"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "ZC=F": {
                "name": "future corn"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "ZW=F": {
                "name": "future wheat"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "ZO=F": {
                "name": "future oat"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "ZS=F": {
                "name": "future soybean"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "LE=F": {
                "name": "future live_cattle"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "GF=F": {
                "name": "future feeder_cattle"
                , "freq": "d"
                , "release": "yahoo"
            }
            , "HE=F": {
                "name": "future hogs"
                , "freq": "d"
                , "release": "yahoo"
            }
        }
    }
}
```

### 2. Economic Data
 - 종류: 경기 지표 (GDP, 물가, 제조업지수, 무역수지, 실업률 등)


### OutPutSample
> key(Ticker) - Value(DataFrame) 형식

ex) Ticker: T10TFF (미국채 10년 - 기준금리 스프레드)  
  ![image](https://github.com/song-junho/MacroDataCollection/assets/67362481/4b613a6c-e975-4a4a-bbd6-c6ebb5b5161d)

