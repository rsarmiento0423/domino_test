*** Settings ***
Documentation       Domino Return Period Tests
...                 Use test accounts: rsarmiento+usshowyourwork1@oneconcern.com, rsarmiento+usshowyourwork2@oneconcern.com
...                 Test accounts should have uploaded CSV file: GOLDEN-Nov16-2021-39Hospitals-Miami+SanBernadino.csv

Library             DominoLoginPage
Library             JSONLibrary
Library             yaml
Library             SeleniumLibrary
Library             Collections
Library             BaseFactory
Library             DominoLocationsPage
Library             DominoShareLocation
Library             DominoAnalysisLocationDetailsPage
Library             DominoHomePageFilters
Library             DominoShowYourWork
Variables           ${ENVFILE}

Test Setup         Open Chrome Browser
Test Teardown      Tear Down Actions
Default Tags       Regression

*** Variables ***
${BROWSER}          headlesschrome
${ROOT}             ${domino.url}
${OPTIONS}          add_argument("--window-size=1920,1080")
${LOCATIONS_PAGE}   /#/locations
${LOCATIONS_PATH}   data/GOLDEN-Nov16-2021-39Hospitals-Miami+SanBernadino.csv

*** Test Cases ***
Bridge asset details should not be displayed in locations details Side panel for US flood hazard
    Log in as ShowYourWork User1
    choose flood
    click at risk location
    click flood bridge lifeline
    assert bridge downtime

Bridge asset details should not be displayed in locations details Side panel for US wind hazard
    Log in as ShowYourWork User1
    choose wind
    click at risk location
    reload page
    click wind bridge lifeline
    assert bridge downtime

Check Bridge lifeline details in 'Show Your Work' for US flood hazard
    Log in as ShowYourWork User1
    choose flood
    click at risk location
    click learn more button
    click bridge side bar link
    assert bridge downtime

Check Bridge lifeline details in 'Show Your Work' for US wind hazard
    Log in as ShowYourWork User1
    choose wind
    click at risk location
    click learn more button
    click bridge side bar link
    assert bridge downtime

Bridge asset details will be displayed in Side panel for US earthquake hazard
    Log in as ShowYourWork User1
    choose earthquake
    click at risk location
    click earthquake bridge lifeline
    assert earthquake bridge downtime

Show Your Work content is displayed in the Side panel for clicked lifeline
    Log in as ShowYourWork User1
    choose earthquake
    click at risk location
    click earthquake airport lifeline
    assert earthquake airport downtime
    assert earthquake airport top3 table
    assert earthquake airport return period chart

Show Your Work return period chart (Community)
    Log in as ShowYourWork User1
    choose flood
    click at risk location
    click flood community lifeline
    assert flood community return period chart

Show Your Work return period chart (Highway)
    Log in as ShowYourWork User1
    choose flood
    click at risk location
    click flood highway lifeline
    assert flood highway return period chart

Show Your Work Lifeline's Average downtime, downtime range, and threshold
    Log in as ShowYourWork User1
    choose flood
    click at risk location
    assert flood community

Back button when showing Learn More in the Analysis Detail Side Panel
    Log in as ShowYourWork User2
    choose earthquake
    click at risk location
    click back button from location details page

Show Your Work - Top 3 impacted Assets Table for Community
    Log in as ShowYourWork User1
    choose flood
    click at risk location
    click flood community lifeline
    get community downtime
    assert flood community top3 table

Show Your Work - Top 3 impacted Assets Table for Highway
    Log in as ShowYourWork User2
    choose flood
    click at risk location
    click flood highway lifeline
    assert flood highway top3 table

Navigation Sidebar in Show Your Work report
    Log in as ShowYourWork User2
    click at risk location
    click learn more button
    assert show your work report
    click side bar links


*** Keywords ***
Log in as ShowYourWork User1
    log     ${domino.syw_us_user1}
    log in  ${domino.syw_us_user1}  ${domino.password}

Log in as ShowYourWork User2
    log     ${domino.syw_us_user2}
    log in  ${domino.syw_us_user2}  ${domino.password}

Open Chrome Browser
    Open browser    ${ROOT}    ${BROWSER}    options=${OPTIONS}
    set selenium speed  0.7

Go to locations page
    open locations page    ${ROOT}

Tear Down Actions
    run keyword if test failed    Fail    Test failed
    run keyword if test failed    capture page screenshot    EMBED
    close browser
