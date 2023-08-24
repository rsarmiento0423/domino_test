*** Settings ***
Documentation       Domino Login Tests

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLoginPage
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${INVALID USER}         Invaliduser1@oneconcer.com
${INVALID PASSWORD}     092393@@@jJPldj
${BROWSER}              headlesschrome
${ROOT}                 ${domino.url}
${OPTIONS}              add_argument("--window-size=1920,1080")

*** Test Cases ***
Login as Domino User
    Get Domino Objects
    log in    ${domino.username}    ${domino.password}
    log out

Login with invalid user and invalid password
    log in    ${INVALID USER}    ${INVALID PASSWORD}
    invalid credentials should show

Login with valid user and invalid password
    log in    ${domino.username}    ${INVALID PASSWORD}
    invalid credentials should show

Login with invalid user and valid password
    log in    ${INVALID USER}    ${domino.password}
    invalid credentials should show

Login with empty user and valid password
    log in    ${EMPTY}    ${domino.password}
    invalid credentials should show

Login with valid user and empty password
    log in    ${domino.username}    ${EMPTY}
    invalid credentials should show

Login with empty user and empty password
    log in    ${EMPTY}    ${EMPTY}
    invalid credentials should show

*** Keywords ***
Get Domino Objects
    log    ${domino.username}

Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    Get Domino Objects
    set selenium speed  0.5

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser

Login with invalid credentials should fail
    [Arguments]    ${username}    ${password}
    Get Domino Objects
    log in    ${username}    ${password}
    invalid credentials should show
