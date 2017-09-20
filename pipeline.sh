
CORES=4 #if quad-core
TASKS= #put here number of processors -1
PREFIX=DLBT #put the cohort name

function job {
    if [ -e "t1w.nii.gz" ]; then
      echo ""
      echo ${1}
      echo "----------------"
      #FSL robustfov to crop the neck (if included in t1 image FOV)
      robustfov "t1w.nii.gz" "t1w_fov.nii.gz"
      #Bias Field correction N4 instead of freesurfer's standard "N3"
      $ANTSPATH/N4BiasFieldCorrection -d 3 -i "t1w_fov.nii.gz" -o "t1w_fov_N4.nii.gz"
      #Freesurfer complete pipeline
      recon-all -i "t1w_fov_N4.nii.gz" -s ${PREFIX}_${1} -nonuintensitycor -3T -parallel -openmp $CORES -all -qcache > ".freesurfer.log"
    fi
}


count=1

for D in *; do
  if [ -d "${D}" ]; then
    cd $D
    echo $D
    if [ $count -eq "$TASKS" ]; then
			count=1
			wait
			echo "waiting....."
			job $D &
		else
			job $D &
			echo "count = $count"
			count=$((count+1))
		fi
		cd ..

  fi
done
wait
echo ""
echo "Mission Completed!"
