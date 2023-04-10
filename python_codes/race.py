

kilometer = 5
min = 22
seconds = 47

miles = round ((kilometer * 0.62137), 1 )

totalSeconds = min * 60 + seconds

avgSecPerMile = round(totalSeconds / miles)

print(miles, totalSeconds, avgSecPerMile)

minPerMile = avgSecPerMile // 60

secPerMile = avgSecPerMile % 60

print(minPerMile, " Minutes" , secPerMile, " Seconds " )
