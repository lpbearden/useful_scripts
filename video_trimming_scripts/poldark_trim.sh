# Script to trim the PlayOn and Cinemax intro from episodes of Poldark

string="f.mp4"
for filename in //FN-SCOUT/Television/Poldark/Season\ 1/*.mp4; do
    test=$(basename "$filename")
    if [[ "$test" = *"s01e02"* ]]; 
        then
            newfilename=${filename::-4}
            echo "$filename"
            ffmpeg -i "$filename" -ss 00:00:39 -c copy "$newfilename$string"
    else
        newfilename=${filename::-4}
        echo "$filename"
        ffmpeg -i "$filename" -ss 00:00:27 -c copy "$newfilename$string"
    fi
done