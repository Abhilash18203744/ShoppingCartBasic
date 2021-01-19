# Shopping cart

--------------------------------------------------------------------------------------------------------------------------------
## For setup 

cd shopping_cart

python3 setup.py install

--------------------------------------------------------------------------------------------------------------------------------

## To run test

cd test

python3 -m pytest test_cart.py

--------------------------------------------------------------------------------------------------------------------------------

Following tasks are completed with few assumptions as mentioned in respective tasks.

## Tasks:
- Make the receipt print items in the order that they were added.<br />
    Function used for printing receipt returns list of items in the order they were added.
    This can be passed to front end and generate receipt in given order of items.
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer.<br />
    Function calculates total items and total price.
    Total price added in the receipt can be used as full price to charge the customer.
- Be able to fetch product prices from an external source (json file, database ...).<br />
    A json file is used to fetch the price of available item (json chosen over database option for simplicity).
    If required further product information can be added in the json (or a database can be created).
    Data is fetched only once and used as a shoppingcart class attribute to reduce IO operations (same as creating DB connection while using database).
- Be able to display the product prices in different currencies (not only Euro).<br />
    A receipt can be printed in requested currencies available in currency details json file
- Update the test suite to extend coverage and limit the number of tests which need changing when changes are introduced.<br />
    Test cases are modified as per the changes made in the code e.g. Total price line addition.
    Few test cases are created to test different real world scenarios. Also negative test cases are added.
- Any other changes which improve the reliability of this code in production.<br />
    Code changes done to perform even when unexpected or unanticipated events occur. Necessary validations added.

    Few assumptions are made which rely on the frontend, such as assuming that only an integer number will be provided in request to add the item in cart.
A requirements.txt file is created so that in further development all the required dependencies can be added in it.


