# Gumshoe PDF Composer


Composes one PDF from the given pdf files, in the given sequence,
then writes it to the given outfile.


## Installation


To install, run `pip install pdfcomposer`


## Examples

### Call the default from the command line

```shell

pdfcomposer --outputer index

# index outputers  
# ('compose', 'index') 

```

### Call a plugin (compose) from the command line

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


from pdfcomposer import Api

composer = Api()


# index
args = []

kws = dict(path='index')

result = composer(*args, **kws)

print(result)



# compose
args = ['./outfile.pdf', './infile1.pdf', './infile2.pdf']

kws = dict(path='compose',
           title="My PDF",
           author="John Doe",
           subject="My first PDF",
           creator="John Doe")

result = composer(*args, **kws)

print(result)


# composes a PDF with the content of infile1.pdf then infile2.pdf
# sets the PDF info with the given kwargs
# writes the PDF to ./outfile.pdf


```




