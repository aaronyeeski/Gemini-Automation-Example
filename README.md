# Client Registration Testing

Hello, my name is Aaron Yee. This script automates testing for the Institutional Client Registration Form in Gemini’s sandbox environment. I had so much fun working on this and I learned a lot along the way.
If you have any questions, feel free to reach me at: aaronyee2@gmail.com
Thank you for your time!

## Quick Start

Steps needed to run tests:
- Install [Selenium](https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium) run 'pip install selenium'
- Install [webdriver manager](https://github.com/SergeyPirogov/webdriver_manager) run 'pip install webdriver-manager'
- Navigate to script directory and run 'python .\test_client_registration.py' 

## Web resources used

https://selenium-python.readthedocs.io/
https://www.selenium.dev/
https://github.com/SergeyPirogov/webdriver_manager

## Testing environment

This script was run on a windows machine with VS Code and uses the Chrome webdriver.

## Additional comments

This script runs through 12 test cases. 1 happy path and 11 negative test cases. There are many ways this script can be improved and optimized. For starters, I could run the tests in parallel. The tests run in 191.947s on my machine. Partly because the webdriver reinitializes between every test case. But it's slower than I'd like. I could also think of a better way to make the test cases more readable. Each test case is run by passing in a dictionary. As a result, there is a lot of repeated code. 