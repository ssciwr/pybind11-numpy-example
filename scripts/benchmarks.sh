# simple bash script to benchmark memory & runtime

echo "#n memory (kb)" > mem_list.txt
cp mem_list.txt mem_array.txt

echo "#n time (seconds)" > time_list.txt
cp time_list.txt time_array.txt

for n in 1000 10000 100000 1000000 10000000 50000000 100000000 200000000 300000000 400000000
do
    m_list=$(./memory.py $n 0)
    m_array=$(./memory.py $n 1)
    echo "${n} ${m_array}" >> mem_array.txt
    echo "${n} ${m_list}" >> mem_list.txt

    t_list=$(./time.py $n 0)
    t_array=$(./time.py $n 1)
    echo "${n} ${t_array}" >> time_array.txt
    echo "${n} ${t_list}" >> time_list.txt
done

for n in 1000000000 2000000000 3000000000 4000000000
do
    m_array=$(./memory.py $n 1)
    echo "${n} ${m_array}" >> mem_array.txt

    t_array=$(./time.py $n 1)
    echo "${n} ${t_array}" >> time_array.txt
done

./plot.py
