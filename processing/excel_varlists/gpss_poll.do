* Create variable list for Gallup GPSS

display "Enter the name of the GPSS survey (mood,world,environment,etc): " _request(s)

describe,short

summarize yr

translate @Results gallup_gpss_${s}_summary.txt, replace

describe, replace

generate select_vars = ""

sort name

export excel position name type varlab select_vars using gallup_gpss_${s}_vars.xlsx, firstrow(variables) replace