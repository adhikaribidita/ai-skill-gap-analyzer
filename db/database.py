import mongomock

# Use mongomock to simulate a real MongoDB cluster without needing connection strings
client = mongomock.MongoClient()
db = client.skillora_db

# Collections
roles_collection = db.job_roles
users_collection = db.users

# Seed initial data if the collection is empty
if roles_collection.count_documents({}) == 0:
    INITIAL_ROLES = [
        {
            "role": "Data Scientist",
            "skills": ["python", "sql", "machine learning", "statistics", "data visualization", "pandas", "numpy"],
            "description": "Analyze and interpret complex data to help companies make decisions."
        },
        {
            "role": "Data Analyst",
            "skills": ["sql", "python", "pandas", "data visualization", "statistics"],
            "description": "Translate numbers and data into plain English to help businesses understand trends."
        },
        {
            "role": "AI Engineer",
            "skills": ["python", "deep learning", "nlp", "tensorflow", "pytorch", "computer vision", "llms"],
            "description": "Build and deploy artificial intelligence models and applications."
        },
        {
            "role": "Software Development Engineer (SDE)",
            "skills": ["java", "python", "c++", "data structures", "algorithms", "system design", "git"],
            "description": "Design, develop, and maintain complex software systems."
        },
        {
            "role": "Frontend Developer",
            "skills": ["react", "javascript", "html", "css", "git", "system design"],
            "description": "Build the user interface and client-side logic of web applications."
        },
        {
            "role": "Backend Developer",
            "skills": ["node.js", "python", "java", "sql", "docker", "system design", "networking"],
            "description": "Build the server-side logic, databases, and APIs for applications."
        },
        {
            "role": "Full Stack Developer",
            "skills": ["react", "javascript", "node.js", "python", "sql", "docker", "git"],
            "description": "Handle both the frontend UI and the backend servers of web applications."
        },
        {
            "role": "Cloud Engineer",
            "skills": ["aws", "azure", "gcp", "docker", "kubernetes", "linux", "networking", "terraform"],
            "description": "Design, provision, and manage highly scalable cloud infrastructure."
        },
        {
            "role": "Cybersecurity Analyst",
            "skills": ["networking", "linux", "penetration testing", "network security", "wireshark", "cryptography"],
            "description": "Protect networks and systems by identifying and mitigating security vulnerabilities."
        },
        {
            "role": "Core Systems Engineer",
            "skills": ["c++", "data structures", "algorithms", "operating systems", "computer architecture", "compilers", "system design"],
            "description": "Build high-performance, low-level software like operating systems, compilers, and game engines."
        },
        {
            "role": "DevOps Engineer",
            "skills": ["docker", "kubernetes", "linux", "networking", "terraform", "aws", "git"],
            "description": "Automate deployment pipelines and manage server infrastructure."
        },
        {
            "role": "Agile Scrum Master",
            "skills": ["agile", "scrum", "system design", "git"],
            "description": "Facilitate agile ceremonies and manage software delivery pipelines."
        }
    ]
    roles_collection.insert_many(INITIAL_ROLES)

def get_job_roles():
    """Fetch available job roles from MongoDB."""
    roles = roles_collection.find({}, {"role": 1, "_id": 0})
    return [r["role"] for r in roles]

def get_required_skills(role_name):
    """Fetch required skills for a specific role from MongoDB."""
    role_doc = roles_collection.find_one({"role": role_name})
    if role_doc:
        return role_doc.get("skills", [])
    return []

def save_user_progress(user_id, uploaded_skills, missing_skills, match_percentage):
    """Save user analysis to MongoDB for progress tracking."""
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {
            "skills": uploaded_skills,
            "missing": missing_skills,
            "match": match_percentage
        }},
        upsert=True
    )
