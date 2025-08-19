import pandas as pd

def analyze_class(csv_file):
    # Load student data from CSV
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"❌ File '{csv_file}' not found. Skipping...")
        return None

    # Students doing good (A and B)
    good_students = df[df["Grade"].isin(["A", "B"])]

    # Percentage calculation
    percent_good = (len(good_students) / len(df)) * 100 if len(df) > 0 else 0

    # Print class-wise results
    print(f"\n📊 Results for {csv_file}")
    if not good_students.empty:
        print("Students doing good (A & B):")
        print(good_students.to_string(index=False))
    else:
        print("No students are doing good in this class.")

    print(f"➡ Percentage of students doing good: {percent_good:.2f}%")

    return {
        "Class": csv_file,
        "Total Students": len(df),
        "Good Students (A & B)": len(good_students),
        "Percentage Good": round(percent_good, 2)
    }

if __name__ == "__main__":
    # Ask teacher for multiple CSVs
    files = input("Enter CSV filenames separated by spaces (e.g., classA.csv classB.csv): ").split()

    summary_data = []
    total_good, total_students = 0, 0

    for file in files:
        result = analyze_class(file.strip())
        if result:
            summary_data.append(result)
            total_good += result["Good Students (A & B)"]
            total_students += result["Total Students"]

    # Overall summary
    if total_students > 0:
        overall_percent = (total_good / total_students) * 100
        summary_data.append({
            "Class": "Overall",
            "Total Students": total_students,
            "Good Students (A & B)": total_good,
            "Percentage Good": round(overall_percent, 2)
        })

        # Save to CSV
        report_df = pd.DataFrame(summary_data)
        report_df.to_csv("summary_report.csv", index=False)

        print("\n📈 Overall Summary Across Classes")
        print(report_df.to_string(index=False))
        print("\n✅ Summary report saved as 'summary_report.csv'")
    else:
        print("\n⚠ No valid data processed.")
