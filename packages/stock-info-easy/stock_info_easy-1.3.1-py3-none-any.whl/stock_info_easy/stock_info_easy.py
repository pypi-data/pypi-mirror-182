"""
Python package that allows users to get stock information easily simply by inserting the names of their interested companies. 
This module uses the yfinance wraper, an already existing Yahoo Finance API wraper to fetch the stock data.
In the previous API wraper, it is difficult to fetch finance data by company names as their stock data are available via companys' abbreviated symbols. 
This package aims to proivde prime stock information in a user-friendly way: by simply adding company names. 
Interactive visuals and audio files will be generated to help non-finance people understand the key numerical stock values.
"""
import yfinance as yf  
import yahoo_fin.stock_info as si 
from yahoo_fin.stock_info import get_data
import yahooquery as yq
yf.pdr_override()
import argparse
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import sys
import os
import numpy as np
import pandas as pd
import datetime
import re
from pandas_datareader import data as pdr
from dateutil.relativedelta import relativedelta
from keras.models import Sequential
from keras.layers import LSTM, Dense
from gtts import gTTS
from playsound import playsound
import warnings
warnings.filterwarnings("ignore")


# def bool_flag(s): 
#     """
#     Parse boolean arguments from the command line.

#     Parameters
#     ----------
#     s : bool
#         Type true/false, on/off,  0/1

#     Return 
#     -------
#     True or False 
    
#     Examples
#     --------
#     >>> bool_flag('true')
#     True
#     """
#     FALSY_STRINGS = {"off", "false", "0"}
#     TRUTHY_STRINGS = {"on", "true", "1"}
#     if s.lower() in FALSY_STRINGS:
#         return False
#     elif s.lower() in TRUTHY_STRINGS:
#         return True
#     else:
#         raise argparse.ArgumentTypeError("invalid value for a boolean flag")


# def get_args():
#     """
#     ArgumentParser provides a convenient interface to handle command-line arguments. 
#     When a user defines what arguments it requires, and argparse will figure out how to parse those.
#     https://docs.python.org/3/library/argparse.html

#     Return
#     -------
#     args: argparse object with parameters    
    
#     """
#     parser = argparse.ArgumentParser(description='StockInfoEasy')
#     parser.add_argument('--comp_names', type=str, nargs='+', default=('amazon', 'apple', 'google', 'microsoft'),
#         help="""list of company names""")
#     parser.add_argument('--start_date', type=str, default="01/04/2022", 
#                         help='Start date for the model training. Default is the first working date of 2022 for the stock market(01/04/2022).')
#     parser.add_argument('--end_date', type=str, 
#                         default=datetime.datetime.strftime(datetime.datetime.today(), format='%Y-%m-%d'), 
#                         help="End date for the model training. Today's date is used as a default. ")
#     parser.add_argument('--window_size', type=int, default=30,
#                         help='window_size to prepare features for stock prediction. ')
#     parser.add_argument('--prediction_window_size', type=int, default=20,
#                     help='window_size for stock price predicition in the future.')                    
#     parser.add_argument('--predict_future_price', default=True, type=bool_flag,
#         help="Adding this argument will predict the future price(s) of the interested company(ies).") 
#     parser.add_argument('--audio_filename', type=str, default='test_stock1.mp3',
#                         help='Define an audio filename with an extension .mp3')
        
#     args, unknown = parser.parse_known_args()
#     return args


