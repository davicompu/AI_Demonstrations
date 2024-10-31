import PyPDF2
import os

def read_pdf_files(directory):
    # Initialize lists to hold PDF data
    pdf_data = []

    # Walk through the directory and find all PDF files
    for root_dir, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.pdf'):
                try:
                    # Open the PDF file
                    with open(os.path.join(root_dir, file_name), 'rb') as f:
                        pdf_reader = PyPDF2.PdfFileReader(f)

                        # Get the number of pages in the PDF document
                        num_pages = pdf_reader.numPages

                        # Create a list to hold page data
                        page_data = []

                        # Iterate over each page and extract text
                        for i in range(num_pages):
                            page = pdf_reader.getPage(i)
                            text = page.extractText()
                            page_data.append(text)

                        # Append the PDF data to the main list
                        pdf_data.append({"file_name": file_name, "pdf_content": "\n".join(page_data)})
                except Exception as e:
                    print(f"Failed to read {os.path.join(root_dir, file_name)}: {str(e)}")

    return pdf_data

def save_text_file(pdf_data, output_file):
    try:
        # Open the output file in write mode
        with open(output_file, 'w') as f:
            # Write the PDF data to the file
            for data in pdf_data:
                f.write("CANDIDATE BELOW \n\n\n")
                f.write(data["file_name"] + "\n")
                f.write(data["pdf_content"])
                f.write("\n\n")  # Add a blank line between PDFs
    except Exception as e:
        print(f"Failed to save text data: {str(e)}")

def main():
    directory = 'recruiter_ai/CVs'
    output_file = 'recruiter_ai/candidates_in_text.txt'
    # print(read_pdf_files(directory))
    pdf_data = read_pdf_files(directory)

    if len(pdf_data) > 0:
        save_text_file(pdf_data, output_file)
        print(f"Text data saved to {output_file}.")

if __name__ == "__main__":
    main()