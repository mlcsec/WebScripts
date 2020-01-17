#!/bin/bash
if [ $# -ne 1 ]; then
    echo -e "Usage: $0 <file>"
else
    cp $1 out.pht
    cp $1 out.phpt
    cp $1 out.phtml
    cp $1 out.php3
    cp $1 out.php4
    cp $1 out.php5
    cp $1 out.php6
    cp $1 out.php%00.gif
    cp $1 out.php%00.png
    cp $1 out.php%00.jpg
    cp $1 out.jpg.php
    cp $1 out.png.php
    cp $1 out.gif.php
fi    
