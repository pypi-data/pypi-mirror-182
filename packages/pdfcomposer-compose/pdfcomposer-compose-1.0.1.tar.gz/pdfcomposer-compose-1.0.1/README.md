# Compose - Gumshoe PDF Composer Plugin


Composes one PDF from the given pdf files, in the given sequence,
then writes it to the given outfile path.


## Installation


To install, run `pip install pdfcomposer-compose` 

(OR `pip install "pdfcomposer-compose"`)


## Examples

### From the command line
```shell

pdfcomposer --outputer compose \
  --args 'outfile.pdf' 'infile1.pdf' 'infile2.pdf'\
  --kwargs title="My PDF" author="John Doe" subject="My first PDF" creator="John Doe"

# composes a PDF with the content of infile1.pdf then infile2.pdf
# sets the PDF info with the given kwargs
# writes the PDF to ./outfile.pdf

```

### From a script


```python

from pdfcomposer_compose import main

args = ['./outfile.pdf', './infile1.pdf', './infile2.pdf']

kws = dict(path='compose',
           title="My PDF",
           author="John Doe",
           subject="My first PDF",
           creator="John Doe")

result = main(*args, **kws)

print(result)


# composes a PDF with the content of infile1.pdf then infile2.pdf
# sets the PDF info with the given kwargs
# writes the PDF to ./outfile.pdf


```




