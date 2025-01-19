# Python program to evaluate and classify student behaviors

def calculate_academic_score(math, english, science):
    return (math * 0.15) + (english * 0.15) + (science * 0.2)

def calculate_discipline_score(absences, issues):
    # Absences score
    if absences <= 5:
        absence_score = 10
    elif absences <= 10:
        absence_score = 7
    else:
        absence_score = 5

    # Issues score
    if issues == 0:
        issue_score = 10
    elif issues <= 2:
        issue_score = 7
    else:
        issue_score = 5

    return (absence_score * 0.15) + (issue_score * 0.15)

def calculate_behavior_score(social_behavior):
    if social_behavior == "positive":
        return 10 * 0.2
    elif social_behavior == "average":
        return 7 * 0.2
    else:
        return 5 * 0.2

def classify_student(final_score):
    if final_score >= 85:
        return "النموذج المثالي"
    elif final_score >= 70:
        return "المتوازن"
    else:
        return "يحتاج متابعة"

# Main function to calculate and classify student behavior
def main():
    print("\n--- تقييم سلوكيات التلاميذ ---\n")

    # Input student data
    math = float(input("أدخل نقطة الرياضيات: "))
    english = float(input("أدخل نقطة الإنجليزية: "))
    science = float(input("أدخل نقطة العلوم: "))
    absences = int(input("أدخل عدد ساعات الغياب: "))
    issues = int(input("أدخل عدد المشاكل: "))
    social_behavior = input("أدخل السلوك الاجتماعي (positive/average/negative): ").lower()

    # Calculate scores
    academic_score = calculate_academic_score(math, english, science)
    discipline_score = calculate_discipline_score(absences, issues)
    behavior_score = calculate_behavior_score(social_behavior)

    # Final score
    final_score = academic_score * 0.5 + discipline_score * 0.3 + behavior_score * 0.2

    # Classification
    classification = classify_student(final_score)

    # Output results
    print("\n--- النتائج ---")
    print(f"النقاط الأكاديمية: {academic_score:.2f}")
    print(f"نقاط الانضباط: {discipline_score:.2f}")
    print(f"نقاط السلوك الاجتماعي: {behavior_score:.2f}")
    print(f"النقطة النهائية: {final_score:.2f}")
    print(f"تصنيف التلميذ: {classification}")

if __name__ == "__main__":
    main()
