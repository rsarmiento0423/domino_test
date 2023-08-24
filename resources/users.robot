*** Settings ***
Documentation  Resource file for Ready automation
Library    JSONLibrary
Library    Collections

*** Keywords ***
Get Domino User
    ${json_obj}=        Load YAML from file     ./data/${ENVFILE}
    ${kcusername}=      Get Value From Json     ${json_obj}     $..kcusername
    ${kcpassword}=      Get Value From Json     ${json_obj}     $..kcpassword
    [Return]    ${kcusername}   ${kcpassword}

