# Script to trim the PlayOn and Cinemax intro from episodes of The Knick

string="f.mp4"
for filename in //FN-SCOUT/Television/The\ Knick/Season\ 2/*.mp4; do
    test=$(basename "$filename")
    if [[ "$test" = *"s02e01"* ]]; 
        then
            newfilename=${filename::-4}
            echo "$filename"
            ffmpeg -i "$filename" -ss 00:00:29 -c copy "$newfilename$string"
    else
        newfilename=${filename::-4}
        echo "$filename"
        ffmpeg -i "$filename" -ss 00:00:23 -c copy "$newfilename$string"
    fi
done