def get_symbol(query):
    """
    THe stock data will be fetched from the existing Yahoo Finance API Wraper. As this wraper fetches finance data with companys' symbols, 
    This function converts the company name that user's inserted into its abbreviated symbol.
    The converted symbol will then be used to fetch finance info from the API wraper. 
    
    Insert a company name(s) in this function to get company name abbreviation(s), 
    This function queries information based on the National Market System (NMS) exchange. 
    Other Exchange choices are NEO, OPR, NGM, and MEX. 

    Parameters
    ----------
    query : str
        Insert a company name(s) to search.

    Returns
    -------
    symbol: str 
        Returns a symbol for the input company. 

    Examples
    --------
    >>> get_symbol('amazon')
    'AMZN'
    """
    try:
        data = yq.search(query)
    except ValueError: 
        print(query)
    else:
        quotes = data['quotes'] 
        if len(quotes) == 0:
            return 'No Symbol Found'
        symbol = quotes[0]['symbol'] # quotes[0] reprepsents NMS. Can get data from Other Exchange choices(NEO, OPR, NGM, and MEX) by 
                                     # changing quotes[0] to quotes[1], quotes[2], quotes[3], and quotes[4]. 

        return symbol



def get_hist_data(comp_names, start_date="01/04/2022", end_date=datetime.datetime.strftime( datetime.datetime.today(), format='%Y-%m-%d'), interval="1d"): 
    """
    Get historical stock data for the customized time frame.
    Data to be fetched are Open, High, Low, Close, Adj Close, Volume, Company Name, and Company Full Name. 
    - High, Low: refer to the maximum and minimum prices in a given time period.
    - Open: refers to the price at which a stock started trading when the opening bell rang.
    - Close: refers to the price of an individual stock when the stock exchange closed shop for the day.
    - Adj Close: amended closing price to reflect that stock's value after accounting for any corporate actions. 
    - Volume: the amount of shares or contracts traded in an asset/ security over a period of time (a trading day).

    Parameters
    ----------
    comp_names: tuple
        company names 
    start_date: str
        start date of data
    end_date: str
        end date of data
    interval: str
        At what interval of time does a user want to see the data. 1 day means data for consecutive dates in the time range will be fetched.

    Returns
    -------
    data_list: pandas.core.frame.DataFrame
    company_list: list
    comp_names_abbr: list
    comp_names: str

    Examples
    --------
    >>> inputs: --comp_names amazon apple google microsoft --start_date 2022-01-04 --end_date 2022-12-08
    >>> outputs: 
   # data_list:
                Open        High         Low       Close   Adj Close    Volume company_name company_fullname
    2022-01-04  170.438004  171.399994  166.349503  167.522003  167.522003  70726000         AMZN           AMAZON
    2022-01-05  166.882996  167.126495  164.356995  164.356995  164.356995  64302000         AMZN           AMAZON
    2022-01-06  163.450500  164.800003  161.936996  163.253998  163.253998  51958000         AMZN           AMAZON
    2022-01-07  163.839005  165.243500  162.031006  162.554001  162.554001  46606000         AMZN           AMAZON
    2022-01-10  160.585495  161.661499  156.304504  161.485992  161.485992  87798000         AMZN           AMAZON
    ...                ...         ...         ...         ...         ...       ...          ...              ...
    2022-12-02  249.820007  256.059998  249.690002  255.020004  255.020004  21522800         MSFT        MICROSOFT
    2022-12-05  252.009995  253.820007  248.059998  250.199997  250.199997  23435300         MSFT        MICROSOFT
    2022-12-06  250.820007  251.860001  243.779999  245.119995  245.119995  22463700         MSFT        MICROSOFT
    2022-12-07  244.830002  246.160004  242.210007  244.369995  244.369995  20481500         MSFT        MICROSOFT
    2022-12-08  244.839996  248.740005  243.059998  247.399994  247.399994  22611800         MSFT        MICROSOFT

    [940 rows x 8 columns] 

    # comp_names_abbr
    ['AMZN', 'AAPL', 'GOOG', 'MSFT'] 

    # company_list
    [                Open        High         Low       Close      Adj Close    Volume     company_name     company_fullname
    2022-01-04  170.438004  171.399994  166.349503  167.522003  167.522003  70726000       amazon           AMAZON
    2022-01-05  166.882996  167.126495  164.356995  164.356995  164.356995  64302000       amazon           AMAZON
    2022-01-06  163.450500  164.800003  161.936996  163.253998  163.253998  51958000       amazon           AMAZON
    2022-01-07  163.839005  165.243500  162.031006  162.554001  162.554001  46606000       amazon           AMAZON
    2022-01-10  160.585495  161.661499  156.304504  161.485992  161.485992  87798000       amazon           AMAZON
    ...                ...         ...         ...         ...         ...       ...          ...              ...
    2022-12-02   94.480003   95.360001   93.779999   94.129997   94.129997  72427000       amazon           AMAZON
    2022-12-05   93.050003   94.059998   90.820000   91.010002   91.010002  71535500       amazon           AMAZON
    2022-12-06   90.500000   91.040001   87.900002   88.250000   88.250000  75503600       amazon           AMAZON
    2022-12-07   88.339996   89.889999   87.480003   88.459999   88.459999  68086900       amazon           AMAZON
    2022-12-08   89.239998   90.860001   87.879997   90.349998   90.349998  73305900       amazon           AMAZON

    [235 rows x 8 columns],                   Open        High         Low       Close   Adj Close     Volume company_name company_fullname
    2022-01-04  182.630005  182.940002  179.119995  179.699997  178.663086   99310400        apple            APPLE
    2022-01-05  179.610001  180.169998  174.639999  174.919998  173.910645   94537600        apple            APPLE
    2022-01-06  172.699997  175.300003  171.639999  172.000000  171.007523   96904000        apple            APPLE
    2022-01-07  172.889999  174.139999  171.029999  172.169998  171.176529   86709100        apple            APPLE
    2022-01-10  169.080002  172.500000  168.169998  172.190002  171.196426  106765600        apple            APPLE
    ...                ...         ...         ...         ...         ...        ...          ...              ...
    2022-12-02  145.960007  148.000000  145.649994  147.809998  147.809998   65421400        apple            APPLE
    2022-12-05  147.770004  150.919998  145.770004  146.630005  146.630005   68826400        apple            APPLE
    2022-12-06  147.070007  147.300003  141.919998  142.910004  142.910004   64727200        apple            APPLE
    2022-12-07  142.190002  143.369995  140.000000  140.940002  140.940002   69721100        apple            APPLE
    2022-12-08  142.360001  143.520004  141.100006  142.649994  142.649994   62128300        apple            APPLE

    [235 rows x 8 columns],                   Open        High         Low       Close   Adj Close    Volume company_name company_fullname
    2022-01-04  145.550507  146.610001  143.816147  144.416504  144.416504  22928000       google           GOOGLE
    2022-01-05  144.181000  144.298004  137.523499  137.653503  137.653503  49642000       google           GOOGLE
    2022-01-06  137.497498  139.686005  136.763504  137.550995  137.550995  29050000       google           GOOGLE
    2022-01-07  137.904999  138.254745  135.789001  137.004501  137.004501  19408000       google           GOOGLE
    2022-01-10  135.098999  138.639999  133.140503  138.574005  138.574005  34096000       google           GOOGLE
    ...                ...         ...         ...         ...         ...       ...          ...              ...
    2022-12-02   99.370003  101.150002   99.169998  100.830002  100.830002  18812200       google           GOOGLE
    2022-12-05   99.815002  101.750000   99.355003   99.870003   99.870003  19955500       google           GOOGLE
    2022-12-06   99.669998  100.209999   96.760002   97.309998   97.309998  20877600       google           GOOGLE
    2022-12-07   96.769997   97.309998   95.025002   95.150002   95.150002  26647900       google           GOOGLE
    2022-12-08   95.690002   95.870003   93.800003   93.949997   93.949997  25593200       google           GOOGLE

    [235 rows x 8 columns],                   Open        High         Low       Close   Adj Close    Volume company_name company_fullname
    2022-01-04  334.829987  335.200012  326.119995  329.010010  325.955750  32674300    microsoft        MICROSOFT
    2022-01-05  325.859985  326.070007  315.980011  316.380005  313.442993  40054300    microsoft        MICROSOFT
    2022-01-06  313.149994  318.700012  311.489990  313.880005  310.966187  39646100    microsoft        MICROSOFT
    2022-01-07  314.149994  316.500000  310.089996  314.040009  311.124725  32720000    microsoft        MICROSOFT
    2022-01-10  309.489990  314.720001  304.690002  314.269989  311.352570  44289500    microsoft        MICROSOFT
    ...                ...         ...         ...         ...         ...       ...          ...              ...
    2022-12-02  249.820007  256.059998  249.690002  255.020004  255.020004  21522800    microsoft        MICROSOFT
    2022-12-05  252.009995  253.820007  248.059998  250.199997  250.199997  23435300    microsoft        MICROSOFT
    2022-12-06  250.820007  251.860001  243.779999  245.119995  245.119995  22463700    microsoft        MICROSOFT
    2022-12-07  244.830002  246.160004  242.210007  244.369995  244.369995  20481500    microsoft        MICROSOFT
    2022-12-08  244.839996  248.740005  243.059998  247.399994  247.399994  22611800    microsoft        MICROSOFT

    [235 rows x 8 columns]]

    # comp_names 
    ('amazon', 'apple', 'google', 'microsoft')
    """
    comp_names_abbr = [get_symbol(comp) for comp in comp_names]  

    # Add the queried stock data into a dataframe.
    data_list = []
    for comp, comp_full in zip(comp_names_abbr, comp_names):
        
        # a method to get historical price data from the yahoo finance library from Yahoo Finance Wraper. It takes company symbols as input. 
        hist_data = get_data(comp, start_date=start_date, end_date=end_date,  interval=interval, index_as_date = True) 
        hist_data['company_fullname'] = comp_full.upper() #### adding a new column called "company fullname"?
        data_list.append(hist_data)

    data_list = pd.concat(data_list, axis=0)
    data_list.columns = ['Open','High','Low','Close','Adj Close','Volume','company_name', 'company_fullname']

    # Company list groups the fetched data (data_list) by company.
    company_list = [data_list[data_list['company_fullname'] == comp_full.upper()] for comp_full in comp_names] 

    for company, com_name in zip(company_list, comp_names):
        company["company_name"] = com_name              

    return data_list, comp_names_abbr, company_list, comp_names


