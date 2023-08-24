*** Settings ***
Documentation       Domino Analysis List View Tests

Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLocationsPage
Library             DominoAnalysisLocationDetailsPage
Library             DominoShareLocation
Library             DominoSearchField
Library             BaseFactory
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Regression

*** Variables ***
${BROWSER}              headlesschrome
${ROOT}                 ${domino.url}
${LOCATIONS_PATH}       data/GOLDEN-Nov16-2021-39Hospitals-Miami+SanBernadino.csv
${NO_LOCATIONS_MATCH}   data/no_locations_match.csv
${OPTIONS}              add_argument("--window-size=1920,1080")

*** Test Cases ***
Test the pagination of the At-Risk Locations list in the sidebar
    Login as US Analysis User1
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    verify at risk locations
    click show more locations button

Verify Stress test Tab
    Login as US Analysis User2
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    verify at risk locations
    click at risk location
    click stress tab
    assert all lifelines
    assert show your work building lifeline

Verify Top Concerns table at At Risk Side panel
    Login as US Analysis User3
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    verify at risk locations
    click at risk location
    click stress tab
    click top concerns tab
    get top concerns data
    click top concerns community
    assert community recovery curve chart

Location Address that does not match what user uploaded
    Login as US Analysis User1
    Go to locations page
    upload locations    ${NO_LOCATIONS_MATCH}
    verify at risk locations
    click at risk location
    assert address no match

Hazard Simulation (movie)
    Login as US Analysis User2
    Go to locations page
    upload locations    ${LOCATIONS_PATH}
    verify at risk locations
    click at risk location
    click view 3d diagram
    assert show downtime details symbolic view
    click community show details
    assert show your work community downtime
    click play hazard simulation    Mariners Hospital   Flood simulation


*** Keywords ***
Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}

Login as US Analysis User1
    log    ${domino.analysis_us_user1}
    set selenium speed  0.5
    log in    ${domino.analysis_us_user1}    ${domino.password}

Login as US Analysis User2
    log    ${domino.analysis_us_user2}
    set selenium speed  0.5
    log in    ${domino.analysis_us_user2}    ${domino.password}

Login as US Analysis User3
    log    ${domino.analysis_us_user3}
    set selenium speed  0.5
    log in    ${domino.analysis_us_user3}    ${domino.password}

Go to locations page
    open locations page    ${ROOT}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
