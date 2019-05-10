python q_45.py > q_45_output.txt
cat q_45_output.txt | sort | uniq -c | sort -r | head -20
echo '-------------------------------------------'
cat q_45_output.txt | grep '^する' | sort | uniq -c | sort -r
echo '-------------------------------------------'
cat q_45_output.txt | grep '^見る' | sort | uniq -c | sort -r
echo '-------------------------------------------'
cat q_45_output.txt | grep '^与える' | sort | uniq -c | sort -r
