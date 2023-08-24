*** Settings ***
Documentation       Domino Entitlements
Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             DominoShareLocation
Library             Collections
Library             DominoEntitlementsPage
Library             DominoLocationsPage
Library             DominoSearchField
Library             DominoAnalysisLocationDetailsPage
Library             BaseFactory
Variables           ${ENVFILE}

Test Setup          Start TestCase
Test Teardown       Tear Down Actions
Default Tags        Regression

*** Variables ***
${BROWSER}          headlesschrome
${9DigitsZipCode}   data/VaccineLocationsCA_9DigitZipcodes.csv
${ROOT}             ${domino.url}
${OPTIONS}          add_argument("--window-size=1920,1080")

*** Test Cases ***
A logged in domino user should view Hazards based on the entitlements configured in cs admin (Floods only)
   Get Domino Objects
   log in    ${domino.floods_only_entitlements}    ${domino.password}
   click hazards dropdown
   assert hazards dropdown has only floods

A logged in domino user should view Hazards based on the entitlements configured in cs admin(Floods and earthquakes)
   Get Domino Objects
   log in    ${domino.floods_and_earthquake_entitlements}    ${domino.password}
   click hazards dropdown
   assert hazards dropdown has only floods and earthquakes

A logged in domino user should view Hazards based on the entitlements configured in cs admin (Floods, earthquakes and wind)
   Get Domino Objects
   log in    ${domino.username}    ${domino.password}
   click hazards dropdown
   assert hazards dropdown has all entitlements

A logged in domino user should view lifelines based on the entitlements configured in cs admin (Floods: Highway, community, power, bridges)
    log in    ${domino.floods_only_entitlements}    ${domino.password}
    Go to locations page
    upload locations    ${9DigitsZipCode}
    click a location
    @{entitlement}=    Create List    Community  Highway   Power   Bridge*  Building
    assert side nav objects based on cs admin configurations    ${entitlement}

A logged in domino user should view lifelines based on the entitlements configured in cs admin (Floods: all)
    log in    ${domino.floods_and_earthquake_entitlements}    ${domino.password}
    Go to locations page
    upload locations    ${9DigitsZipCode}
    click a location
    @{entitlement}=    Create List    Community  Highway   Power   Bridge*  Building    Port  Airport
    assert side nav objects based on cs admin configurations    ${entitlement}

A logged in domino user should view lifelines based on the entitlements configured in cs admin(Earthquake: Bridge, ports, Airports)
    log in    ${domino.floods_and_earthquake_entitlements}    ${domino.password}
    click hazards dropdown
    select earth quake
    Go to locations page
    upload locations    ${9DigitsZipCode}
    click a location
    @{entitlement}=    Create List    Bridge  Port  Airport  Building
    Set Selenium Speed    0.5
    assert side nav objects based on cs admin configurations    ${entitlement}

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
Go to locations page
    open locations page    ${ROOT}