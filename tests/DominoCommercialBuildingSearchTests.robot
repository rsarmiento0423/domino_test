*** Settings ***
Documentation       Domino Commercial Building Search Tests

Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoSearchField
Library             BaseFactory
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${BROWSER}      headlesschrome
${ROOT}         ${domino.url}
${OPTIONS}      add_argument("--window-size=1920,1080")

*** Test Cases ***
User search for commercial building in USA
    log in    ${domino.username}    ${domino.password}
    search for commercial building    white house
    assert search results related to search criteria    white house
    search result

*** Keywords ***
Get Domino Objects
    log    ${domino.username}

Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
