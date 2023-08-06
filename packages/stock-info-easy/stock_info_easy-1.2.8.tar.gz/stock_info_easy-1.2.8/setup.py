# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['stock_info_easy']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'stock-info-easy',
    'version': '1.2.8',
    'description': 'This package provides user-friendly functions to easily navigate stock information of the companies of their interests. The output results include visualization of closing prices and daily returns, stock prediction for the next twenty days, as well as the company information with sectors and PE ratios.',
    'long_description': '# Stock_Info_Easy\n<Br>\nThis Python package is an implementation of the existing  _yfinance wrapper_, one of the  widely used yahoo finance API wrappers.<br>\n<br>\nMost of the times, the currently available Yahoo finance API wrappers take __company symbols__ as input queries instead of company names. \nThis often causes confusion as it is difficult to guess company symbols by heart. <br>\n(eg. what is the abbreviation form of the company _Apple - is it _APPL?_ _AAPL?_ or _APLE?)_  <br>\n<br>\nTherefore, this package aims to provide an improved functionality of querying by making it possible for users to fetch stock data by __company name(s) alone__. <br><br>\nMoreover, this package will generate stock information in dynamic formats in the form of visualizations, data table, stock price forecast, and an audio file with daily prime stock price.\n<br><Br>\nThe fetched data table includes: <br>\n* _company name, open, high, low, close (closing price), adj close, volume, daily return, and PE ratios._ <br>\n<br>\n\n\n## Installation\n\n```bash\n$ pip install stock_info_easy\n```\n\n\n## Usage\n\n### 1. Fetch Stock Data\nInsert the name of a company inside the `get_hist_data` function. <Br> \nex) [\'amazon\', \'apple\', \'google\', \'microsoft\']\n```python\n\n# if not specifying the "end_date", today\'s date will be selected by default. \n>>> data_list, comp_names_abbr, company_list, comp_names = \\\nstock_info_easy.get_hist_data(([\'amazon\', \'apple\', \'google\', \'microsoft\']), \\\nstart_date="01/04/2022", end_date = "2022-01-10") \n\n```\n\n```python\n\n# To view the stock data as a table, \n# Type "data_list" (to view all) or "company_list[i]", i = index of the company (to view by company). \n\n# stock info of all queried companies.\n\n>>> data_list \n```\n\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/data_list.png" width="700" height="300"/>\n</p>\n<br>\n\n```python\n\n# first company info (amazon).\n\n>>> company_list[0]  \n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[0].png" width="700" height="300"/>\n</p>\n<br>\n\n```python\n\n# second company info (apple).\n\n>>> company_list[1]  \n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[1].png" width="700" height="300"/>\n</p>\n<br>\n```\n\n### 2. Visualization of Closing Price\n\n```python\n\n# To generate a visualization of closing price, copy-paste below function as it is.\n\n>>> get_closing_price_viz(company_list, comp_names) \n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price_.png" width="900" height="400"/>\n</p>\n<br>\n\n### 3. Visualization of Daily Return\n\n```python\n\n# To generate a visualization of Daily Return, copy-paste below function as it is.\n\n>>> get_daily_return_viz(company_list, company_names)\n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/daily_return_.png" width="750" height="430" />\n</p>\n\n### 4. Prime Stock Info on Audio\nThis package provides key stock information such as PE ratio and basic company information of all queries companies in an audio format. \n\n```python\n\n# customize the audio filename in the "audio_filename" parameter.\n\n>>> generate_audio(comp_names_abbr, audio_filename=\'default1.mp3\') \n```\n<br>\n\n### 5. Prediction on Closing Price\nThis package uses the time series LSTM vanila model to predict the closing price. \nLSTM model is built with two hidden LSTM layers followed by a standard feedforward output layer. \n\n```python\n# Write following functions.\n# The window size and prediction window size can be customized. \n\n>>> stock_info_easy.predict_future_price(data_list, comp_names_abbr, \\\nwindown_size=30, predict_window_size=10, predict=True)\n\n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_amazon.png", width="500" height="200" />\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_apple.png", width="500" height="200" />\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_google.png", width="500" height="200" />\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_microsoft.png", width="500" height="200" />\n</p>\n<br>\n\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`stock_info_easy` was created by Shauna Han. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`stock_info_easy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).',
    'author': 'Shauna Han',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/shaunahan/Stock_Info_Easy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
