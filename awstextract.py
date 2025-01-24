import boto3

def extract_text_from_pdf(pdf_path):
    # Initialize the AWS Textract client
    textract_client = boto3.client('textract')

    # Read the PDF file as binary
    with open(pdf_path, 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()

    # Call AWS Textract to analyze the document
    response = textract_client.analyze_document(
        Document={'Bytes': pdf_bytes},
        FeatureTypes=['TABLES', 'FORMS']  # Optional: Use 'TABLES' and 'FORMS' for structured data
    )

    # Extract text blocks from the response
    extracted_text = ''
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text += block['Text'] + '\n'

    return extracted_text

# Example usage
if __name__ == "__main__":
    pdf_path = 'data/bp.pdf'
    text = extract_text_from_pdf(pdf_path)
    print("Extracted Text:")
    print(text)
