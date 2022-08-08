# Credit Card Fraud

Group 6 Members: Sally Mei, Debolina Bhaumik, Cole Barnes, Kanu Madhok

## Topic Overview

Digital payments and cyber criminal activities are evolving and fraud is very common for both Card-Present and Card-not present type of payments. A dataset containing information on credit card fraud was analyzed using machine learning classification models to determine trends in fraudulent purchases.

## Dataset

[Credit_Card_Fraud_Data](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud)

## Exploratory Data Analysis

Pandas was used to import anad understand the data, while sklearn was used to normalize the data, and matplotlib was used to create bar graphs.

![card_df](Images/card_df.PNG)

The probability of fraud remains constant as the distance from home increases but at a certain distance, the probability spikes to its maximum value, the probability goes from 5% to 35%. 

![distance_from_home](Images/distance_from_home.PNG)

As the distance from last transaction increases, fraud increases too.

![distance_from_last_trans](Images/distance_from_last_trans.PNG)

The below bar graph shows that the probability of fraud remains constant as the distance increases but at a certain distance, the probability spikes from less than 3% all the way to 40% and then to more than 60%. Therefore, higher ratio to median purchase price increases the probability of fraud.

![ratio_to_median_purchase](Images/ratio_to_median_purchase.PNG)

Also, the below graph reveals that repeat retailer don't affect the probability of a transaction being fraud.

![repeat_retailer](Images/repeat_retailer.PNG)

Overall, used pin number transactions are less likely to be a fraud, while, used chip transactions are more likely to be a fraud.

![used_pin](Images/used_pin.PNG)

![used_chip](Images/used_chip.PNG)

## Building Machine Learning Model



