import asyncio
import pandas as pd






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

    return ((absence_score * 0.15) + (issue_score * 0.15))*10

def calculate_behavior_score(social_behavior):
    if social_behavior == "positive":
        return 10 * 0.2 * 10
    elif social_behavior == "average":
        return 7 * 0.2 * 10
    else:
        return 5 * 0.2 * 10

def classify_student(final_score):

    if final_score >= 85:
        return "Ideal Model"
    elif final_score >= 70:
        return "Balanced"
    else:
        return "Needs Follow-up"

async def process_student(row):
    academic_score = calculate_academic_score(row['Math_Score'], row['English_Score'], row['Science_Score'])
    discipline_score = calculate_discipline_score(row['Absences'], row['Issues'])
    behavior_score = calculate_behavior_score(row['Social_Behavior'])

    # Final score
    final_score = academic_score  + discipline_score  + behavior_score


    # Classification
    classification = classify_student(final_score)

    return classification


async def main():

    print(calculate_behavior_score('positive'))
    print(calculate_behavior_score('average'))
    print(calculate_behavior_score('negative'))

    dataset = pd.read_csv('d:/Repos/Python/Studient-Behavior-Analysis/app/Students_Data_Sample.csv')
    tasks = [process_student(row) for _, row in dataset.iterrows()]
    results = await asyncio.gather(*tasks)
    dataset['Score'] = results
    print(dataset.head(5))  # or save to CSV
    dataset.to_csv("Student_Data_Sample_Score.csv")




#
#print(dataset.head())

if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function
