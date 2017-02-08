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

-t or --search-terms  :  add a series of comma delimited search terms surrounded by brackets that you want to add to the hourly regex search. 
  ex. You want to prevent a specific set of ips that you know is malicious, it would look something like
```
  
python3 setup.py -t [207.233.102.1, 10.8.4.2, 129.74.32.1]
  
```
  
-l or --set-level  :  set the search intensity level, a number from 1-5. This will adjust how 
```

python3 setup.py -l 5

```
  
-p or --log-path  :  set the path to your spam filter log file. make sure this file has been chmoded with read permissions
```

python3 setup.py --log-path /var/log/MailScanner/access.log

```
