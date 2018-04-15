# Script to trim the PlayOn and Cinemax intro from episodes of Game of Thrones

string="f.mp4"
for filename in //FN-SCOUT/Television/Game\ Of\ Thrones/Season\ 7/*.mp4; do
    test=$(basename "$filename")
    if [[ "$test" = *"s07e01"* ]]; 
        then
            newfilename=${filename::-4}
            echo "$filename"
            ffmpeg -i "$filename" -ss 00:01:58 -c copy "$newfilename$string"
    elif [[ "$test" = *"s07e02"* ]]; 
        then
            newfilename=${filename::-4}
            echo "$filename"
            ffmpeg -i "$filename" -ss 00:00:44 -c copy "$newfilename$string"
    elif [[ "$test" = *"s07e07"* ]]; 
        then
            newfilename=${filename::-4}
            echo "$filename"
            ffmpeg -i "$filename" -ss 00:01:58 -c copy "$newfilename$string"
    else
        newfilename=${filename::-4}
        echo "$filename"
        ffmpeg -i "$filename" -ss 00:01:29 -c copy "$newfilename$string"
    fi
done