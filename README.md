# EBS
## Eggs, Bacon, Sausage and Spam

![spam gif](http://68.media.tumblr.com/6f70a3509189c6148a25c6782ce41fdc/tumblr_ndjj6nDkt91u0k6deo1_500.gif)


EBS is a simple python program which, using barebone regex searches, can be used to prevent your user's emails from getting owned by spam.

EBS is to be run as a cron job every hour, and will scan over your spam filter logs to see if someone is trying to use spam to pwn a user on your mail server.

Use setup.py to automatically set up the cron job with the appropriate settings. Setup.py takes the following arguments:

-v or --verbose  :  enables verbose output for the execution of setup.py, generally used to troubleshoot 
```

python3 setup.py --verbose

```

-t or --search-terms  :  add a series of space delimited search terms surrounded by brackets and a space that you want to add to the hourly regex search. Default values [ Blocked SPAM spam quarentine QUARENTINE BLOCKED Quarentined quarentined ] (Your entry will not be appended to this by default, it will replace it) 
```
  
python3 setup.py -t [ 207.233.102.1 10.8.4.2 129.74.32.1 ]
  
```
-a or --append-terms  :  this will make all your search terms be appended to the default list of search terms (only has an effect if -t is defined)
```

python3 setup.py -a -t [foo, bar, foobar] 

```
  
-l or --set-level  :  set the search intensity level, a number from 5-30. This will adjust how many spam emails can come through before a system administrator is notified. Default 15
```

python3 setup.py -l 5

```
  
-p or --log-path  :  set the path to your spam filter log file, this is required. Make sure this file has been chmoded with read permissions
```

python3 setup.py --log-path /var/log/MailScanner/access.log

```

-e or --set-email  :  
