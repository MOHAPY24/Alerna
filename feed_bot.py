import json

# Load your bot's memory
with open("training.json", "r") as f:
    values = json.load(f)

# Load the knowledge pack
with open("language_pack.json", "r") as f:
    pack = json.load(f)

# Merge questions & answers
for q, a in zip(pack["questions"], pack["answers"]):
    if q.lower() not in values["questions"]:
        values["questions"].append(q.lower())
        values["answers"].append(a.lower())

# Save updated memory
with open("training.json", "w") as f:
    f.write(json.dumps(values, indent=2))

print("✅ Alerna has been fed with knowledge from language_pack.json!")
