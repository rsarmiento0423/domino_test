*** Settings ***
Documentation       Domino Return Period Tests

Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoReturnPeriodFilter
Library             BaseFactory
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${BROWSER}      headlesschrome
${ROOT}         ${domino.url}
${OPTIONS}      add_argument("--window-size=1920,1080")
${fname}        First
${lname}        Last

*** Test Cases ***
Login as Domino User and choose Planning Horizon period filter
    log in    ${domino.username}    ${domino.password}
    user chooses planning horizon year    1    1 year
    planning horizon filter texts should be changed    Planning horizon    1y
    user chooses planning horizon year    5    5 years
    planning horizon filter texts should be changed    Planning horizon    5y
    user chooses planning horizon year    10    10 years
    planning horizon filter texts should be changed    Planning horizon    10y
    user chooses planning horizon year    20    20 years
    planning horizon filter texts should be changed    Planning horizon    20y
    user chooses planning horizon year    30    30 years
    planning horizon filter texts should be changed    Planning horizon    30y

Login as Domino User and choose Return Period filter
    log in    ${domino.username}    ${domino.password}
    user chooses return period year    50    50 years
    return period filter texts should be changed    Return period    50y
    user chooses return period year    100    100 years
    return period filter texts should be changed    Return period    100y
    user chooses return period year    250    250 years
    return period filter texts should be changed    Return period    250y
    user chooses return period year    500    500 years
    return period filter texts should be changed    Return period    500y
    user chooses return period year    1000    1000 years
    return period filter texts should be changed    Return period    1000y

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
