string="f.mp4"
s1="s01e01"
for filename in //FN-SCOUT/Television/Westworld/Season\ 1/*.mp4; do
	test=$(basename "$filename")
	if [[ "$test" = *"s01e01"* ]]; 
		then
			newfilename=${filename::-4}
			echo "$filename"
			ffmpeg -i "$filename" -ss 00:00:42 -c copy "$newfilename$string"
	elif [[ "$test" = *"s01e02"* ]]; 
		then
			newfilename=${filename::-4}
			echo "$filename"
			ffmpeg -i "$filename" -ss 00:01:59 -c copy "$newfilename$string"
	elif [[ "$test" = *"s01e06"* ]]; 
		then
			newfilename=${filename::-4}
			echo "$filename"
			ffmpeg -i "$filename" -ss 00:02:26 -c copy "$newfilename$string"
	elif [[ "$test" = *"s01e07"* ]]; 
		then
			newfilename=${filename::-4}
			echo "$filename"
			ffmpeg -i "$filename" -ss 00:02:52 -c copy "$newfilename$string"
	elif [[ "$test" = *"s01e10"* ]]; 
		then
			newfilename=${filename::-4}
			echo "$filename"
			ffmpeg -i "$filename" -ss 00:03:53 -c copy "$newfilename$string"
	else
		newfilename=${filename::-4}
		echo "$filename"
		ffmpeg -i "$filename" -ss 00:02:37 -c copy "$newfilename$string"
	fi
done