import pypdf

reader = pypdf.PdfReader("filled-out.pdf")
writer = pypdf.PdfWriter()



writer.add_page(reader.pages[0])
fields = reader.get_fields()

#for field,Value in fields.items():
#    print(f"{field} : {Value}")


for field in fields:
    print(f"{field}")