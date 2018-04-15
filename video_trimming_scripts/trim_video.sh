# Script to trim the PlayOn and other intros from episodes recorded with playon
# This script is used for episodes that all have the same time needed cut.

string="f.mp4"
for filename in //FN-SCOUT/Television/The\ Knick/Season\ 1/*.mp4; do
    newfilename=${filename::-4}
    echo "$newfilename$string"
    
    # Using ffmpeg to trim files.
    # -i for input file (using absolute file name (with path))
    # will copy the original file starting at the below time till the end
    # and name it originalFileNamef.mp4
    ffmpeg -i "$filename" -ss 00:00:23 -c copy "$newfilename$string"
done