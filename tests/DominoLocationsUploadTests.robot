*** Settings ***
Documentation       Domino Location Upload Tests

Library             OperatingSystem
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLoginPage
Library             DominoLocationsPage
Library             DominoHomePageFilters
Library             DominoShareLocation
Variables           ${ENVFILE}

Test Setup          Open Chrome Browser
Test Teardown       Tear Down Actions

*** Variables ***
${INVALID USER}         Invaliduser1@oneconcer.com
${INVALID PASSWORD}     092393@@@jJPldj
${ROOT}                 ${domino.url}
${LOCATIONS_PAGE}       /#/locations
${LOCATIONS_PATH}       data/GOLDEN-Nov16-2021-39Hospitals-Miami+SanBernadino.csv
${INVALID_LOCATIONS}    data/invalid_usa_locations_sheet.csv
${9DigitsZipCode}       data/VaccineLocationsCA_9DigitZipcodes.csv
${Not_CSV_file}         data/Image.jpg
${Big_CSV_file}         data/File_has_too_manay_locations.csv
${over_5000_locations}       data/File_has_over_5000_locations.csv


*** Test Cases ***
Upload locations
    [Tags]  Smoke
    Login as Nonconsultant Domino User
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    upload message should be visible
    Go to locations page
    locations processed should be correct    39

Delete locations
    [Tags]  Smoke
    Login as Consultant Domino Admin
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    Go to locations page
    delete all locations
    no locations should be uploaded
    go to domino    ${ROOT}
    locations uploaded should be correct on at risk table    0

Upload locations with invalid locations
    [Tags]  Smoke
    Login as Nonconsultant Domino User
    Go to locations page
    upload locations    ${INVALID_LOCATIONS}
    upload error message should be visible
    Go to locations page
    locations hidden should equal    2
    locations processed should be correct     39

Upload locations with 9 digits zip code
    [Tags]  Smoke
    Login as Nonconsultant Domino Admin
    Go to locations page
    upload locations    ${9DigitsZipCode}
    Go to locations page
    locations processed should be correct     12

Upload Not CSV file
    [Tags]  Smoke
    Login as Nonconsultant Domino User
    Go to locations page
    upload locations    ${Not_CSV_file}
    upload not csv file error message should be visible

Upload a Locations sheet has too many locations to be uploaded in Domino
    [Tags]  Regression
    Login as Nonconsultant Domino User
    Go to locations page
    upload locations    ${Big_CSV_file}
    upload big csv file error message should be visible

As a domino user I should not upload files with over 5000 locations
    [Tags]  Regression
    Login as Nonconsultant Domino User
    Go to locations page
    upload locations    ${over_5000_locations}
    upload more than 5000 locations error should be visible

As a Domino user, I should be able to downloaded the error report
    [Tags]  Smoke
    Login as Nonconsultant Domino User
    Go to locations page
    upload locations    ${9DigitsZipCode}
    upload message should be visible
    click review button
    click view details button
    click download error report
    Verify downloaded CSV file      VaccineLocationsCA_9DigitZipcodes.csv

As a Domino user, I should not be able to upload downloaded vulnerable locations file
    [Tags]  Smoke
    Login as Nonconsultant Domino User
    Go to locations page
    upload locations    ${9DigitsZipCode}
    upload message should be visible
    click review button
    Go to home page
    verify at risk locations
    download vulnerable locations file
    ${file_path}    Verify downloaded CSV file      vulnerableLocations.csv
    Go to locations page
    upload vulnerable locations file    ${file_path}

Compare the uploading results for Download CSV sheet and the original uploaded locations sheet
    [Tags]  Smoke
    Login as Nonconsultant Domino Admin
    Go to locations page
    upload locations    ${9DigitsZipCode}
    upload message should be visible
    click review button
    Go to home page
    download vulnerable locations file
    ${file_path}    Verify downloaded CSV file      vulnerableLocations.csv
    Go to locations page
    assert downloaded csv locations count equals processed locations    ${file_path}

As a Domino user, I should be able to Download and re-upload the Locations sheet Template
    [Tags]  Smoke
    Login as Consultant Domino Admin
    Go to locations page
    download locations template
    ${file_path}    Verify downloaded CSV file      LocationsTemplate.csv
    upload downloaded template      ${file_path}


*** Keywords ***
Open Chrome Browser
    ${chrome_options}      Evaluate    selenium.webdriver.ChromeOptions()
    Call Method    ${chrome_options}    add_argument    --window-size\=1920,1080
    ${prefs}    Create Dictionary    download.default_directory=${OUTPUT DIR}
    Call Method    ${chrome_options}    add_experimental_option    prefs    ${prefs}
    Call Method    ${chrome_options}    add_argument    --headless
    Create WebDriver    Chrome    chrome_options=${chrome_options}
    Go To   ${ROOT}

Verify downloaded CSV file
    [Arguments]     ${csvfile}
    ${file_path}=   Catenate    SEPARATOR=/     ${OUTPUT DIR}   ${csvfile}
    file should exist   ${file_path}
    log     Downloaded CSV file: ${file_path}
    [Return]    ${file_path}

Get Domino Objects
    Log    ${domino.username}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser

Login as Consultant Domino Admin
    Get Domino Objects
    set selenium speed  0.5
    log in    ${domino.consultant_us_admin}    ${domino.password}

Login as Nonconsultant Domino User
    Get Domino Objects
    set selenium speed  0.5
    log in    ${domino.nonconsultant_us_contributor}    ${domino.password}

Login as Nonconsultant Domino Admin
    Get Domino Objects
    set selenium speed  0.5
    log in    ${domino.nonconsultant_us_admin}    ${domino.password}

Go to home page
    open home page    ${ROOT}

Go to locations page
    open locations page    ${ROOT}
