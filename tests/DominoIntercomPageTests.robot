*** Settings ***
Documentation       Domino Intercom Tests

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLoginPage
Library             DominoIntercomMessagePage
Library             DominoLocationsPage
Variables           ${ENVFILE}

Test Setup          Start Browser
Test Teardown       Tear Down Actions
Default Tags        Regression

*** Variables ***
${BROWSER}              headlesschrome
${ROOT}                 ${domino.url}
${OPTIONS}              add_argument("--window-size=1920,1080")
${NAME}                 Ray
${MESSAGE}              This is a test

*** Test Cases ***
User can view Intercom Message icon is displayed in Home page
     [Tags]  Smoke
    Log     ${domino.username}
    log in  ${domino.username}    ${domino.password}
    assert intercom icon is displayed

Intercom Message is opened successfully
    [Tags]  Smoke
    Log     ${domino.username}
    log in  ${domino.username}    ${domino.password}
    assert intercom icon is displayed
    click intercom icon
    assert intercom screen is opened

User can view intercom message content
    Log     ${domino.username}
    log in  ${domino.username}    ${domino.password}
    assert intercom icon is displayed
    click intercom icon
    assert intercom screen is opened
    assert intercom screen content     ${NAME}

User can send a message to Oneconcern
    Log     ${domino.username}
    log in  ${domino.username}    ${domino.password}
    assert intercom icon is displayed
    click intercom icon
    assert intercom screen is opened
    send intercom message    ${MESSAGE}

User can search for help
    [Tags]  Smoke
    Log     ${domino.username}
    log in  ${domino.username}    ${domino.password}
    assert intercom icon is displayed
    click intercom icon
    assert intercom screen is opened
    search for articles     domino
    assert search results

User can view the domino help page
    [Tags]  Smoke2
    Log     ${domino.username}
    log in  ${domino.username}    ${domino.password}
    open locations page    ${ROOT}
    click help link
    Switch Window    new
    assert help page content

Intercom content should be displayed with the same language as the logged in user (JA)
    switch language
    Log     ${domino.jp_user}
    log in  ${domino.jp_user}    ${domino.password}
    assert intercom icon is displayed
    click intercom icon
    assert intercom screen is opened
    assert japan items


*** Keywords ***
Start Browser
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
