from datetime import datetime 

currentDate = datetime.now()

formattedDate = currentDate.strftime("%m/%d/%Y")

# Print the formatted date
print(formattedDate)