def get_closing_price_viz(company_list, comp_names):
    """
    Visualizing the closing price for each company.

    Parameters
    ----------
    company_list: list
        Using the company list from the get_hist_data function.
    comp_names: tuple
        Using the company names from the get_hist_data function.

    Return 
    -------
    Plots of closing prices for each input company.
    """   

    
    plt.figure(figsize=(15, 6))
    plt.subplots_adjust(top=1.25, bottom=1.2)

    for i, company in enumerate(company_list, 1): 
        plt.subplot(2, 2, i)
        company['Adj Close'].plot()
        plt.ylabel('Adj Close')
        plt.xlabel(None)
        plt.title(f"Closing Price of {comp_names[i - 1]}") 
    # generate subplots
    plt.tight_layout()
    plt.show()
  

def get_daily_return_viz(company_list, company_names):
    """
    Visualizing daily return for each input company.

    Parameters
    ----------
    company_list: list
        Using the company list from the get_hist_data function.
    comp_names: tuple
        Using the company names from the get_hist_data function.

    Return 
    -------
    Plots of daily returns for each input company.
    """    
    for i, company in enumerate(company_list, 1):
        company['Daily Return'] = company['Adj Close'].pct_change()
        plt.subplot(2, 2, i)
        company['Daily Return'].hist(bins=50)
        plt.ylabel('Daily Return')
        plt.title(f'{company_names[i - 1]}')
        
    plt.tight_layout()
    plt.show()


