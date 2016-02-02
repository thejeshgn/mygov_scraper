# mygov_scraper
Scrapes "MyGov.in" public comments and saves into SQLITE. Can also export into CSV, JSON

## Download ##

Downlonad from the releases and or clone the git project.


## Install Dependencies ##
`
pip install -r requirements
`

## To run ##
`
Open spider.py in a text editor and change the following values
total_comments = 2433
start_urls = 'https://mygov.in/group-issue/ministry-railway-invites-suggestions-public-regarding-forthcoming-railway-budget-2016-17/'
issue = "ministry-railway-invites-suggestions-public-regarding-forthcoming-railway-budget-2016-17"

`

and then

`
python scrape.py
`

### Export data as json and csv ####
`
datafreeze export.yaml
`



## Author ##
Thejesh GN <i@thejeshgn.com>
Fingerprint: C7D4 1911 9893 ADAF 27B0 FCAA BFFC 8DD3 C06D D6B0

<table>
  <tr>
    <td><img src="http://www.gravatar.com/avatar/4545b2a84b0ae407abc97ad8f23cc28b?s=60"></td><td valign="middle">Thejesh GN<br><a href="http:/thejeshgn.com">http://thejeshgn.com</a></td>
    <td>i-at-thejeshgn-com <br> GPG ID :  0xBFFC8DD3C06DD6B0</td>
  </tr>
</table>


## License ##
Copyright (C) 2014  Thejesh GN <i@thejeshgn.com>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.