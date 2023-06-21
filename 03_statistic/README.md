# NSFG Cycle 6 (2002)
The National Survey of Family Growth (NSFG) gathers information on pregnancy and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.

[Codebooks and Documentation](https://www.cdc.gov/nchs/nsfg/nsfg_cycle6.htm)

## Variables

We have already seen two variables in the NSFG dataset, caseid and pregordr, and we have seen that there are 244 variables in total. Following variables are used:

- **caseid** is the integer ID of the respondent.
- **prglngth** is the integer duration of the pregnancy in weeks.
outcome is an integer code for the outcome of the pregnancy. The code 1 indicates a live birth.
- **pregordr** is a pregnancy serial number; for example, the code for a respondent’s first pregnancy is 1, for the second pregnancy is 2, and so on.
- **birthord** is a serial number for live births; the code for a respondent’s first child is 1, and so on. For outcomes other than live birth, this field is blank.
- **birthwgt_lb** and** birthwgt_oz** contain the pounds and ounces parts of the birth weight of the baby.
- **agepreg** is the mother’s age at the end of the pregnancy.
- **finalwgt** is the statistical weight associated with the respondent. It is a floating-point value that indicates the number of people in the U.S. population this respondent represents.


