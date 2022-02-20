* Create variable list for Gallup COVID-19 Survey

describe,short
summarize WAVE_MONTH

translate @Results gallup_covid_summary.txt, replace

describe, replace

generate select_vars = ""

sort name

export excel position name type varlab select_vars using gallup_covid_vars.xlsx, firstrow(variables) replace