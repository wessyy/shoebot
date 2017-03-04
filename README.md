# Shoebot

Automated bot for Adidas with manual Captcha bypass functionality. Given a user inputted model number, desired size, and Captcha token (if needed), will generate a backdoor link and automatically drive browser to adidas site cart with shoe added.

In order to run:
1) Open up terminal and go into this directory.
2) Activate virtual environment : $ source venv/bin/activate 
3) Run $ python manage.py runserver 
4) Open up new terminal and repeat steps 1 and 2. 
5) Run $ python main.py 
6) Input information for form and click submit 
7) If all information is correct and shoe is in stock, browser will automatically add shoe to cart and open up new tab with shoe in cart.

Enjoy! 
