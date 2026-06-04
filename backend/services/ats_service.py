def clean_text(text):
    import re
    return re.sub(r'(?<=\w)\s+(?=\w)', '', text)


# skill score 
def calculate_skill_score(text):
    skills = [
        "python",
        "java",
        "c++",
        "react",
        "javascript",
        "html",
        "css",
        "sql",
        "mongodb",
        "fastapi"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    score = min(len(found_skills)*3 , 30)

    return score, found_skills


# project score
def calculate_project_score(text):

    keywords = [
        "project",
        "developed",
        "built",
        "created",
        "implemented"
    ]

    count = 0

    text = text.lower()

    for word in keywords:
        if word in text:
            count += 1

    return min(count * 4, 20)


# education score
def calculate_education_score(text):

    text = text.lower()

    score = 0

    if "b.tech" in text:
        score += 8

    if "computer science" in text:
        score += 7

    return min(score, 15)


# resume completeness score
def calculate_completeness(text):

    sections = [
        "education",
        "skills",
        "project",
        "experience"
    ]

    count = 0

    text = text.lower()

    for section in sections:
        if section in text:
            count += 1

    return count * 3


# keyword match score
def calculate_keyword_score(text):

    keywords = [
        "python",
        "api",
        "database",
        "react",
        "sql",
        "fastapi",
        "javascript"
    ]

    count = 0

    text = text.lower()

    for keyword in keywords:
        if keyword in text:
            count += 1

    return min(count * 3, 20)


# Combine Everything
def calculate_ats_score(text):

    text = clean_text(text)

    skills_score, skills = calculate_skill_score(text) # unpacking tuple : skills_score, skills = (15, ["python", "react"])

    project_score = calculate_project_score(text)

    education_score = calculate_education_score(text)

    completeness_score = calculate_completeness(text)

    keyword_score = calculate_keyword_score(text)

    total_score = (
        skills_score
        + project_score
        + education_score
        + completeness_score
        + keyword_score
    )

    return {
        "overall_score": min(total_score, 100),
        "skills_score": skills_score,
        "project_score": project_score,
        "education_score": education_score,
        "completeness_score": completeness_score,
        "keyword_score": keyword_score,
        "detected_skills": skills
    }