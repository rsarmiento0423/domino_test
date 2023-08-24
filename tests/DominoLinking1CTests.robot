*** Settings ***
Documentation       Domino Linking 1C test for TAU-623

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLoginPage
Library             DominoHomePageFilters
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Regression

*** Variables ***
${BROWSER}              headlesschrome
${ROOT}                 ${domino.url}
${OPTIONS}              add_argument("--window-size=1920,1080")

*** Test Cases ***
As a Domino user, I should be able to see that the 1C icon on Domino is linked to 1C website
    click 1c icon

*** Keywords ***
Get Domino Objects
    log    ${domino.username}

Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    Get Domino Objects
    set selenium speed  0.5
    log in    ${domino.username}    ${domino.password}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
