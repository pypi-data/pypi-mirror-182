from csv2pdf import convert
import fitz
import pathlib
def csv2img(a):
    name = str(a).replace(".csv",'')
    pdf = str(name) + str(".pdf")
    convert(a, pdf)
    file_path = pdf
    doc = fitz.open(file_path)
    i = 0
    for page in doc:
        i += 1
        pix = page.get_pixmap(dpi=300)  # render page to an image
        output = str(name) + str(i) + ".png"
        pix.save(output)
    doc.close()
    file = pathlib.Path(pdf)
    file.unlink()
    
csv2img(a)
