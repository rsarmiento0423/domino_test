*** Settings ***
Documentation       Domino ROI Analysis Tests

Library             OperatingSystem
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             DominoLoginPage
Library             DominoLocationsPage
Library             DominoAnalysisLocationDetailsPage
Library             DominoHomePageFilters
Library             DominoShareLocation
Library             DominoSearchField
Library             DominoROIAnalysis
Library             Collections
Variables           ${ENVFILE}

Test Setup          Open Chrome Browser
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${ROOT}                 ${domino.url}
${LOCATIONS_PAGE}       /#/locations
${ROI_ANALYSIS}         data/roi_analysis.csv
${9DigitsZipCode}       data/VaccineLocationsCA_9DigitZipcodes.csv
${OPTIONS}              add_argument("--window-size=1920,1080")

*** Test Cases ***
Verify ROI analysis for Office 15
    Login as ROI US User1
    Go to locations page
    upload locations    ${ROI_ANALYSIS}
    verify at risk locations
    click at risk location
    click view 3d diagram
    click power roi notification
    assert power roi analysis headers

Verify ROI analysis for Campus Pharmacy
    Login as ROI US User2
    Go to locations page
    upload locations    ${9DigitsZipCode}
    verify at risk locations
    click at risk location
    click view 3d diagram
    click power roi notification
    assert power roi analysis headers

Show intercom article for power downtime mitigation
    Login as ROI US User3
    Go to locations page
    upload locations    ${ROI_ANALYSIS}
    verify at risk locations
    click at risk location
    click view 3d diagram
    click power roi notification
    click roi analysis help


*** Keywords ***
Open Chrome Browser
    ${chrome_options}      Evaluate    selenium.webdriver.ChromeOptions()
    Call Method    ${chrome_options}    add_argument    --window-size\=1920,1080
    ${prefs}    Create Dictionary    download.default_directory=${OUTPUT DIR}
    Call Method    ${chrome_options}    add_experimental_option    prefs    ${prefs}
    Call Method    ${chrome_options}    add_argument    --headless
    Create WebDriver    Chrome    chrome_options=${chrome_options}
    Go To   ${ROOT}

Login as ROI US User1
    log    ${domino.roi_us_user1}
    set selenium speed  0.5
    log in    ${domino.roi_us_user1}    ${domino.password}

Login as ROI US User2
    log    ${domino.roi_us_user2}
    set selenium speed  0.5
    log in    ${domino.roi_us_user2}    ${domino.password}

Login as ROI US User3
    log    ${domino.roi_us_user3}
    set selenium speed  0.5
    log in    ${domino.roi_us_user3}    ${domino.password}

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
