
# 18.1 //task1
# import re

# messages = """1. Aarav Sharma registered via aarav.sharma@example.com for Dance on 14/02/2026, phone 9876543210, paid Rs 250
# 2. Diya Patel registered via diya.patel@example.com for Singing on 14/02/2026, phone 8765432109, paid Rs 300
# 3. Rohan Verma registered via rohan_v@example.com for Coding on 15/02/2026, phone 7654321098, paid Rs 500
# 4. Ananya Nair registered via ananya.nair@example.com for Drama on 15/02/2026, phone 6543210987, paid Rs 200
# 5. Kabir Singh registered via kabir+fest@example.com for Gaming on 16/02/2026, phone 9123456780, paid Rs 400
# 6. Meera Joshi registered via meera.j@example.com for Quiz on 16/02/2026, phone 8234567891, paid Rs 150
# 7. Vikram Rao registered via vikram-rao@example.com for Robotics on 17/02/2026, phone 7345678912, paid Rs 600
# 8. Sneha Gupta registered via sneha.g@example.com for Painting on 17/02/2026, phone 6456789123, paid Rs 250
# 9. Arjun Das registered via arjun.das@example.com for Photography on 18/02/2026, phone 9567891234, paid Rs 350
# 10. Kavya Menon registered via kavya.m@example.com for Debate on 18/02/2026, phone 8678912345, paid Rs 200
# 11. Siddharth Roy registered via sid.roy@example.com for Music on 19/02/2026, phone 7789123456, paid Rs 450
# 12. Nisha Kulkarni registered via nisha.k@example.com for Fashion on 19/02/2026, phone 6891234567, paid Rs 500
# 13. Invalid entry ://example.com on 20/02/2026, phone 9988776655, paid Rs 250
# 14. Invalid entry from pooja@example on 20/02/2026, phone 8877665544, paid Rs 300
# 15. Invalid entry from @example.com on 21/02/2026, phone 7766554433, paid Rs 150"""

# with open("fest_messages.txt", "w") as f:
#     f.write(messages)

# with open("fest_messages.txt", "r") as f:
#     text = f.read()

# emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
# print("Valid Emails:", emails)
# print("Email Count:", len(emails))
# Valid Emails: ['aarav.sharma@example.com', 'diya.patel@example.com', 'rohan_v@example.com', 'ananya.nair@example.com', 'kabir+fest@example.com', 'meera.j@example.com', 'vikram-rao@example.com', 'sneha.g@example.com', 'arjun.das@example.com', 'kavya.m@example.com', 'sid.roy@example.com', 'nisha.k@example.com']
# Email Count: 12
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 


#18.2 //task 2
# import re

# with open("fest_messages.txt", "r") as f:
#     text = f.read()

# phones = re.findall(r"\b[6-9]\d{9}\b", text)
# print("Phone Count:", len(phones))

# with open("fest_messages.txt", "r") as f:
#     for line_num, line in enumerate(f, start=1):
#         match = re.search(r"\d{2}/\d{2}/\d{4}", line)
#         if match:
#             print("First Date:", match.group(), "| Line Number:", line_num)
#             break
# Phone Count: 15
# First Date: 14/02/2026 | Line Number: 1

#18.3 //task 3
# import re

# with open("fest_messages.txt", "r") as f:
#     text = f.read()

# masked_text = re.sub(r"\b[6-9]\d{5}(\d{4})\b", r"XXXXXX\1", text)

# with open("fest_messages_masked.txt", "w") as f:
#     f.write(masked_text)

# print(masked_text)
# Aarav Sharma registered via aarav.sharma@example.com for Dance on 14/02/2026, phone XXXXXX3210, paid Rs 250
# 2. Diya Patel registered via diya.patel@example.com for Singing on 14/02/2026, phone XXXXXX2109, paid Rs 300
# 3. Rohan Verma registered via rohan_v@example.com for Coding on 15/02/2026, phone XXXXXX1098, paid Rs 500
# 4. Ananya Nair registered via ananya.nair@example.com for Drama on 15/02/2026, phone XXXXXX0987, paid Rs 200
# 5. Kabir Singh registered via kabir+fest@example.com for Gaming on 16/02/2026, phone XXXXXX6780, paid Rs 400
# 6. Meera Joshi registered via meera.j@example.com for Quiz on 16/02/2026, phone XXXXXX7891, paid Rs 150
# 7. Vikram Rao registered via vikram-rao@example.com for Robotics on 17/02/2026, phone XXXXXX8912, paid Rs 600
# 8. Sneha Gupta registered via sneha.g@example.com for Painting on 17/02/2026, phone XXXXXX9123, paid Rs 250
# 9. Arjun Das registered via arjun.das@example.com for Photography on 18/02/2026, phone XXXXXX1234, paid Rs 350
# 10. Kavya Menon registered via kavya.m@example.com for Debate on 18/02/2026, phone XXXXXX2345, paid Rs 200
# 11. Siddharth Roy registered via sid.roy@example.com for Music on 19/02/2026, phone XXXXXX3456, paid Rs 450
# 12. Nisha Kulkarni registered via nisha.k@example.com for Fashion on 19/02/2026, phone XXXXXX4567, paid Rs 500
# 13. Invalid entry ://example.com on 20/02/2026, phone XXXXXX6655, paid Rs 250
# 14. Invalid entry from pooja@example on 20/02/2026, phone XXXXXX5544, paid Rs 300
# 15. Invalid entry from @example.com on 21/02/2026, phone XXXXXX4433, paid Rs 150
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 

#18.4 //task 4
# import re
# import json

# with open("fest_messages.txt", "r") as f:
#     text = f.read()

# emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
# phones = re.findall(r"\b[6-9]\d{9}\b", text)
# amounts = re.findall(r"Rs\s?(\d+)", text)

# int_amounts = [int(a) for a in amounts]
# total_revenue = sum(int_amounts)
# ticket_count = len(int_amounts)

# print("Ticket Count:", ticket_count)
# print("Total Ticket Revenue:", total_revenue)

# summary = {
#     "email_count": len(emails),
#     "phone_count": len(phones),
#     "total_revenue": total_revenue
# }

# with open("fest_summary.json", "w") as f:
#     json.dump(summary, f, indent=4)

# print("Summary saved:", summary)
# c:/tops/session 1/18.1.py"'
# Ticket Count: 15
# Total Ticket Revenue: 4850
# Summary saved: {'email_count': 12, 'phone_count': 15, 'total_revenue': 4850}
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 