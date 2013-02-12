qotd-img
========

Qoute of the day server displaying asciized NASA images of the day

Version 0.1

Setting up
----------
This application depends on two libraries:
 - feedparser, you can get it from http://code.google.com/p/feedparser/
 - PIL, you can get it from your distro's repository or from http://www.pythonware.com/library/

First you have to create SQLite database to be used by application. To do that
just copy file data/qotd-img-empty.sqlite to data/qotd-img.sqlite

Standard TCP port for QOTD is 17, that means that you have to run server as root.
Included `serve-iotd.sh` script will do just that. Run it and it will serve
latest image of the day from database.
Alternatively you can change port number in the same shell script.

Last, but not least, configure cron to fetch NASA Image of the day every day. Use included `grab-iotd.sh`
script to perform this.

Notes
-----
This application violates RFC 865. RFC requests that quote should be less than 512 characters.
Unfortunately for image to fit in 512 symbols it's dimensions has to be 32x16 pixels.
Given that Internet speed has improved slightly since RFC865 was developed 56x56 image size is used.

This application is not an example of how to write proper Python programs, it was coded just for fun in couple of
hours, so judge accordingly.

Send your comments to ovoronin-at-gmail-dot-com
