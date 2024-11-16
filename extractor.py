from bs4 import BeautifulSoup

html_content = '''

'''

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all passwords
passwords = []
for div in soup.find_all("div", class_="flex gap-3 md:gap-7 py-4 border-b border-primary font-mono"):
    password_div = div.find_all("div")[1]  # The second div contains the password
    passwords.append(password_div.text.strip())

# Display the total number of passwords
print(f"Total passwords extracted: {len(passwords)}")

# Ask whether to save to a file
save_to_file = input("Do you want to save the passwords to a file? (y/n): ").strip().lower()
if save_to_file == 'y':
    file_name = input("Enter the file name to save (e.g., passwords.txt): ").strip()
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write('\n'.join(passwords))  # Write each password on a new line
        print(f"Passwords have been saved to the file: {file_name}")
    except Exception as e:
        print(f"Error occurred while saving the file: {e}")
else:
    print("Operation canceled. Passwords were not saved.")
