*** Settings ***
Documentation       Verify version for Domino and Data for US/JP (TAU-767)

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLoginPage
Library             DominoHomePageFilters
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${BROWSER}              headlesschrome
${ROOT}                 ${domino.url}
${OPTIONS}              add_argument("--window-size=1920,1080")

*** Test Cases ***
As a US Domino user, I should be able to see link to version for Domino/Data and linked to Help Verify Control
    log in    ${domino.username}    ${domino.password}
    click version link with version control article     US

As a JP Domino user, I should be able to see link to version for Domino/Data and linked to Help Verify Control
    log in    ${domino.jp_user}    ${domino.password}
    click version link with version control article     JP


*** Keywords ***
Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.7

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
