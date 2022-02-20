* Create variable list for Gallup World Poll

describe,short
summarize YEAR_WAVE

translate @Results gallup_world_summary.txt, replace

describe, replace

generate select_vars = ""

sort name

export excel position name type varlab select_vars using gallup_world_vars.xlsx, firstrow(variables) replace