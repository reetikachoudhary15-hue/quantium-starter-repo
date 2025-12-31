import csv
import os

DATA_FOLDER = "data"
OUTPUT_FILE = "pink_morsels_sales.csv"

final_rows = []

for filename in os.listdir(DATA_FOLDER):
    if filename.endswith(".csv"):
        file_path = os.path.join(DATA_FOLDER, filename)

        with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row["product"] == "Pink Morsels":
                    quantity = float(row["quantity"])
                    price = float(row["price"])
                    sales = quantity * price

                    final_rows.append({
                        "Sales": sales,
                        "Date": row["date"],
                        "Region": row["region"]
                    })

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as output_file:
    fieldnames = ["Sales", "Date", "Region"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(final_rows)

print("File created successfully")
