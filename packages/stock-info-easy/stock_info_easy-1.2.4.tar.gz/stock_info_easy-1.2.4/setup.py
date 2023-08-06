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
    'version': '1.2.4',
    'description': 'This package provides user-friendly functions to easily navigate stock information of the companies of their interests. The output results include visualization of closing prices and daily returns, stock prediction for the next twenty days, as well as the company information with sectors and PE ratios.',
    'long_description': '# Stock_Info_Easy\n\nThis Python package is an implementation of the existing  _yfinance wrapper_, one of the  widely used yahoo finance API wrappers.<br>\n<br>\nMost of the times, the currently available finance API wrappers take company symbols as queries instead of company names. \nThis often causes confusion as it is difficult to guess company symbols (eg. what is the abbreviation of the company `Apple` - APPL? AAPL? or APLE?)  <br>\n<br>\nTherefore, this package hopes to provide an improved functionality of querying by enabling users to fetch stock data by company name(s) alone. \n<br>\nThe fetched data includes: <br>\n* _company name, open, high, low, close (closing price), adj close, volume, daily return, and PE ratios._ <br>\n<br>\nThe stock information will be provided in dynamic formats with the use of visualizations, a data table, a stock forecast and an audio file.\n\n## Installation\n\n```bash\n$ pip install stock_info_easy\n```\n\n\n## Usage\n\n```python\n# Insert the name(s) of company(ies) inside the `get_hist_data` function.  ex) [\'amazon\', \'apple\', \'google\', \'microsoft\']\n>>> data_list, comp_names_abbr, company_list, comp_names = stock_info_easy.get_hist_data(([\'amazon\', \'apple\', \'google\', \'microsoft\']), start_date="01/04/2022", end_date = "2022-01-10") # if don\'t specify the `end_date`, today\'s date will be selected by default. \n```\n\n```python\n# To view the stock data as a table, type `data_list` to view all or by company `company_list[i]`, i = index of the company. \n>>> company_list[1]  # stock info of all queried companies.\n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/data_list.png" width="900" height="400"/>\n</p>\n<br>\n```python\n>>> company_list[0]  # first company (amazon) info.\n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[0].png" width="900" height="400"/>\n</p>\n<br>\n```python\n>>> company_list[1]  # second company (apple) info.\n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[1].png" width="900" height="400"/>\n</p>\n<br>\n\n\n```\n\n#### 2. Visualization of Closing Price\n```python\n# To generate a visualization of closing price, copy-paste below function as it is.\n>>> get_closing_price_viz(company_list, comp_names) \n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price_.png" width="900" height="400"/>\n</p>\n<br>\n\n#### 3. Visualization of Daily Return\n```python\n# To generate a visualization of Daily Return, copy-paste below function as it is.\n>>> get_daily_return_viz(company_list, company_names)\n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/daily_return_.png" width="750" height="430" />\n</p>\n\n#### 4. Audio file on Stock Info\nThis package provides key stock information such as PE ratio and basic company information of all queries companies in an audio format. \n\n```python\n>>> generate_audio(comp_names_abbr, audio_filename=\'default1.mp3\') # customize the audio filename; by default, the file will be saved as \'default1.mp3\'.\n```\n<br>\n\n#### 5. Prediction on Closing Price\nThis package uses the time series LSTM vanila model to predict the closing price. \nLSTM model is built with two hidden LSTM layers followed by a standard feedforward output layer. \n\n```python\n# Write following functions.\n# The window size and prediction window size can be customized; by default, they are set as 30 days and 10 days respectively. \n\n>>> stock_info_easy.predict_future_price(data_list, comp_names_abbr, windown_size=30, predict_window_size=10, predict=True)\n\n```\n<p align="center">\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_amazon.png", width="500" height="200" />\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_apple.png", width="500" height="200" />\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_google.png", width="500" height="200" />\n<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_microsoft.png", width="500" height="200" />\n</p>\n<br>\n\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`stock_info_easy` was created by Shauna Han. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`stock_info_easy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).',
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
