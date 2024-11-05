import csv

# Function to generate country abbreviation
def get_country_abbreviation(country_name):
    words = country_name.split()
    if len(words) == 1:
        return words[0][0].upper() + words[0][1].upper() + words[0][-1].upper()
    else:
        return ''.join(word[0].upper() for word in words)

# Reading from customer_dimension.csv and creating a new file with abbreviations
with open('customer_dimension.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['country_abbreviation']
    
    # Write to a new CSV file with the additional column
    with open('customer_dimension_with_abbreviations.csv', mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Process each row, add abbreviation, and write to new file
        for row in reader:
            row['country_abbreviation'] = get_country_abbreviation(row['country'])
            writer.writerow(row)