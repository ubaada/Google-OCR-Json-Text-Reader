# Google-OCR-Json-Text-Reader
Reads simple page text from JSON book files generated from Google's OCR API and converts it into a readable HTML.

1. Use Google Cloud OCR to convert scanned documents to text

```
# Command to perform OCR on my-book.pdf uploaded in gcloud-storage and generate json files
gcloud ml vision detect-text-pdf gs://xyz/in-pdf/my-book.pdf gs://abc/output-directory/
```

2. Download json files for processing by the python script
```
gsutil -m cp -r "gs://ktbook/jw-book-out" .
```

3. Extract the scanned json data to HTML using gcloud-ocr-to-html.py .
## Google OCR Json Structure

```
- JSON
  - responses
    - fullTextAnnotation
      - pages
        - blocks
          - paragraphs 
            - word 
              - symbols 
                - text
```
Direct whole page text

```
- JSON
  - responses
    - fullTextAnnotation
      * text
```

