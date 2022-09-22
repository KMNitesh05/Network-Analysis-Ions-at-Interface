i="1"
COUNTER=1
while [ $COUNTER -lt 6660 ]; do
	ipython make_layer_pdbs.py $COUNTER
	let COUNTER=COUNTER+1
done
