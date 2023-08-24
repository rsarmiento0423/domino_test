*** Settings ***
Documentation       Domino HomePage Filters Tests${\n}
...                 Test User: Non-consultant US admin

Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLocationsPage
Library             DominoHomePageFilters
Library             BaseFactory
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${BROWSER}          headlesschrome
${ROOT}             ${domino.url}
${LOCATIONS_PATH}   data/GOLDEN-Nov16-2021-39Hospitals-Miami+SanBernadino.csv
${OPTIONS}          add_argument("--window-size=1920,1080")

*** Test Cases ***
Login as Domino User and check if all homepage filter are displayed
    [Tags]     Smoke    Sanity
    all filters on homepage should be displayed

User can update climate change filter
    switch climate change filter on off    On
    switch climate change filter on off    Off

Check the threshold filter aspects are displayed
    user_click_on_threshold_filter
    check all threshold filter input fields are displayed

Check the default values for Threshold filter
    user_click_on_threshold_filter
    user to check the default threshold filter values

User can edit the Building threshold value
    user_click_on_threshold_filter
    user can edit the threshold building filter    5
    user_click_on_threshold_filter
    user check the new buildings threshold value    5

User can cancel the changes to the Threshold filter
    user_click_on_threshold_filter
    user to cancel the values changes in threshold filter    16

User can choose to Reset the Threshold filter values to the Default
    user_click_on_threshold_filter
    restore filters to default
    user to check the default threshold filter values

Make sure the Hazard filter list has 3 options for Domino US
    check hazard selector list values for domino us

User can choose different hazard types
    user can choose different hazard types

*** Keywords ***
Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5
    Get Domino Objects
    log in    ${domino.nonconsultant_us_admin}    ${domino.password}
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    upload message should be visible

Get Domino Objects
    log    ${domino.nonconsultant_us_admin}

Go to locations page
    open locations page    ${ROOT}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
