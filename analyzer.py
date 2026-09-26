import re

SKILLS_DB = {
    "python": 10,
    "java": 8,
    "c++": 8,
    "html": 6,
    "css": 6,
    "javascript": 10,
    "sql": 10,
    "mysql": 8,
    "flask": 10,
    "django": 10,
    "react": 10,
    "node": 10,
    "machine learning": 15,
    "data analysis": 15,
    "communication": 5
}

JOB_ROLES = {
    "web developer": ["html", "css", "javascript", "react", "node", "flask", "django"],
    "data analyst": ["python", "sql", "data analysis", "machine learning"],
    "software engineer": ["python", "java", "c++", "sql"],
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text


def analyze_resume(text):
    text = clean_text(text)

    found_skills = []
    missing_skills = []
    score = 0

    # ✅ skill detection
    for skill, weight in SKILLS_DB.items():
        if skill in text:
            found_skills.append(skill)
            score += weight
        else:
            missing_skills.append(skill)

    if score > 100:
        score = 100

    # ✅ job role matching
    role_match = {}
    for role, skills in JOB_ROLES.items():
        match_count = sum(1 for s in skills if s in found_skills)
        role_match[role] = int((match_count / len(skills)) * 100)

    best_role = max(role_match, key=role_match.get)

    # -----------------------------
    # ✅ IMPROVEMENT SUGGESTIONS (FIXED)
    # -----------------------------
    suggestions = []

    if "python" not in found_skills:
        suggestions.append("Add Python projects")

    if "sql" not in found_skills:
        suggestions.append("Learn SQL & Databases")

    if "javascript" not in found_skills:
        suggestions.append("Improve JavaScript")

    if "react" not in found_skills:
        suggestions.append("Learn React")

    if "machine learning" not in found_skills:
        suggestions.append("Learn Machine Learning basics")

    if "communication" not in found_skills:
        suggestions.append("Improve communication skills")

    if len(suggestions) == 0:
        suggestions.append("Good profile 👍 Add projects & GitHub")

    # ✅ RETURN
    return {
        "score": score,
        "found_skills": found_skills,
        "missing_skills": missing_skills[:5],
        "status": "Good",
        "best_role": best_role,
        "role_match": role_match,
        "suggestions": suggestions
    }