* Create variable list for Gallup US Tracker Survey 2008-2017

local y = YEAR in 1

describe,short
summarize YEAR

translate @Results gallup_tracker_`y'_summary.txt, replace

describe, replace

generate select_vars = ""

sort name

export excel position name type varlab select_vars using gallup_tracker_`y'_vars.xlsx, firstrow(variables) replace