def create_pricelist(close_prices, windown_size = 30): 
    """
    This function extracts historical stock data for the queried time interval, and 
    calculates *returns* (ratio of current price with respect to initial price) from the closing price. 
    This function pre-processes data for the prediction function.
    
    Parameters
    ----------
    close_prices: numpy.ndarray
        Stock closing price
        
    window_size: int 
        Window size determines the size of the sliding window.

    Return 
    -------
     result_list: numpy.ndarray

    Examples
    -------
    > output:
    [[ 0.         -0.01889309 -0.02547728 ... -0.07375148 -0.06573169
    -0.05624043]
    [ 0.         -0.00671098 -0.01096999 ... -0.04774057 -0.03806653
    -0.05904524]
    [ 0.         -0.00428778 -0.01082978 ... -0.03156739 -0.05268785
    -0.06525106]
    ...
    [ 0.          0.00650975 -0.03471871 ... -0.21440496 -0.24044398
    -0.26347855]
    [ 0.         -0.04096181 -0.07993366 ... -0.24535652 -0.26824211
    -0.26650083]
    [ 0.         -0.04063639 -0.10591388 ... -0.23698775 -0.23517209
    -0.21883109]]



    """   
    # a list of price for 30 days
    result_list = []
    for i in range(len(close_prices) - (windown_size + 1)): 
        result_list.append(close_prices[i: i + (windown_size + 1)]) 

    normal_data = []
    # ratio 
    for window in result_list:
        window_list = [((float(p) / float(window[0])) - 1) for p in window]
        normal_data.append(window_list)

    result_list = np.array(normal_data)
    return result_list


