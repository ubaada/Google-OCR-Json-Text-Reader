# Google-OCR-Json-Text-Reader
Reads simple page text from JSON book files generated from Google's OCR API and converts it into a readable HTML.


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
