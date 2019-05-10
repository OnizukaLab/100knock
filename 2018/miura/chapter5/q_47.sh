python q_47.py > q_47_output.txt
cat q_47_output.txt | cut -f 1 -d $'\t' | sort | uniq -c | sort -r | head -20
echo '-------------------------------------------'
cat q_47_output.txt | cut -f 1,2 -d $'\t' | sort | uniq -c | sort -r | head -20