def predict_future_price(data_list, comp_names_abbr, windown_size=30, predict_window_size=10, predict=True):
    """
    Predict future price. 

    Parameters
    ----------
    data_list: pandas.core.frame.DataFrame
        
    windown_size: int
        Window size determines the size of the sliding window.
    
    predict_window_size: int

    predict: bool
        Whether to predict or not; True/ False
    -------
    > 
    """ 
    # add stock price as an input for the train model.
    if predict:
        for comp_name in comp_names_abbr:
            stock = data_list[data_list['company_name'] == comp_name]
            train_model(stock, comp_name, windown_size, predict_window_size)


def predict_rolling_price(result_list, model, window_size = 30, predict_window_size = 10):
    """
    Predict future stock price in a rolling basis. 

    Parameters
    ----------
    result_list: numpy.ndarray

    model: keras.engine.sequential.Sequential

    window_size: int
        Window size determines the size of the sliding window.
    
    predict_window_size: int

    Return 
    -------
    pred_list: 

    Examples
    -------
    """ 
    pred_list = []
    for i in range(predict_window_size):
  
        x_future = result_list[-window_size:, :-1]
        x_future = np.reshape(x_future, (x_future.shape[0], x_future.shape[1], 1))

        pred = model.predict(x_future)[0][-1]
        pred_list.append(pred)
        
        result_list[:-1,:] = result_list[1:,:] 
        result_list[-1, :-1] = result_list[-1,1:]
        result_list[-1,-1] = pred
    return pred_list


