from datetime import datetime

file_names = [
    "20220101_000438_512_HMII.jpg", "20220102_001038_512_HMII.jpg",
    "20220101_002238_512_HMII.jpg", "20220102_002238_512_HMII.jpg",
    "20220101_004038_512_HMII.jpg", "20220102_004038_512_HMII.jpg",
    "20220101_005238_512_HMII.jpg", "20220102_005238_512_HMII.jpg",
    "20220101_011038_512_HMII.jpg", "20220102_011038_512_HMII.jpg",
    "20220101_012238_512_HMII.jpg", "20220102_012238_512_HMII.jpg",
    "20220101_014038_512_HMII.jpg", "20220102_014038_512_HMII.jpg",
    "20220101_015238_512_HMII.jpg", "20220102_015238_512_HMII.jpg",
    "20220101_021038_512_HMII.jpg", "20220102_021038_512_HMII.jpg",
    "20220101_022238_512_HMII.jpg", "20220102_022238_512_HMII.jpg",
    "20220101_024038_512_HMII.jpg", "20220102_024038_512_HMII.jpg",
    "20220101_025238_512_HMII.jpg", "20220102_025838_512_HMII.jpg",
    "20220101_031038_512_HMII.jpg", "20220102_031038_512_HMII.jpg",
    "20220101_032238_512_HMII.jpg", "20220102_032838_512_HMII.jpg",
    "20220101_034038_512_HMII.jpg", "20220102_034038_512_HMII.jpg",
    "20220101_035838_512_HMII.jpg", "20220102_035238_512_HMII.jpg",
    "20220101_041038_512_HMII.jpg", "20220102_041038_512_HMII.jpg",
    "20220101_042838_512_HMII.jpg", "20220102_042238_512_HMII.jpg",
    "20220101_044038_512_HMII.jpg", "20220102_043438_512_HMII.jpg",
    "20220101_045238_512_HMII.jpg", "20220102_045238_512_HMII.jpg",
    "20220101_051038_512_HMII.jpg", "20220102_050438_512_HMII.jpg",
    "20220101_052838_512_HMII.jpg", "20220102_052238_512_HMII.jpg",
    "20220101_054038_512_HMII.jpg", "20220102_054038_512_HMII.jpg",
    "20220101_055238_512_HMII.jpg", "20220102_055238_512_HMII.jpg",
    "20220101_061038_512_HMII.jpg", "20220102_061038_512_HMII.jpg",
    "20220101_062238_512_HMII.jpg", "20220102_062238_512_HMII.jpg",
    "20220101_064038_512_HMII.jpg", "20220102_064038_512_HMII.jpg",
    "20220101_065238_512_HMII.jpg", "20220102_065238_512_HMII.jpg",
    "20220101_071038_512_HMII.jpg", "20220102_071038_512_HMII.jpg",
    "20220101_072838_512_HMII.jpg", "20220102_072838_512_HMII.jpg",
    "20220101_074038_512_HMII.jpg", "20220102_074038_512_HMII.jpg",
    "20220101_075238_512_HMII.jpg", "20220102_075238_512_HMII.jpg",
    "20220101_081038_512_HMII.jpg", "20220102_080438_512_HMII.jpg",
    "20220101_082838_512_HMII.jpg", "20220102_082238_512_HMII.jpg",
    "20220101_084038_512_HMII.jpg", "20220102_084038_512_HMII.jpg",
    "20220101_085238_512_HMII.jpg", "20220102_085238_512_HMII.jpg",
    "20220101_091038_512_HMII.jpg", "20220102_091038_512_HMII.jpg",
    "20220101_092238_512_HMII.jpg", "20220102_092238_512_HMII.jpg",
    "20220101_000014_512_0335.jpg"
]


date_times = []

for file_name in file_names:
    # Split the file name using '_' as the separator
    parts = file_name.split('_')

    # Extract date and time components
    date_str = parts[0]
    time_str = parts[1]

    # Convert date and time components to a DateTime object
    dt = datetime.strptime(date_str + time_str, "%Y%m%d%H%M%S")

    date_times.append(dt)

# Format DateTime objects as strings with quotes and commas
formatted_dates = ['"{0}"'.format(dt.strftime("%Y-%m-%d %H:%M:%S")) for dt in date_times]

# Join the formatted dates with commas and print
formatted_dates_str = ', '.join(formatted_dates)
print(formatted_dates_str)