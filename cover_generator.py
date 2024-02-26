import csv
import tkinter as tk
from tkinter import ttk

def fill_cover_letter(template_csv):
    mad_lib = {}

    # Read headers from the cover_letter_data.csv
    with open(template_csv, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

    root = tk.Tk()
    root.title("Select Header Categories")

    canvas = tk.Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    def on_submit():
        for header in headers:
            selected_indices = listbox[header].curselection()
            if selected_indices:
                selected_values = [listbox[header].get(idx) for idx in selected_indices]
                mad_lib[header] = ', '.join(selected_values)
            else:
                mad_lib[header] = listbox[header].get(0) if listbox[header].size() > 0 else ''
        root.destroy()

    listbox_var = {}
    listbox = {}

    for header in headers:
        label = tk.Label(frame, text=f"Select {header}:", padx=10, pady=5)
        label.pack(side="top", anchor="w")

        # Read unique values for each header from the cover_letter_data.csv
        with open(template_csv, 'r') as file:
            reader = csv.DictReader(file)
            options = list(set(row[header] for row in reader))

        listbox_var[header] = tk.StringVar(frame, value=options)
        listbox[header] = tk.Listbox(frame, listvariable=listbox_var[header], selectmode=tk.MULTIPLE)
        listbox[header].pack(side="top", anchor="w", padx=10, pady=(0, 10))  # Increased vertical space


    submit_button = tk.Button(frame, text="Submit", command=on_submit)
    submit_button.pack(side="top", pady=10)

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", on_configure)

    canvas.config(yscrollcommand=scrollbar.set)

    root.mainloop()

    return mad_lib



def generate_cover_letter(data):
    # Template directly defined here
    cover_letter_template = f"""
{data['FullName']}
{data['Address']}
{data['City']}, {data['State']} {data['ZIPCode']}
{data['EmailAddress']}
{data['PhoneNumber']}

Dear {data['HiringManagerName']},

I am writing to express my interest in the {data['JobPosition']} position as advertised on {data['JobSource']}.

In my previous roles, I have honed skills in {data['KeySkills']} which perfectly align 
with the key requirements outlined in the job description.

I am impressed by {data['CompanyAchievements']} at {data['CompanyName']}.
My {data['CompanyConnection']} has fueled my enthusiasm to contribute to your esteemed organization.

During my tenure at {data['PreviousCompany']}, I successfully {data['MyAchievement']}.

My values closely align with {data['CompanyName']}'s culture, and I am excited about the prospect of 
contributing to a company with a mission focused on {data['CompanyMission']} and {data['CompanyValues']}.

I look forward to the opportunity to discuss how my skills and experiences make me a perfect fit 
for the {data['JobPosition']} at {data['CompanyName']}. {data['ClosingStatement']}. Thank you for considering my application.

Sincerely,
{data['FullName']}
"""


    return cover_letter_template

if __name__ == "__main__":
    # Change to actual path of your data CSV file
    csv_file_path = "cover_letter_data.csv"  

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = next(reader)  # Assuming there is only one row of data

    mad_lib_values = fill_cover_letter(csv_file_path)
    cover_letter = generate_cover_letter(mad_lib_values)
    print("\nGenerated Cover Letter:\n")
    print(cover_letter)
