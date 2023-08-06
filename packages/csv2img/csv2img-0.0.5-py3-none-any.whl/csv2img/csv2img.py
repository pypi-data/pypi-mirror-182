from csv2pdf import convert
import fitz
def saveas(a=None) -> None:
    if a is not None:
        name = str(a).replace(".csv",'')
        pdf = str(name) + str(".pdf")
        convert(a, pdf)
        file_path = pdf
        doc = fitz.open(file_path)
        i = 0
        for page in doc:
            i += 1
            pix = page.get_pixmap(dpi=300)
            output = str(name) + str(i) + ".png"
            pix.save(output)
        doc.close()
        return " "
