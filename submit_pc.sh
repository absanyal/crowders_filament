nres=1

echo "variable xx uloop $nres" > in.variables
echo >> in.variables
printf  "variable vseed universe " >> in.variables
for (( x=0; x<$nres; x++ ))
do
    printf "%i " $RANDOM >> in.variables

done

python3 polymer.py

mkdir -p data
mkdir -p plots

time mpirun -n 16 lmp_mpi -in in_summit.lammps > out.run

rm log.*