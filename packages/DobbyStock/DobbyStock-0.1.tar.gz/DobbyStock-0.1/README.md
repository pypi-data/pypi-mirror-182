# Dobbyrandom simulator

Group member : 
- Yiwei Gan : gavinyw@outlook.com 
- Viji Rajagopalan : vijayalakshmi_r.here@yahoo.com


## Directory layout:
| Section | Details|
| -----------| -----------|
|Project repository:| https://github.com/vijina17/InClassCI2022N |
|Main package:| main_package. Modules: Stock_main.py, Buy.py |
|Sub packages:| sub_package. Modules: User.py, bot.py, endgame.py |
|Documentation:| README.md, Game_preview.png |
|Automated test:| to be updated by 19-Dec as part of step 2 |


### Report Coverage
![IMAGE_DESCRIPTION](https://github.com/vijina17/InClassCI2022N/blob/main/coverage_rate.png)


### TRAVIS CI
[![Build Status](https://app.travis-ci.com/vijina17/InClassCI2022N.svg?branch=main)](https://app.travis-ci.com/vijina17/InClassCI2022N)

              
## Documentation:

<<<<<<< HEAD

Write a .md file explaining the function details and how they work [1 mark].

=======
1. preview_of_program(only_User).png - Snapshot of game for user
2. Game preview.jpg - Snapshot of full game with one round
2. README.md - Comprehensive list of files and functions for the program


## Execution steps:

1. Execute one of the script files (refer Scripts section below) and the program will first ask for number of rounds to play. Input number as non-zero integer. (1-10 is recommended if wanting to finish game in < 1 min).
2. User will be shown stock high value, stock low value and available quantity of stock to buy. User can choose not to buy or buy under available quantity. Do not: buy over available quantity, program gives error.
3. User has a limit of 10000 for overall purchase.
4. User can play till the number of rounds are exhausted.
5. If user's stock is higher than available balance or if the volume selected will be more than available balance, user will be shown warnings and program will help direct the user to buy in less volume.
6. In the background, there is a bot user who is competing with the user. Bot user will make decisions based on random and play the same number of rounds as user.
7. Once user's rounds are exhausted, bot user plays and then the program ends by showing final score card and announcing the winner. Final score aka Gain/loss is calculated based on (buy volume * final sell price) - (buy volume * buy price) + cashback. If one player decides to play a round and another passes the round, the amount invested by the player in the given round (buy volume * buy price) is given as cashback to the second player.


## Files and Functions: 

### Scripts

There are two Python script files available for users depending on their operating system, 
1. one for Linux/Mac (start_game.py)
2. another based on Jupyter notebook (Windows_Start_game.ipynb) notebook mainly for Windows

The script includes all main and sub packages of the program and instantiates necessary objects of Stock, User and bot(named Dobby!) and invokes the game. Upon completion of the game, it executes a endgame package to 1. calculate final price of each stock using random and collect game results 2. assess cashback for each player and totals 3. declare winner based on final score card. It also prints the scorecard.

### .py initialization
The start_game.py is the file that initializes the game. 

It imports two .py files(Stock_main.py & Buy.py) from main_package and three.py files(bot.py & endgame.py & User.py) from sub_package.

- After entering "python start_game.py", the terminal will ask user to set the numbers of round of game. 
- During the game, user will decide to buy or pass the round. 
- If user decide to buy, game will lead user to next step for the current price and available volume user can buy. 
- The game will continue still user enter "end" or the number of rounds is reached.
- Then Dobby(bot) will do the same trading process, controlled by the result of random.int.
- After both players finish the game, the game will generate the info as data-frame for both players. 
- The winner is the one with higher profit.
- Game end.


### Main Package

There are two modules that are inherited by user and bot modules. They are present in the main package, details of them are as follows:
a) Stock_main - This manages the stock related information for both the users to commonly play with. It generates stock with a high value, low value and available volume of the stock. These are global variables. The number of different stocks generated is equal to the number of rounds the player wants to play and is input by the user in this module. This also has functions to share the high price, low price and volume of stock outside the class. The values of the stock are generated based on random numbers.
``` class Stock: i. __init__ - This method initializes all stock parameters and also assigns a random value for high, low and available stock. Get the number of rounds to be played from the user.
   ii. get_high_price - This method is used to get the high price list which is a list of all possible high values for the stock.
   iii. get_low_price - This method is used to get the low price list which is a list of all possible low values for the stock.
   iv. get_volume - The available volume for each stock.
   v. get_size - Number of rounds selected to be played by the user.
   vi. __str__ - prints high price, low price and volume lists 
 ```

b) Buy - This manages functions that will allow user to buy and also manages related contraints for the user. It generates a random price for the stock and accepts user input for the amount(volume) of stock user wants to buy. It validates if the user has enough balance to buy and allows only to the extent of outstanding balance and within the available stock limits. It calculates the total expense in purchasing the stock and shares the following information to the User module - 1. buy volume 2. expense in buying the stock (volume*price) 3. random price at which stock is bought by the user.
``` class Buy: i. __init__ - This method initializes all parameters for user to buy new stocks during the game.
   ii. check_balance - This method checks if user has enough balance to buy new stock and returns True or False.
   iii. check_volume - This method checks if available volume of stock is > new stock volume requested by user and returns True or False.
   iv. execute - This method takes in high price, low price, balance, input volume and random price and returns the total expense, random price and volume purchased in the given round by the user.
   v.  buy_stock - This method takes in high price, low price, balance, volume and calculates random price for the stock. It gets the volume that user wants to purchase and executes the buy using execute function. It validates if user is selecting a volume that is within the available balance and stock and handles warnings to get the right volume. 
``` 


### Sub-packages and Modules

The following sub packages are used. User and bot modules inherit stock class. User module also inherits Buy class for executing stock purchases. User as well as bot are two players in the game and both are given an initial balance of 10000.
a) User - User class gets the n number of rounds player has selected to play and the stock high, low information from Stock_main module. It then gets the information from user if the user wants to play or pass the given round and processes following n times: If user selects to play, It then invokes the Buy module to get inputs from user on the volume to be bought and the overall stock price, expense. If user passes the round, it treats the overall expense for the round as zero. It stores the following information and has functions to make them accessible outside the class - total expense, volume and random stock price at purchase/buy.
``` class User that inheritss Stock, Buy classes: 
   i. __init__ - This method initializes all stock parameters using stock object and provides an initial balance of 10000 to play the game. Get the number of rounds to be played from the user.
   ii. check_balance - This method checks if user selected to play or pass the round and returns True or False.
   iii. get_low_price - This method is used to get the low price list which is a list of all possible low values for the stock.
   iv. print_stock_info - The shows details about stock to user to help in purchase, high value and low value and available volume.
   v. process - This is the main function for the class and is executed n number of times (no of rounds selected by the user). It shows the       stock information to the user by calling print_stock_info function and collects user's input to play or pass the round. If calls   check_balance to validate if user has enough balance to buy stock and then calls buy_stock module to execute the stock purchase. It stores the stock buying expense, random buy price and buy volume for the user.
   vi.  get_expense_list - This returns the total expense of each round of stock purchase for the user.
   vii.  get_price_of_stock_buy_list - This returns the stock buy price of each round for the user.
   viii. get_volume - This returns the stock buy volume of each round for the user.
```

