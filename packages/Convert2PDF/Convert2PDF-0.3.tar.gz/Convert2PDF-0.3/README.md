[![License: GNU GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/ashfaque/Convert2PDF/blob/main/LICENSE)

## How to install
```sh
pip install Convert2PDF
```

## How to import
```python3
from Convert2PDF.ConvertToPDF import docx2pdfConvert, pptx2pdfConvert, img2pdfConvert, bmp2pdfConvert, txt2pdfConvert, mergePdfs
```

## Dependencies needs to be installed, if using `docx2pdfConvert()` & `pptx2pdfConvert()`
```sh
libreoffice
build-essential
libssl-dev
libffi-dev
python-dev
default-jre
```

## Documentation


### Convert from doc or docx to pdf format.
```python3
docx = docx2pdfConvert(f'{os.getcwd()}/file name.docx', f'{os.getcwd()}/output_dir/')
doc = docx2pdfConvert(f'{os.getcwd()}/file name.doc', f'{os.getcwd()}/output_dir/')
```


### Convert from ppt or pptx to pdf format
```python3
pptx = pptx2pdfConvert(f'{os.getcwd()}/file name.pptx', f'{os.getcwd()}/output/')
ppt = pptx2pdfConvert(f'{os.getcwd()}/file name.ppt', f'{os.getcwd()}/output/')
```


### Convert from jpeg, jpg or png ot pdf format.
```python3
jpeg = img2pdfConvert(f'{os.getcwd()}/file name.jpeg', f'{os.getcwd()}/output/file name.pdf')
jpg = img2pdfConvert(f'{os.getcwd()}/file name.jpg', f'{os.getcwd()}/output/file name.pdf')
png = img2pdfConvert(f'{os.getcwd()}/file name.png', f'{os.getcwd()}/output/file name.pdf')
```


### Convert from bmp to pdf format.
```python3
bmp = bmp2pdfConvert(f'{os.getcwd()}/file name.bmp', f'{os.getcwd()}/output/file name.pdf')
```


### Convert from txt to pdf format.
```python3
txt = txt2pdfConvert(f'{os.getcwd()}/file name.txt', f'{os.getcwd()}/output/file name.pdf')
```


### Merge all pdf files to one pdf file.
```python3
all_pdfs_path_tuple = (
                    f'{os.getcwd()}/file 1.pdf'
                    , f'{os.getcwd()}/file 2.pdf'
                    , f'{os.getcwd()}/file 2.pdf'
                    , f'{os.getcwd()}/file 3.pdf'
                    , f'{os.getcwd()}/file 4.pdf'
                    , f'{os.getcwd()}/file 5.pdf'
                )
merged = mergePdfs(*all_pdfs_path_tuple, output_pdf_file_path=f'{os.getcwd()}/output_merged_file.pdf')
```


## License
[GNU GPLv3](LICENSE)
