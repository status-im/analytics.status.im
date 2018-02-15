# Analytics for Status

Scripts, links and sheets to calculate important metrics.

Right now:
- Monthly Active Contributors
- Monthly Contributor Retention Rate

Currently semi-manual and relying on Google Docs. At some point this will be scripted up and produced for general consumption. Only measures commits for status-react and some comparative-ish projects.

Why measure? See Android app example usage for impact, as well as organizational design. For further information, see FB Growth video linked below.

## Crypto OSS

![Monthly Active Contributors Crypto OSS](mac_crypto_oss.png "Monthly Active Contributors Crypto OSS")

## Images

![Android app usage](app_retention_example.png "Android app usage")

![Monthly Active Contributors](mac_example.png "Monthly Active Contributors")

![Monthly Contributor Retention Rate](mcrr_example.png "Monthly Contributor Retention Rate")

## Links

https://wiki.status.im/Status_Organisational_Design#Goals_of_Organisation

https://docs.google.com/spreadsheets/d/1B9rEC-pxS3-1c_FfevHi0TK9pNJRDLif5NtkpsFKJ30/edit#gid=0

http://startupclass.samaltman.com/courses/lec06/

https://en.wikipedia.org/wiki/Cohort_analysis



## SETUP

sudo apt-get install python-pip
sudo pip install python-dateutil

TODO: -1 vs -2 trailing /

# TODO: Should just work in dir and go everywhere there
./mac.py ~/git-analytics/crypto/bitcoin/ ~/git-analytics/crypto/ccxt/ ~/git-analytics/crypto/go-ethereum/ ~/git-analytics/crypto/litecoin/ ~/git-analytics/crypto/lnd/ ~/git-analytics/crypto/mist/ ~/git-analytics/crypto/parity/ ~/git-analytics/crypto/solidity/ ~/git-analytics/crypto/status-react/ ~/git-analytics/crypto/web3.js/ > crypto-mac.csv

scp blue:~/git-analytics/crypto/crypto-mac.csv .
cat foo.csv | pbcopy
