*** Settings ***
Documentation       Domino MyProfile Tests

Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoMyProfilePage
Library             BaseFactory
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${BROWSER}                  headlesschrome
${ROOT}                     ${domino.url}
${OPTIONS}                  add_argument("--window-size=1920,1080")
${Invalidpassword}          blahblahblah

*** Test Cases ***
Login as Domino User and view profile
    log in    ${domino.profile_us_user}    ${domino.password}
    open my profile page
    all elements on user profile page should be displayed    ${domino.profile_us_user}

all edit user name fields are displayed
    log in    ${domino.profile_us_user}    ${domino.password}
    open my profile page
    all edit user name fields are displayed

Cancel edit user name
    log in    ${domino.profile_us_user}    ${domino.password}
    open my profile page
    click edit user name button
    cancel edit user name    Ray    Profiler

Edit user name
    log in    ${domino.profile_us_user}    ${domino.password}
    edit user name    Profile    Tester
    assert user name value    Profile   Tester    Ray    Profiler

All Edit Passwords fields are displayed
    log in    ${domino.profile_us_user}    ${domino.password}
    open my profile page
    all edit user password fields are displayed

Check Edit Password validations
    log in    ${domino.profile_us_user}    ${domino.password}
    open my profile page
    click edit password button
    check edit password save button is disabled untill all fields are valid    thepassword

cancel edit password
    log in    ${domino.profile_us_user}    ${domino.password}
    open my profile page
    click edit password button
    cancel edit password

Edit Password with valid values
    log in    ${domino.profile_us_user}    ${domino.password}
    open my profile page
    edit user password    ${domino.password}    ${domino.password}
    edit password success message should be visible
    log out from profile page
    log in    ${domino.profile_us_user}    ${domino.password}

Edit Password with invalid values
    log in     ${domino.profile_us_user}    ${domino.password}
    open my profile page
    edit user password    ${Invalidpassword}    thep@ssworD123
    edit password error message should be visible

*** Keywords ***
Get Domino Objects
    log     ${domino.profile_us_user}

Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
