# File: getEmails.py

def get_emails(input_file, output_file, start, count):
    try:
        with open(input_file, 'r') as infile:
            emails = infile.read().split(',')

        first_2000_emails = emails[start:min(start+2000, len(emails))]

        with open(output_file, 'w') as outfile:
            outfile.write(','.join(first_2000_emails))

        print(f"Successfully wrote the first 2000 emails to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = 'python/emails.txt'  # Path to your input file
    get_emails(input_file, 'emails1.txt', 0, 2000)  # Get the first 2000 emails
    get_emails(input_file, 'emails2.txt', 2000, 2000)  # Get the next 2000 emails
    get_emails(input_file, 'emails3.txt', 4000, 2000)  # Get the next 2000 emails
    get_emails(input_file, 'emails4.txt', 6000, 2000)