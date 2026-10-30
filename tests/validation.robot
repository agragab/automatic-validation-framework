*** Settings ***
Library    ../validators.py

*** Test Cases ***

Temperature Field Empty
    Given defaults are set
    When temperature of reading 0 is ${EMPTY} 
    And temperature validation is ran
    Then sequence of temperature result 0 is 0
    And result of temperature result 0 is False
    And reading of temperature result 0 is Null
    And note of temperature result 0 is Empty Value

Temperature Inside Range
    Given defaults are set
    When temperature of reading 0 is 25
    And temperature validation is ran
    Then sequence of temperature result 0 is 0
    And test of temperature result 0 is Temperature
    And result of temperature result 0 is True
    And reading of temperature result 0 is 25
    And note of temperature result 0 is Temperature is within range

Temperature Outside Lower Range
    Given defaults are set
    When temperature of reading 0 is 15
    And temperature validation is ran
    Then sequence of temperature result 0 is 0
    And test of temperature result 0 is Temperature
    And result of temperature result 0 is False
    And reading of temperature result 0 is 15
    And note of temperature result 0 is WARNING: Temperature is too low

Temperature Outside Higher Range
    Given defaults are set
    When temperature of reading 0 is 65
    And temperature validation is ran
    Then sequence of temperature result 0 is 0
    And test of temperature result 0 is Temperature
    And result of temperature result 0 is False
    And reading of temperature result 0 is 65
    And note of temperature result 0 is WARNING: Temperature is too high

Temperature Higher Edge Case 
    Given defaults are set
    When temperature of reading 0 is 50
    And temperature validation is ran
    Then sequence of temperature result 0 is 0
    And test of temperature result 0 is Temperature
    And result of temperature result 0 is True
    And reading of temperature result 0 is 50
    And note of temperature result 0 is Temperature is within range

Temperature Lower Edge Case 
    Given defaults are set
    When temperature of reading 0 is 20
    And temperature validation is ran
    Then sequence of temperature result 0 is 0
    And test of temperature result 0 is Temperature
    And result of temperature result 0 is True
    And reading of temperature result 0 is 20
    And note of temperature result 0 is Temperature is within range

Exposure Field Empty
    Given defaults are set
    When exposure of reading 0 is ${EMPTY}
    And exposure validation is ran
    Then sequence of exposure result 0 is 0
    And result of exposure result 0 is False
    And reading of exposure result 0 is Null
    And note of exposure result 0 is Empty Value

Exposure Inside Range
    Given defaults are set
    When exposure of reading 0 is 15
    And exposure validation is ran
    Then sequence of exposure result 0 is 0
    And test of exposure result 0 is Exposure
    And result of exposure result 0 is True
    And reading of exposure result 0 is 15
    And note of exposure result 0 is Subject is correctly exposed

Exposure Outside Range
    Given defaults are set
    When exposure of reading 0 is 25
    And exposure validation is ran
    Then sequence of exposure result 0 is 0
    And test of exposure result 0 is Exposure
    And result of exposure result 0 is False
    And reading of exposure result 0 is 25
    And note of exposure result 0 is WARNING: Subject is overexposed

Exposure Lower Edge Case 
    Given defaults are set
    When exposure of reading 0 is 10
    And exposure validation is ran
    Then sequence of exposure result 0 is 0
    And test of exposure result 0 is Exposure
    And result of exposure result 0 is True
    And reading of exposure result 0 is 10
    And note of exposure result 0 is Subject is correctly exposed

Exposure Higher Edge Case 
    Given defaults are set
    When exposure of reading 0 is 20
    And exposure validation is ran
    Then sequence of exposure result 0 is 0
    And test of exposure result 0 is Exposure
    And result of exposure result 0 is True
    And reading of exposure result 0 is 20
    And note of exposure result 0 is Subject is correctly exposed

Focus Error Field Empty
    Given defaults are set
    When focus error of reading 0 is ${EMPTY}
    And focus error validation is ran
    Then sequence of focus_error result 0 is 0
    And result of focus_error result 0 is False
    And reading of focus_error result 0 is Null
    And note of focus_error result 0 is Empty Value

Focus Error Inside Range
    Given defaults are set
    When focus error of reading 0 is 5
    And focus error validation is ran
    Then sequence of focus_error result 0 is 0
    And test of focus_error result 0 is Focus Error
    And result of focus_error result 0 is True
    And reading of focus_error result 0 is 5
    And note of focus_error result 0 is Focus error is acceptable
    
Focus Error Outside Range
    Given defaults are set
    When focus error of reading 0 is 15
    And focus error validation is ran
    Then sequence of focus_error result 0 is 0
    And test of focus_error result 0 is Focus Error
    And result of focus_error result 0 is False
    And reading of focus_error result 0 is 15
    And note of focus_error result 0 is WARNING: Focus Error is outside permitted range

Focus Error Edge Case 
    Given defaults are set
    When focus error of reading 0 is 5
    And focus error validation is ran
    Then sequence of focus_error result 0 is 0
    And test of focus_error result 0 is Focus Error
    And result of focus_error result 0 is True
    And reading of focus_error result 0 is 5
    And note of focus_error result 0 is Focus error is acceptable

Invalid Type
    Given defaults are set
    When temperature of reading 0 is abc
    And type validation is ran
    Then sequence of type result 0 is 0    
    And test of type result 0 is temperature
    And exception of type result 0 is ValueError