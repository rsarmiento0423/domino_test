*** Settings ***
Documentation       Domino User Management Tests

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             DominoLoginPage
Library             DominoViewerUser
Library             DominoThresholdFilter
Library             DominoSearchField
Library             DominoAnalysisLocationDetailsPage
Library             DominoClimateToggle
Library             Collections
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Regression

*** Variables ***
${BROWSER}                  headlesschrome
${ROOT}                     ${domino.url}
${OPTIONS}                  add_argument("--window-size=1920,1080")

*** Test Cases ***
As a Domino Viewer, I should not be able to upload locations files
    [Tags]  Smoke
    assert manage locations button is not displayed

As a Domino viewer, I should not be able to see any seeded data with at-risk locations
    [Tags]  Smoke
    assert at risk location list is not displayed

As a domino viewer, I should be able to search for individual locations
    [Tags]  Smoke
    search for commercial building    white house
    assert search results related to search criteria    white house
    search result

As a domino viewer user, some UI components should be hidden
    assert manage locations button is not displayed
    assert locations filter dropdown is not displayed

As a Domino viewer, I should be able to view and edit analysis assumption
    edit_climate_assumptions
    edit threshold assumption   9   5
    assert threshold assumptions changed   9   5

As a domino viewer, I should be able to Select built objects locations on the map when searching for an address
    search for commercial building    white house
    assert search results related to search criteria    white house
    search result
    assert side nav objects


*** Keywords ***
Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.7
    Get Domino Objects
    log in    ${domino.viewer_user}    ${domino.password}

Get Domino Objects
    log    ${domino.viewer_user}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
