*** Settings ***
Documentation       Domino Financial Loss Calculator Tests

Library             OperatingSystem
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             DominoLoginPage
Library             DominoLocationsPage
Library             DominoAnalysisLocationDetailsPage
Library             DominoHomePageFilters
Library             DominoShareLocation
Library             DominoFinancialLossCalculator
Library             Collections
Variables           ${ENVFILE}

Test Setup          Open Chrome Browser
Test Teardown       Tear Down Actions
Default Tags        Regression

*** Variables ***
${ROOT}                 ${domino.url}
${LOCATIONS_PAGE}       /#/locations
${9DigitsZipCode}       data/VaccineLocationsCA_9DigitZipcodes.csv
${OPTIONS}              add_argument("--window-size=1920,1080")

*** Test Cases ***
As a Domino contributor, I should see Financial Loss Calculator and At-risk side bars collapsible
    Login as FLC US User1
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    expand and collapse side bars

As a Domino user, I should see 'No data available' in the dialog when there's no location type revenues given by user
    Login as FLC US User2
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    assert no data analysis available

As a Domino user, I should see Financial Loss Calculator Help article from side bar
    Login as FLC US User3
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click sidebar flc help link

As a Domino user, I should be able to input by revenue loss for each location type to create the materiality metrics
    Login as FLC US User4
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers

As a Domino user I want a dashboard that summarises the financial loss and materiality estimates
    Login as FLC US User5
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    assert dashboard table and controls
    click first location dashboard
    assert locations details card

As a Domino user, I should be able to reset revenue loss for all location types
    Login as FLC US User1
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    reset annual revenue data   1000.99     2000.11     3456.12

As a Domino user, I should see Financial Loss Calculator Help article for dashboard
    Login as FLC US User2
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    click dashboard flc help link

Data should persist after user inputs the revenue per location type data
    Login as FLC US User3
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    click close flc button
    Go to home page
    log out
    Login as FLC US User3
    click financial losss calculator side bar
    click learn more materiality button

Export the Materiality driver table into a CSV file
    Login as FLC US User4
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    click export button
    Verify downloaded CSV file  VaccineLocationsCA_9DigitZipcodes_FinancialLosses.csv

As a Domino user, I should be able to input materiality threshold
    Login as FLC US User5
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    click settings nav
    enter materiality threshold     50

As a Domino user, I should be able to input by additional cost for each location type from Settings
    Login as FLC US User1
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    click settings nav
    click additional cost
    enter additional cost data  700.23      877.22      900

As a Domino user, I should be able to input by revenue loss for each location type from Settings
    Login as FLC US User2
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    click settings nav
    click annual revenue
    enter annual revenue data   1.99     2.11     3.12  False

As a Domino user, I should see under Materiality Drivers that it is paginated and sorts/displays revenue
    Login as FLC US User3
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    assert dashboard table and controls
    assert column data  loss
    check rows per page

Ability to sort the materiality driver table
    Login as FLC US User4
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    assert dashboard table and controls
    sort location column
    assert column data  location    asc
    sort loss column
    assert column data  loss    asc
    sort downtime column
    assert column data  downtime    asc
    sort lifeline column
    assert column data  lifeline    asc

Verify ability to select a specific property in the materiality driver table
    Login as FLC US User5
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click financial losss calculator side bar
    click setup analysis button
    assert annual revenue input
    enter annual revenue data   1000.99     2000.11     3456.12
    assert dashboard revenue with financial loss drivers
    assert dashboard table and controls
    click locations


*** Keywords ***
Open Chrome Browser
    ${chrome_options}      Evaluate    selenium.webdriver.ChromeOptions()
    Call Method    ${chrome_options}    add_argument    --window-size\=1920,1080
    ${prefs}    Create Dictionary    download.default_directory=${OUTPUT DIR}
    Call Method    ${chrome_options}    add_experimental_option    prefs    ${prefs}
    Call Method    ${chrome_options}    add_argument    --headless
    Create WebDriver    Chrome    chrome_options=${chrome_options}
    Go To   ${ROOT}

Login as FLC US User1
    log    ${domino.flc_us_user1}
    set selenium speed  0.5
    log in    ${domino.flc_us_user1}    ${domino.password}

Login as FLC US User2
    log    ${domino.flc_us_user2}
    set selenium speed  0.5
    log in    ${domino.flc_us_user2}    ${domino.password}

Login as FLC US User3
    log    ${domino.flc_us_user3}
    set selenium speed  0.5
    log in    ${domino.flc_us_user3}    ${domino.password}

Login as FLC US User4
    log    ${domino.flc_us_user4}
    set selenium speed  0.5
    log in    ${domino.flc_us_user4}    ${domino.password}

Login as FLC US User5
    log    ${domino.flc_us_user5}
    set selenium speed  0.5
    log in    ${domino.flc_us_user5}    ${domino.password}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser

Go to locations page
    open locations page    ${ROOT}

Verify downloaded CSV file
    [Arguments]     ${csvfile}
    ${file_path}=   Catenate    SEPARATOR=/     ${OUTPUT DIR}   ${csvfile}
    file should exist   ${file_path}
    log     Downloaded CSV file: ${file_path}
    [Return]    ${file_path}

Go to home page
    open home page    ${ROOT}
