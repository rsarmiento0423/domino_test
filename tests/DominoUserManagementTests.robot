*** Settings ***
Documentation       Domino User Management Tests

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             DominoLoginPage
Library             DominoUserManagementPage
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Smoke

*** Variables ***
${BROWSER}                  headlesschrome
${ROOT}                     ${domino.url}
${UserManagement_PAGE}      /#/usermanagement
${OPTIONS}                  add_argument("--window-size=1920,1080")

*** Test Cases ***
Check that User Managemnt page is not displayed for normal user
    log in     ${domino.nonconsultant_us_contributor}    ${domino.password}
    Open User Management Page
    user management not displayed for normal users

Add a new normal user
    log in    ${domino.nonconsultant_us_admin}    ${domino.password}
    Open User Management Page
    add new normal user details
    click add user button

Add a new Admin user
    log in    ${domino.nonconsultant_us_admin}    ${domino.password}
    Open User Management Page
    ${email}    add new admin user details
    click add user button
    add an existing user details    ${email}

Add user with external email domain
    log in    ${domino.nonconsultant_us_admin}    ${domino.password}
    Open User Management Page
    check that system permit external domain     test@gmail.com

Hide the admin user from themselves in user management screen
    [Tags]  Regression
    log in    ${domino.consultant_us_admin2}    ${domino.password}
    Open User Management Page
    assert hidden_admin user    ${domino.consultant_us_admin2}

Inviting a user with an invalid email address should return an error
    [Tags]  Regression
    log in    ${domino.consultant_us_admin2}    ${domino.password}
    Open User Management Page
    add invalid email

Admin user can edit the details-status for existing users
    [Tags]  Regression
    log in    ${domino.consultant_us_admin2}    ${domino.password}
    Open User Management Page
    edit existing user details

Add user with empty spaces for first and last name (TAU-428)
    [Tags]  Regression
    log in    ${domino.nonconsultant_us_admin}    ${domino.password}
    Open User Management Page
    add first last name empty spaces


*** Keywords ***
Get Domino Objects
    log     ${domino.nonconsultant_us_contributor}

Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5

Open User Management Page
    go to user management page    ${ROOT}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
