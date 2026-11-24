# import re

# with open("fest_messages.txt", "r", encoding="utf-8") as file:
#     text = file.read()

# emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)

# print("Valid Emails:")
# for email in emails:
#     print("-", email)

# print("Total Valid Emails:", len(emails))

# import os
# import re

# folder = r"c:\tops\session 1"
# input_file = os.path.join(folder, "fest_messages.txt")

# with open(input_file, "r", encoding="utf-8") as file:
#     text = file.read()

# phones = re.findall(r"\b[6-9]\d{9}\b", text)
# print("Total Mobile Numbers:", len(phones))

# for line_num, line in enumerate(text.splitlines(), start=1):
#     match = re.search(r"\d{2}/\d{2}/\d{4}", line)
#     if match:
#         print(f"First Date Found: {match.group()} on Line {line_num}")
#         break

import json
import os
import re

folder = r"c:\tops\session 1"
with open(
    os.path.join(folder, "fest_messages.txt"), "r", encoding="utf-8"
) as f:
    text = f.read()

# Task 1
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
print("Valid Emails:", emails)
print("Total Valid Emails:", len(emails))

# Task 2
phones = re.findall(r"\b[6-9]\d{9}\b", text)
print("Total Mobile Numbers:", len(phones))

for i, line in enumerate(text.splitlines(), 1):
    m = re.search(r"\d{2}/\d{2}/\d{4}", line)
    if m:
        print(f"First Date: {m.group()} on Line {i}")
        break

# Task 3
masked = re.sub(r"\b[6-9]\d{5}(\d{4})\b", r"XXXXXX\1", text)
with open(
    os.path.join(folder, "fest_messages_masked.txt"), "w", encoding="utf-8"
) as f:
    f.write(masked)

# Task 4
amounts = [int(x) for x in re.findall(r"Rs\s?(\d+)", text)]
total = sum(amounts)
print("Total Tickets:", len(amounts))
print("Total Revenue:", total)

summary = {
    "valid_emails_count": len(emails),
    "phone_numbers_count": len(phones),
    "total_ticket_revenue": total,
}
with open(
    os.path.join(folder, "fest_summary.json"), "w", encoding="utf-8"
) as f:
    json.dump(summary, f, indent=4)
