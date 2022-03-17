# EBAY-ONLINE-AUCTION


Problem Statement:
To avoid the scenario of buying the auctioned items for an uncertainity price.

Here I have created a Machine Learning Model to estimate the price from the data available.

You can estimate the Final Bidding price from this link: https://ebayonlineauction.herokuapp.com/

Data Source:
The data is obtained from https://dphi.tech/challenges/data-sprint-17-online-auction/48/overview/about.

Deployment Platform:Heroku,Flask API,gunicorn,Jinja Template
Software Tools:Python,Scikit Learn,Numpy,Pandas,HTML,CSS

DATA DICTIONARY:

auctionid - unique identifier of an auction

bid - the proxy bid placed by a bidder

bidtime - the time (in days) that the bid was placed, from the start of the auction

bidder - eBay username of the bidder

bidderrate - eBay feedback rating of the bidder

openbid - the opening bid set by the seller

price - the closing price that the item sold for (equivalent to the second highest bid + an increment)
