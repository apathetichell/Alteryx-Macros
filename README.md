# Alteryx-Macros
Macros for Alteryx.

Current listing:
Quarter creator. Take an Alteryx date and returns quarter start/quarter end (both as dates) and the number of days into a quarter where a date falls as Integer. Note - quarters are set up as 1/4/7/10 start dates.

Python Factorial Calculator (Analytic App) - It's a factorial calculator. It's in Alteryx. It's recursive. Well not exactly - it uses a recursive function in the Python tool. Originally developed for https://community.alteryx.com/t5/Weekly-Challenge/Challenge-74-Build-a-Factorial-Calculator/td-p/65932

Spatial adjuster is a macro which takes in one spatial field and returns the combined entity as a polygon with a matching end point. It should replicate the summarize tool's spatial build feature but provide a spatial object which can be used for spatial analytics. 

ST Dev/DOF macro - takes in one numeric field and various user-desginated inputs most notably Degrees of Freedom and returns at Standard Deviation value. Most notable for providing Standard Deviation of a Sample currently not readily available in Alteryx off-the-shelf tools.
