*** Settings ***
Documentation       Domino Analysis location details side panel Tests${\n}
...                 Test User: Non-consultant US contributor

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLoginPage
Library             DominoLocationsPage
Library             DominoAnalysisLocationDetailsPage
Variables           ${ENVFILE}

Test Setup          Start Testcase
Test Teardown       Tear Down Actions

*** Variables ***
${BROWSER}              headlesschrome
${ROOT}                 ${domino.url}
${LOCATIONS_PATH}       data/GOLDEN-Nov16-2021-39Hospitals-Miami+SanBernadino.csv
${OPTIONS}              add_argument("--window-size=1920,1080")

*** Test Cases ***
User can see the sample data set and see vulnerable locations based on that data set and check the details for first At risk location
    [Tags]  Smoke
    make sure some controls are displayed in at risk list
    click on show more button
    check show more button shows the rest of vulnerable locations
    make sure some controls are displayed in at risk list
    check location name and address are displayed in the details page
    check some controls should displayed in the location details page
    check map scale control value    5 mi
    click back button from location details page
    make sure some controls are displayed in at risk list
    check map scale control value    100 mi

User should be able to zoom-in/out from the map and recenter map
    [Tags]  Regression
    click zoom out button
    click update results button
    check map scale control value   300 mi
    click zoom in button
    click update results button
    check map scale control value   100 mi
    click center map
    check map scale control value   100 mi

User navigates directly to analysis detail for location that no longer exits
    [Tags]  Regression
    click on first at risk location card
    ${at-risk-url}      Get current url
    log  Current URL is ${at-risk-url}
    Go to locations page
    delete all locations
    close browser
    Open Browser      ${at-risk-url}    ${BROWSER}    options=${OPTIONS}
    Login as Domino User
    assert no at risk locations

User opens a saved location details view and later navigates directly to it
    [Tags]  Regression
    click on first at risk location card
    ${at-risk-url1}      Get current url
    log  Expected URL: ${at-risk-url1}
    close browser
    Open Browser      ${at-risk-url1}    ${BROWSER}    options=${OPTIONS}
    Login as Domino User
    ${at-risk-url2}      Get current url
    log  Actual URL: ${at-risk-url2}
    should be equal as strings  ${at-risk-url1}     ${at-risk-url2}

*** Keywords ***
Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5
    Login as Domino User
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    upload message should be visible

Get Domino Objects
    Log    ${domino.username}

Login as Domino User
    Get Domino Objects
    log in    ${domino.username}    ${domino.password}

Go to locations page
    open locations page    ${ROOT}

Get current url
    ${url}=     Get Location
    [Return]    ${url}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
