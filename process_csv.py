import csv

def read_and_process_csv(file_path):
    total_score = 0
    row_count = 0

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_score += int(row['score'])
            row_count += 1

    average = total_score / row_count if row_count > 0 else 0
    print(f"Processed {row_count} rows.")
    print(f"Average Score: {average:.2f}")

if __name__ == "__main__":
    read_and_process_csv("data.csv")
