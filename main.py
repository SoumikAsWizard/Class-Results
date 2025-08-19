import pandas as pd
import matplotlib.pyplot as plt
import os

# Grade mapping function
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

def analyze_class(csv_file, good_grades):
    # Load student data from CSV
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"❌ File '{csv_file}' not found. Skipping...")
        return None

    # Ensure file has Marks column
    if "Marks" not in df.columns:
        print(f"⚠ CSV {csv_file} must contain a 'Marks' column. Skipping...")
        return None

    # Convert Marks → Grade
    df["Grade"] = df["Marks"].apply(get_grade)

    # Students doing good
    good_students = df[df["Grade"].isin(good_grades)]

    # Weak students
    weak_students = df[df["Grade"].isin(["D", "F"])]

    # Percentage calculation
    percent_good = (len(good_students) / len(df)) * 100 if len(df) > 0 else 0

    # Print class-wise results
    print(f"\n📊 Results for {csv_file}")
    print("Students doing good:")
    if not good_students.empty:
        print(good_students[["Name", "Marks", "Grade"]].to_string(index=False))
    else:
        print("No students are doing good in this class.")

    if not weak_students.empty:
        print("\n⚠ Weak students (D & F):")
        print(weak_students[["Name", "Marks", "Grade"]].to_string(index=False))

    print(f"\n➡ Percentage of students doing good: {percent_good:.2f}%")

    # Grade distribution chart
    plt.figure(figsize=(6,4))
    grade_counts = df["Grade"].value_counts().sort_index()
    grade_counts.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title(f"Grade Distribution - {csv_file}")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=0)
    chart_file = f"{os.path.splitext(csv_file)[0]}_chart.png"
    plt.savefig(chart_file)
    plt.close()
    print(f"📈 Grade distribution chart saved as {chart_file}")

    return {
        "Class": csv_file,
        "Total Students": len(df),
        "Good Students": len(good_students),
        "Weak Students": len(weak_students),
        "Percentage Good": round(percent_good, 2)
    }

if __name__ == "__main__":
    # Ask teacher for multiple CSVs
    files = input("Enter CSV filenames separated by spaces (e.g., classA.csv classB.csv): ").split()

    # Ask what counts as "doing good"
    threshold = input("Enter good grades (comma separated, e.g., A,B): ").replace(" ", "").split(",")
    good_grades = [g.strip().upper() for g in threshold if g.strip()]

    summary_data = []
    total_good, total_students = 0, 0
    total_weak = 0

    for file in files:
        result = analyze_class(file.strip(), good_grades)
        if result:
            summary_data.append(result)
            total_good += result["Good Students"]
            total_weak += result["Weak Students"]
            total_students += result["Total Students"]

    # Overall summary
    if total_students > 0:
        overall_percent = (total_good / total_students) * 100
        summary_data.append({
            "Class": "Overall",
            "Total Students": total_students,
            "Good Students": total_good,
            "Weak Students": total_weak,
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
