import csv

def generate_csv(output_csv, header_list):
    # Sample data for the CSV file
    

    # Writing to CSV
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header_list)
       # writer.writerows(data)

if __name__ == "__main__":
    # Change to desired output CSV file path
    output_csv_path = "cover_letter_data.csv"  
    header_list = ['FullName', 'Address', 'City', 'State', 'ZIPCode', 'EmailAddress', 'PhoneNumber', 'HiringManagerName', 'JobPosition', 'JobSource', 'KeySkills', 'CompanyAchievements', 'CompanyName', 'CompanyConnection', 'PreviousCompany', 'MyAchievement', 'CompanyMission', 'CompanyValues', 'ClosingStatement']

    generate_csv(output_csv_path, header_list)
    print(f"CSV file '{output_csv_path}' generated successfully.")