b) bot - Bot class will get the object created from Stock class as the inheritance. Bot will receive parameters from stock's object as its private parameters and process them through the following steps: 1. start with the loop and make bot to decide whether it should buy or not (based on the integer generated in random.int). Then bot will start to determine its own balance and buy the available amount of stock. Then bot will store all the parameters after the BUY, such as stock_price, volume_bought, expense. If the bot all the round, the parameters will just take 0 as the result. The result will be output as three array: ['expense'], ['total_stock_price_list'], and ['volume_list'].
```   i. __init__(self, Stock)-  Initialization for all stock parameters using stock obeject (as an inheritance), and set 10000of balance to play the game.
   ii. print_stock_info(self, high, low, vol) - Method to print the stock information, the input will be the paramters from the stock instance.
   iii. buy_stock_rp(self, high_price, low_price, vol=0) - Method to process the "Buying". Gathering paramters from bot and execute the function if is True. Function contains randomness to set the stock price and output an array with three parameters (total_price, buy_price, buy_volume).
   iv. process(self) - Main method, processing the bot's trading strategy. Process is controlled by the result of random package. Most methods ares] covered within a for loop, generating a dict with three parameters['expense'], ['total_stock_price_list'], and ['volume_list'].
   v. get_expense_list(self) - Method to return whole info['expense'].
   vi. get_price_of_stock_buy_list(self) - Method to return whole info['total_stock_price_list'].
   vii. get_volume(self) - Method to return whole ['volume_list'].
```

c) endgame - Endgame is a .py file contains several functions that combine the outputs from User and Both classes. The "cashback" function is used in "start_game.py" to get the total price for stock bought by User and Bot. "buy_stock_rp" function is used to alculating current price for each stock and calculate player win, it adds one more argument for player stock high and low to calculate current price. "final_price" function will generate the final total expense by User and bot.
```   i. cashback(player_1_status, dobby_2_status) - Method generate two results based on the input from User and bot after the game is over. 
   ii. buy_stock_rp(high_price, low_price, vol=0) - Method to calculate current price for each stock and return an arrary with three array-like parameters: total_price, buy_price, buy_volume.
   iii. final_price(status, stock_list) - Method to calculate the final profit from the buy and sell by both user and bot.
```