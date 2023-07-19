import PyPDF2
import json
import os

def convert_pdf_to_txt(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text

def create_json_with_exam_data(pdf_files_folder, output_json_path):
    exams_data = {"exams": []}
    for filename in os.listdir(pdf_files_folder):
        if filename.endswith(".pdf"):
            pdf_file_path = os.path.join(pdf_files_folder, filename)
            exam_name = os.path.splitext(filename)[0]
            exam_data = {"name": exam_name, "text": convert_pdf_to_txt(pdf_file_path)}
            exams_data["exams"].append(exam_data)
    
    with open(output_json_path, 'w') as output_file:
        json.dump(exams_data, output_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pdf_files_folder = "enrikush/learnex/exams"  # Replace with the folder path containing your PDF files
    output_json_path = "enrikush/learnex/questions.json"  # Path to save the JSON file
    create_json_with_exam_data(pdf_files_folder, output_json_path)

