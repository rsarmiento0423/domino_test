# Domino QA Test Automation

How to use the Domino QA Automation Framework

## Description

This project is for running automated UI tests on Domino, to ensure quality is up to company standards.

## Getting Started

### Prerequisites

* Install Python 3 via either methods below
  * ```brew install python3```
  * https://www.python.org/downloads
* Install chromedriver by either choices below. It is preferred to use brew.
  * https://chromedriver.chromium.org/downloads
  * ```brew install chromedriver```
* Install geckodriver (Firefox) by either choices below. It is preferred to use brew.
  * https://github.com/mozilla/geckodriver/releases
  * ```brew install geckodriver```

### Installing

* ```pip install -r requirements.txt```

### Executing tests
Tests are stored as `.robot` files. When you are looking to see where the test cases are stored, 
they will be in a named robot file under the `tests` directory.
<br />
<br />

#### Decrypt test data
The tests require sensitive information in order to run, therefore they need to be decrypted.
```shell
./decrypt.sh
```
<br />



#### Running singular test files
Note: Default browser is headless chrome. 

To run a single test file use the following as an example:
```
 robot  --outputdir results -P ./library tests/DominoLoginTests.robot
```
Replace `DominoLoginTests.robot` with your desired test file

<br />

#### Running parallel test files

To run parallel tests file use the following as an example:

``` 
pabot --processes 2 --testlevelsplit --outputdir results  -P ./library tests/DominoLoginTests.robot
```
* ```--processes``` denotes how many browsers to run at once
* Adding `-v browser:browser_name` to the command will change the browser to Chrome. 
* Browser names can be `headlesschrome`, `headlessfirefox`, `chrome` or `firefox`
  * Headless browsers are browsers that open an actual browser but use the drivers to run the test on the browser "under the hood".

To run tests with multiple browsers at once. 

```
pabot  --argumentfile1 chrome.txt  --argumentfile2 firefox.txt --verbose  --processes 4 --testlevelsplit --outputdir results  -P ./library tests/DominoLoginTests.robot
```
This will use both `headlesschrome` and `headlessfirefox` as defined in `chrome.txt` and `firefox.txt`

Replace `DominoLoginTests.robot` with your desired test file
<br />
<br />

#### Running all tests files in parallel

To run all the test files in parallel in the `tests` directory, run the following.

``` 
pabot --processes 2 --testlevelsplit --outputdir results  -P ./library tests/*.robot
```
<br />

#### Results

Results will be outputted to the `results` directory. 
<br />
<br />
In that directory you will find `report.html` which you can open in a browser to view the full report of passes or failures as well as logs.
<br />
<br />
Screenshots from failures are stored in the parent directory like the following example format: `element_not_found_timestamp.png`


## Help

The QA team is open to help if needed. Please reach out to us on Slack under the tag `@qa`!

## Authors

Contributors names and contact info


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change 
contact: rsarmiento@oneconcern.com

