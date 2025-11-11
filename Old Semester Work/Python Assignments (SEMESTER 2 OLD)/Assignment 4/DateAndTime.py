with open("ApplicationLog.csv", "r") as file:
    # Open csv file and reads the header
    header = file.readline().strip().split(",")
    # Finds "Date and Time" and "Source" columns
    date_and_time = header.index("Date and Time")
    source = header.index("Source")

    # Loop throughout the entire csv file
    for line in file:
        fields = line.strip().split(",")
        if len(fields) <= max(date_and_time, source):
            continue  
        
        # Checks for lines that only include "Universal Print"
        if fields[source] == "Universal Print":
            datetime = fields[date_and_time]
            if " " not in datetime:
                continue  
            #Splits each day, time, hour, etc into its own variable
            date,time,_ = datetime.split(" ")
            year,month,day = date.split("-")
            hour,minute,second = time.split(":")

            # Print in the format of hours:seconds \t day:month:year
            print(f"{int(hour)}:{int(second)}\t{int(day)}:{int(month)}:{int(year)}")