# Stock_Info_Easy

This Python package is an implementation of the existing  _yfinance wrapper_, one of the  widely used yahoo finance API wrappers.<br>
<br>
Most of the times, the currently available finance API wrappers take company symbols as queries instead of company names. 
This often causes confusion as it is difficult to guess company symbols (eg. what is the abbreviation of the company `Apple` - APPL? AAPL? or APLE?)  <br>
<br>
Therefore, this package hopes to provide an improved functionality of querying by enabling users to fetch stock data by company name(s) alone. 
<br>
The fetched data includes: <br>
* _company name, open, high, low, close (closing price), adj close, volume, daily return, and PE ratios._ <br>
<br>
The stock information will be provided in dynamic formats with the use of visualizations, a data table, a stock forecast and an audio file.

## Installation

```bash
$ pip install stock_info_easy
```


## Usage

```python
# Insert the name(s) of company(ies) inside the `get_hist_data` function.  ex) ['amazon', 'apple', 'google', 'microsoft']
>>> data_list, comp_names_abbr, company_list, comp_names = stock_info_easy.get_hist_data((['amazon', 'apple', 'google', 'microsoft']), start_date="01/04/2022", end_date = "2022-01-10") # if don't specify the `end_date`, today's date will be selected by default. 
```

```python
# To view the stock data as a table, type `data_list` to view all or by company `company_list[i]`, i = index of the company. 
>>> company_list[1]  # stock info of all queried companies.
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/data_list.png" width="900" height="400"/>
</p>
<br>
```python
>>> company_list[0]  # first company (amazon) info.
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[0].png" width="900" height="400"/>
</p>
<br>
```python
>>> company_list[1]  # second company (apple) info.
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[1].png" width="900" height="400"/>
</p>
<br>


```

#### 2. Visualization of Closing Price
```python
# To generate a visualization of closing price, copy-paste below function as it is.
>>> get_closing_price_viz(company_list, comp_names) 
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price_.png" width="900" height="400"/>
</p>
<br>

#### 3. Visualization of Daily Return
```python
# To generate a visualization of Daily Return, copy-paste below function as it is.
>>> get_daily_return_viz(company_list, company_names)
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/daily_return_.png" width="750" height="430" />
</p>

#### 4. Audio file on Stock Info
This package provides key stock information such as PE ratio and basic company information of all queries companies in an audio format. 

```python
>>> generate_audio(comp_names_abbr, audio_filename='default1.mp3') # customize the audio filename; by default, the file will be saved as 'default1.mp3'.
```
<br>

#### 5. Prediction on Closing Price
This package uses the time series LSTM vanila model to predict the closing price. 
LSTM model is built with two hidden LSTM layers followed by a standard feedforward output layer. 

```python
# Write following functions.
# The window size and prediction window size can be customized; by default, they are set as 30 days and 10 days respectively. 

>>> stock_info_easy.predict_future_price(data_list, comp_names_abbr, windown_size=30, predict_window_size=10, predict=True)

```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_amazon.png", width="500" height="200" />
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_apple.png", width="500" height="200" />
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_google.png", width="500" height="200" />
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_microsoft.png", width="500" height="200" />
</p>
<br>


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`stock_info_easy` was created by Shauna Han. It is licensed under the terms of the MIT license.

## Credits

`stock_info_easy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).