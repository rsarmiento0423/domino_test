*** Settings ***
Documentation       Domino Search Location Tests${\n}
...                 Test User: Non-consultant US admin

Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoAnalysisLocationDetailsPage
Library             DominoShareLocation
Library             DominoHomePageFilters
Library             DominoLocationsPage
Library             DominoSearchField
Library             BaseFactory
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Regression

*** Variables ***
${BROWSER}          headlesschrome
${ROOT}             ${domino.url}
${LOCATIONS_PATH}   data/GOLDEN-Nov16-2021-39Hospitals-Miami+SanBernadino.csv
${OPTIONS}          add_argument("--window-size=1920,1080")

*** Test Cases ***
User search for commercial building in USA that doesn't exist
    assert no_commercial building    Yellowstone National Park

Search for a location the user already uploaded
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    upload message should be visible
    search for commercial building    Mariners Hospital
    assert search results related to search criteria    Mariners Hospital
    search result

Search for a recently viewed location
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    upload message should be visible
    Go to home page
    verify at risk locations
    click at risk location
    click back button from location details page
    assert recently viewed location     Mariners Hospital

Search for a recently viewed commercial address that was not uploaded as a location
    Go to locations page
    verify no locations uploaded
    Go to home page
    search for commercial building    169 University Ave, Palo Alto, California 94301
    assert search results related to listed first    169 University Avenue

Search for a commercial address using the Name of a place (not the street address) , when the address was not uploaded as a location.
    Go to locations page
    verify no locations uploaded
    Go to home page
    search for commercial building    Moscone Center
    assert search results related to search criteria    Moscone Center

Check the 3D view and Play Hazard simulation for any building that you search for
    Go to locations page
    verify no locations uploaded
    Go to home page
    choose earthquake
    search for commercial building    Steamboat Springs Airport
    assert search results related to listed first    Steamboat Springs Airport
    click view 3d diagram
    click play hazard simulation    Steamboat Springs Airport   Earthquake simulation
    click play button


*** Keywords ***
Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5
    Get Domino Objects
    log in    ${domino.nonconsultant_us_admin}    ${domino.password}

Get Domino Objects
    log    ${domino.nonconsultant_us_admin}

Go to locations page
    open locations page    ${ROOT}

Go to home page
    open home page    ${ROOT}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
