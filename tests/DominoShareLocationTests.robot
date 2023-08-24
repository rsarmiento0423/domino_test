*** Settings ***
Documentation       Domino Share Location Tests

Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             DominoLoginPage
Library             DominoViewerUser
Library             DominoShareLocation
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
As a Domino contributor, I should not be able to share location with invalid email
    [Tags]  Smoke
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    enter bad inputs to share location     New     User    blahblahblah

As a Domino contributor, I should be able to invite a new user to share location
    [Tags]  Smoke
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    enter valid inputs to share location     New     User    rsarmiento+newuser0117@oneconcern.com

As a Domino contributor, I should able to invite an existing user to share location
    [Tags]  Smoke
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    enter valid inputs to share location     Existing     User    rsarmiento+usviewer1@oneconcern.com

As a Domino contributor, I should be cancel from Share location dialog
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    cancel inputs to share location     New     User    rsarmiento+newuser0116b@oneconcern.com

As a Domino contributor, verify Share button is not enabled with spaces entered in all Share location inputs
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    verify share button disabled    spaces  spaces  spaces

As a Domino contributor, verify Share button is not enabled by default with no inputs
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    verify share button disabled    blank  blank  blank

As a Domino contributor, verify Share button is not enabled when email input is blank
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    verify share button disabled    Test  User  blank

As a Domino contributor, verify Share button is not enabled when last name input is blank
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    verify share button disabled    Test  blank  rsarmiento+usviewer1@oneconcern.com

As a Domino contributor, verify Share button is not enabled when first name input is blank
    log in    ${domino.share_location_user}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    verify share button disabled    blank  User  rsarmiento+usviewer1@oneconcern.com

As new Domino consultant contributor, invite a new user to share location with default locations (TAU-757)
    log in    ${domino.new_us_contributor_consultant}    ${domino.password}
    verify at risk locations
    click at risk location
    click share location button
    enter valid inputs to share location     US     Viewer    rsarmiento+usviewer0508@oneconcern.com

As new Domino non-consultant contributor, verify unable to share location with default locations
    log in    ${domino.new_us_contributor_nonconsultant}    ${domino.password}
    verify at risk locations
    click at risk location
    verify share button not visible


*** Keywords ***
Start TestCase
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.5

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
