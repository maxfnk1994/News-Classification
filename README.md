# CIS-622 BIG DATA ANALYTCS CAPSTONE
This repository will show how to classify news headlines with an impact on a stock price change
<br>

## Prerequisites for using this dashboard
The analysis was built in [R](https://www.r-project.org), an open source programming language using the [h2o package](https://www.h2o.ai), a open source leader in AI and machine learning for R. Users will need to download [R](https://cran.uni-muenster.de/) in order to run this analysis and also it is suggested to use [RStudio](https://www.rstudio.com). R is completely free to use. All required code can be found in this github repositroy.

## Input type for calculations
This analysis works with two main input datasets, both are csv files. The first file is about the news headlines from the year 2019. For news headlines, there are a lot API's out there. One example is to use the ["News API"](https://newsapi.org). But you need an API key.

The second dataset is about the stock prices. To get historical data about stock prices, the [Dukascopy](https://www.dukascopy.com/trading-tools/widgets/quotes/historical_data_feed) website. You can filter the date and more features and the data is available via a csv export.


### Input variables for **this analysis**
#### News headline
| Variable             	| Detail                                                                           	|
|----------------------	|----------------------------------------------------------------------------------	|
| Date | Date in the format Month/Day/Year Hour:Min |
| Title | Headline of the news |
| Description | Description of the news |


#### Stock data
| Variable             	| Detail                                                                           	|
|----------------------	|----------------------------------------------------------------------------------	|
| Local time | Time in minutes  |
| Open | Open price of stock |
| High | High price of stock |
| Low | Low price of stock |
| Close | Close price of stock |
| Volume | Volume of stock |


## Story of analysis

 ### 1. Preprocessing of data
    - Subset the news (headline and description) for the stock symbol (e.g. "Apple", and "AAPL"; transformation in lowercases)
    - Iterate through each headline of the subset and count the words, result: table of the most frequently mentioned tags (e.g. update)
    - Create a result dataframe: Symbol, Counts, Tag, Price Difference from minute 1 to minute 15
 
        - For each tag, the price difference from 1-15min will be calculated and to the result dataframe attanded
 
        - Check if there is a statistical difference between the time frames

### 2. Compare the price differences

     - Most profitable time frame
     - Most profitable tag

### 3. Create input data

 Predictors (x) = current close price, Volume, avg. top three tag price difference (normalized)
 
 | Variable             	| Example value                                                                 	|
|----------------------	|----------------------------------------------------------------------------------	|
| Current close price | 150.163 |
| Volume | 822,766 |
| FirstTag | -0.1407 |
| SecondTag | 0.1759 |
| ThirdTag | -0.0137 |
| Outcome (y) | -0.0678 |

 Outcome (y) = Actual price difference for 3 min concerning the headline (normalized)

### 4. Create models with h2o (deep neural network, a multi-layer feedforward neural network)

Paramters:

 1. Input Layers: 4 (Current close price, Volume, FirstTag, SecondTag, ThirdTag)
 2. Hidden Layers: 3 (all possible neuron permutations with 5, 10, 20, 40, 80, 100, 200)
 3. epochs: All layer - neuron permutations will be tested with different numbers of epochs: 10, 100, 1000, 10000
 4. Output Layer: Normalized price difference

 ### 5. Performance Measurement

 1. Minimize errors:
  - After predicting the normalized close price change, the aim is to minimize the error by comparing the different architectures of the network

2. Maximize accuracy:
 - After predicting the normalized close price change, the prediction will be transformed into positive price change (1), no price change (0) and negative price change (-1). The prediction results will be compared with the actual price change (also transformed in these categories) 
 
<br>

Example of picture:!!


![gdp](/03_Images/01_NationalAccount/GDP.gif)

## Privacy and storage
This dashboard can be run locally (for example: [aws server](https://aws.amazon.com/de/)) or on personal machines (mac, windows). But keep in mind that the script will run all in all 1,372 neural networks for each approach. So, it will take time. If you want to save time, you can import the csv files, where the results of each network are stored. These files are stored in this repository. 

## Author

This analysis was created at the School of Science of the [St. Thomas University](http://www.stu.edu) by Max Franke in the class CIS-622 BIG DATA ANALYTCS CAPSTONE.