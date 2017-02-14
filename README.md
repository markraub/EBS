# EBS
## Eggs, Bacon, Sausage and Spam

![spam gif](http://68.media.tumblr.com/6f70a3509189c6148a25c6782ce41fdc/tumblr_ndjj6nDkt91u0k6deo1_500.gif)


EBS is a simple python program which, using barebone regex searches, can be used to prevent your user's emails from getting owned by spam.

EBS is to be run as a cron job every hour, and will scan over your spam filter logs to see if someone is trying to use spam to pwn a user on your mail server. It will also create a database of filtered IP addresses, and you can easily view these from a web interface so you can add them to a blacklist on your firewall to prevent further access.

Use setup.py to automatically set up the cron job with the appropriate settings. Setup.py has the following configuration by default:

```
path = /opt/EBS/logsample.log

out_log = /opt/EBS/out.log

email = markraub@csh.rit.edu

tolerance = 15

```