def train_model(stock, comp_name, windown_size=30, predict_window_size=10):
    """
    Build a time series LSTM Model

    Parameters
    ----------
    stock: pandas.core.frame.DataFrame

    comp_name: str
        Company name input.

    windown_size: int
        Window size determines the size of the sliding window to fetch historical data.
    
    predict_window_size: int
         How many days to predict.
    ----------
    """ 

    close_prices = stock['Close'].values
    result_list = create_pricelist(close_prices, windown_size=windown_size)
    
    row = result_list.shape[0] - 20
    train = result_list[:row, :]

    x_train = train[:, :-1]
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    y_train = train[:, -1]

    x_test = result_list[row:, :-1]
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    y_test = result_list[row:, -1]
    
    # First instantiate the model
    model = Sequential()
    # Add the first layer
    model.add(LSTM(windown_size, return_sequences=True, input_shape=(windown_size, 1)))
    # Add the second layer
    model.add(LSTM(64, return_sequences=False))
    # Add the output layer
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    model.summary()

    # train
    model.fit(x_train, y_train,
    validation_data=(x_test, y_test),
    batch_size=10,
    epochs=10)
    
    # predict future prices (finally!)
    pred_list = predict_rolling_price(result_list, model, window_size = windown_size, predict_window_size = predict_window_size)
    
    # generate xticks for ploting
    date_list = [d.strftime('%Y-%m-%d') for d in stock.index]  
    
    for i in range(predict_window_size):
        date_list.append(datetime.datetime.strftime(datetime.datetime.strptime(date_list[-1], '%Y-%m-%d') \
                                                    + datetime.timedelta(days=1), '%Y-%m-%d'))
    
    window = result_list[-1]
    
    # plotting time series prediction
    pred = model.predict(x_test)
    pred_price = []
    for i in pred:
        pred_price.append( (i + 1) * window[0] )

    real_price = []
    for i in y_test:
        real_price.append( (i + 1) * window[0] )

    fig = plt.figure(facecolor='white', figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax.plot(date_list[-(len(real_price)+len(pred_list)):], real_price + [None for _ in range(len(pred_list))] , label='real price')
    ax.plot(date_list[-(len(pred_price)+len(pred_list)):], pred_price + [np.array((p+1)*window[0]) for p in pred_list], label='predicted price')
    ax.set_xlabel("date")
    ax.set_ylabel("closing price")
    ax.set_title(comp_name)
    ax.set_xticklabels(ax.xaxis.get_ticklabels(), rotation = 45)

    every_nth = 5
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)

    ax.legend()
    plt.show()

    return 

def generate_audio(comp_names_abbr, audio_filename='default1.mp3'): 
    """
    Generate an audio file that provides information on company's full name, sector/ industry, and daily PE ratio. 

    Parameters
    ----------
    comp_names_abbr: list
        A list of abbreviated company names (symbols).

    audio_filename: str
        Name of the audiofile.

    Return 
    -------
    default1.mp3  #an mp3 audio file 

    """ 
    info_lists = []
    for comp_name in comp_names_abbr:
        comp_info1 = si.get_quote_table(comp_name)
        comp_info2 = yq.search(comp_name)['quotes'][0] 
        info_list = [comp_info2['shortname'], comp_info1['PE Ratio (TTM)'], comp_info2['sector'], comp_info2['industry']]
        info_lists.append(info_list)
        
    texts = ""

    for info_list in info_lists:
        text = "Hello! Today is {}. The PE Ratio of the selected company {} is {}. The sector and industry of the company is {}, {}. "\
                .format(datetime.datetime.strftime(datetime.datetime.today(), format='%Y-%m-%d'), info_list[0], info_list[1], info_list[2], info_list[3])
        texts += text

    tts = gTTS(text=texts , lang ='en')

    if os.path.isfile(audio_filename):
        splited_filename = audio_filename.split('.') # ['default100', 'mp3']
        curr_num = re.findall(r'\d+', splited_filename[0])[0] # '100'
        curr_num_len = len(curr_num)  # 3
        audio_filename = splited_filename[0][:-curr_num_len] + str(1+int(curr_num)) + '.' + splited_filename[1]

    tts.save(audio_filename)
    playsound(audio_filename)


# if __name__ == "__main__":
#     args = get_args()
#     data_list, comp_names_abbr, company_list, comp_names = get_hist_data(args.comp_names, start_date=args.start_date, end_date=args.end_date)
    

#     print("Company Name: ", comp_names_abbr)
#     #print(data_list.groupby('company_fullname').head(1))
#     print(data_list.groupby('company_fullname').tail(1))
#     print(company_list)
#     get_closing_price_viz(company_list, comp_names)
#     get_daily_return_viz(company_list, comp_names)
#     predict_future_price(data_list,  windown_size=args.window_size, 
#                         predict_window_size=args.prediction_window_size, 
#                         predict = args.predict_future_price)
#     generate_audio(comp_names_abbr, audio_filename=args.audio_filename)
#     sys.exit()

