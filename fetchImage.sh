#!/bin/bash
######################################################################
#DownloadImage_Mac.sh
#Author: Kevin M. Addison
#Description: Downloads browse images using start date, end date, channel, and resolution parameters
#Published: 2022-08-04
#Schedule: no schedule
#Input Params: STARTDATE, ENDDATE, CHANNEL, RESOLUTION, DOWNLOAD_PATH
#Date Format: YYYY-MM-DD
#Channels: [0193,0171,0304,0131,0335,0211,0094,1600,1700,HMIB,HMIBC,HMII,HMIIC,HMIIF,HMID]
#Resolutions: [4096,2048,1024,512]
#Commandline Instructions: chmod +x DownloadImage_Mac.sh
#                          ./DownloadImage_Mac.sh 2022-01-01 2022-01-02 0171 512 /PATH/TO/DOWNLOADS
######################################################################

# COMMANDLINE ARGUMENTS
STARTDATE=$1
ENDDATE=$2
CHANNEL=$3
RESOLUTION=$4
DOWNLOAD_PATH=$5

# SDO WEBSITE URL
SDOURL=https://sdo.gsfc.nasa.gov
BROWSEDIR=$SDOURL"/assets/img/browse"

# DOWNLOAD PATH
LOCALDIR=$DOWNLOAD_PATH

# UNIX TIMESTAMPS
STARTSECONDS=$(date -j -u -f "%Y-%m-%d" ${STARTDATE} +"%s")
ENDSECONDS=$(date -j -u -f "%Y-%m-%d" ${ENDDATE} +"%s")

echo -e "\n\n"
echo "Download Images to local directory"
echo "START DATE: "$STARTDATE
echo "END DATE: "$ENDDATE
echo "CHANNEL: "$CHANNEL
echo "RESOLUTION: "$RESOLUTION
echo "DOWNLOAD PATH: "$LOCALDIR
echo -e "\n"

val=0
for (( i=$STARTSECONDS; i<=$ENDSECONDS; i+=86400 ))
do
	NEXTDATEPATH=$(date -j -u -f %s "${i}" +%Y/%m/%d)
	NEXTDATESTRING=$(date -j -u -f %s "${i}" +%Y%m%d)
	URL=${BROWSEDIR}/${NEXTDATEPATH}
	ACCEPT=${NEXTDATESTRING}_*_${RESOLUTION}_${CHANNEL}.jpg
	printf "Downloading Images from: %s\r" "$URL"
	wget -N -q -nd --no-check-certificate --level=1 --recursive -e robots=off --no-parent -R "index.html*" -A $ACCEPT $URL --directory-prefix=$LOCALDIR
done

echo -e "\n"Script complete: $(date)