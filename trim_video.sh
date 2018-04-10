string="f.mp4"
for filename in //FN-SCOUT/Television/Poldark/Season\ 1/*.mp4; do
	newfilename=${filename::-4}
	echo "$newfilename$string"
	ffmpeg -i "$filename" -ss 00:00:27 -c copy "$newfilename$string"
done