# Stock_Info_Easy

This Python package is an implementation of the existing  __*yfinance wrapper*__, one of the  widely used yahoo finance API wrappers.
One drawback of the existing yahoo finance API wrapper is its inability to fetch stock data using the company name; it can only fetch the data with company symbol registered on the Yahoo Finance. <br><br>
To improve the functionality of the previous wrapper, this package enables a user to query a company with its full name.
By simply typing a company name, this pacakage will generate today's stock information for the company of interest. 

The fetched data includes: <br>
* _company name, open, high, low, close (closing price), adj close, volume, daily return, and PE ratios._ <br>
<br>
The stock information will be provided in dynamic formats with the use of visualizations, a data table, a stock forecast and an audio file.

## Installation

```bash
$ pip install stock_info_easy
```


## Usage
To execute the package, __simply type the names of companies__. <br> 
On the terminal, type:  
```python
# Example: Only specify a company name(s) to query, using all other parameters as default.
>>> Input:
% get_hist_data(['amazon', 'apple', 'microsoft', 'google'], start_date = 01/04/2022, end_date = '01/10/2022') # end_date is today's date by default.

>>> Output: 
[                Open        High         Low       Close      Adj Close    Volume     company_name     company_fullname
    2022-01-04  170.438004  171.399994  166.349503  167.522003  167.522003  70726000       amazon           AMAZON
    2022-01-05  166.882996  167.126495  164.356995  164.356995  164.356995  64302000       amazon           AMAZON
    2022-01-06  163.450500  164.800003  161.936996  163.253998  163.253998  51958000       amazon           AMAZON
    2022-01-07  163.839005  165.243500  162.031006  162.554001  162.554001  46606000       amazon           AMAZON
    2022-01-10  160.585495  161.661499  156.304504  161.485992  161.485992  87798000       amazon           AMAZON
    [5 rows x 8 columns],
    
    Open        High         Low       Close   Adj Close     Volume company_name company_fullname
    2022-01-04  182.630005  182.940002  179.119995  179.699997  178.663086   99310400        apple            APPLE
    2022-01-05  179.610001  180.169998  174.639999  174.919998  173.910645   94537600        apple            APPLE
    2022-01-06  172.699997  175.300003  171.639999  172.000000  171.007523   96904000        apple            APPLE
    2022-01-07  172.889999  174.139999  171.029999  172.169998  171.176529   86709100        apple            APPLE
    2022-01-10  169.080002  172.500000  168.169998  172.190002  171.196426  106765600        apple            APPLE
    [5 rows x 8 columns], 
    
    Open        High         Low       Close   Adj Close    Volume company_name company_fullname
    2022-01-04  145.550507  146.610001  143.816147  144.416504  144.416504  22928000       google           GOOGLE
    2022-01-05  144.181000  144.298004  137.523499  137.653503  137.653503  49642000       google           GOOGLE
    2022-01-06  137.497498  139.686005  136.763504  137.550995  137.550995  29050000       google           GOOGLE
    2022-01-07  137.904999  138.254745  135.789001  137.004501  137.004501  19408000       google           GOOGLE
    2022-01-10  135.098999  138.639999  133.140503  138.574005  138.574005  34096000       google           GOOGLE
    [5 rows x 8 columns],
    
    Open        High         Low       Close   Adj Close    Volume company_name company_fullname
    2022-01-04  334.829987  335.200012  326.119995  329.010010  325.955750  32674300    microsoft        MICROSOFT
    2022-01-05  325.859985  326.070007  315.980011  316.380005  313.442993  40054300    microsoft        MICROSOFT
    2022-01-06  313.149994  318.700012  311.489990  313.880005  310.966187  39646100    microsoft        MICROSOFT
    2022-01-07  314.149994  316.500000  310.089996  314.040009  311.124725  32720000    microsoft        MICROSOFT
    2022-01-10  309.489990  314.720001  304.690002  314.269989  311.352570  44289500    microsoft        MICROSOFT
    [5 rows x 8 columns]]
```

#### 2. Visualization of Closing Price
```python
>>> Input: get_closing_price_viz(company_list, comp_names) # company_list and comp_names are output from the previous function.
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price.png" width="900" height="400"/>
</p>
<br>

#### 3. Visualization of Daily Return
```python
>>> Input: get_daily_return_viz(company_list, company_names)
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/daily_return.png" width="750" height="430" />
</p>

#### 4. Audio file on Stock Info
This package provides key stock information such as PE ratio and basic company information of all queries companies in an audio format. 
```python
% generate_audio(comp_names_abbr, audio_filename='default1.mp3') # insert a filename in audio_filename
```
<br>

#### 5. Prediction on Closing Price
This package uses the time series LSTM vanila model to predict the closing price. 
LSTM model is built with two hidden LSTM layers followed by a standard feedforward output layer. 

```python
# Write following functions 
% create_pricelist(close_prices, windown_size = 30)
% predict_rolling_price(result_list, model, window_size = 30, predict_window_size = 10)
% train_model(stock, comp_name, windown_size=30, predict_window_size=10)
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price_forecast.png", width="850" height="350" />
</p>
<br>


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`stock_info_easy` was created by Shauna Han. It is licensed under the terms of the MIT license.

## Credits

`stock_info_easy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).