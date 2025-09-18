from PyPDF2 import PdfMerger
import os

# Pasta onde estão os PDFs
pasta_pdf = "Exemplo/caminho/para/pasta"

# Lista com os PDFs na ordem que você quer unir
pdfs = [
    "Resume.pdf",
    "Declaracao.pdf",
    "documento.pdf",
]

# Criar objeto PdfMerger
merger = PdfMerger()

# Adicionar cada PDF na ordem definida
for pdf in pdfs:
    caminho_completo = os.path.join(pasta_pdf, pdf)
    if os.path.exists(caminho_completo):
        merger.append(caminho_completo)
    else:
        print(f"Aviso: {pdf} não encontrado na pasta!")

# Salvar PDF final
merger.write("PDF_final.pdf")
merger.close()

print("PDFs unidos na ordem especificada com sucesso!")
