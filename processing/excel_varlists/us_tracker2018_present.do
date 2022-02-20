* Create variable list for Gallup US Tracker Survey 2018-

display "Enter descriptor for survey (pe,wb,etc): " _request(d)

local y = YEAR in 1

describe,short

summarize YEAR

translate @Results gallup_tracker_`y'${d}_summary.txt, replace

describe, replace

generate select_vars = ""

sort name

export excel position name type varlab select_vars using gallup_tracker_`y'${d}_vars.xlsx, firstrow(variables) replace