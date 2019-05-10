wcl=`wc -l hightemp.txt | awk '{print $1}'`
n=`expr \( ${wcl} + $1 - 1 \) / $1`
split -l ${n} hightemp.txt hightemp-
