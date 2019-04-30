i=1

#for i in {1..10};
#do
#    echo $i;
#done

while [ $i -lt 20 ]
do
    echo $i;
    i=$(($i+1));
done
