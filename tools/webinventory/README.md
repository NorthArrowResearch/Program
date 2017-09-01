Some instructions on updating the repo

Step one is to get the json inventory that Lambda made. Find it here:

sfr-riverscapesdata/inventory.json --> ./inventory.json 

Step 2 is to get the CSV with the full list of projects from google drive
https://docs.google.com/spreadsheets/d/1hJCiJ7rh1SVmPDMtQpSDhM8Aq9vLBMTYDWGHVCaC3ww

(only get columns 1 and 2) save it as `./rsinclude.csv`

now it's time to push things up:

render the site with jekyll build

then push the _site folder to:

demos.northarrowresearch.com/riverscapes_inventory/

