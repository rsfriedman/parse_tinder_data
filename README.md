# parse_tinder_data
Inspired by /r/dataisbeautiful

Following a number of recent posts on reddit's /r/dataisbeautiful about analyzing Tinder data I wanted to analyze some myself. Wrote a simple script to parse through the data that was available. Steps below to use this script yourself.

# Steps to Parse Tinder Data
## To retrieve data:
https://account.gotinder.com/login?from=%2Fdata

## To run script:
`python processData.py 'data.json'`

### Sample output:
>Total number of swipes right: 1235 <br />
Total number of swipes left: 9362 <br />
Total number of  matches: 638 <br />
Total number of matches messaged: 229 <br />
Total times number was given out:  19

## To make a Sankey diagram and display data:
Use http://sankeymatic.com/build/

Input data like so:
> Swipes [1235] Right Swipes <br />
Swipes [9362] Left Swipes <br />
Right Swipes [638] Matches <br />
Right Swipes [597] No Match/Unmatched <br />
Matches [229] Exchanged Messages <br />
Exchanged Messages [23] Exchanged numbers <br />
Exchanged numbers [6] Date <br />

# Notes:
* Script only checks for your number as messages only include your side of the conversation
* Dates or any additional offline context counted manually

