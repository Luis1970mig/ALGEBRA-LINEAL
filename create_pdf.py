from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor

out='/mnt/data/algebra_lineal_app/resolucion.pdf'
navy=HexColor('#17365D'); orange=HexColor('#E87924'); pale=HexColor('#F2F5F9'); ink=HexColor('#243447')
doc=SimpleDocTemplate(out,pagesize=A4,rightMargin=2.0*cm,leftMargin=2.0*cm,topMargin=1.7*cm,bottomMargin=1.7*cm)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='MainTitle',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=20,leading=25,textColor=navy,alignment=TA_CENTER,spaceAfter=5))
styles.add(ParagraphStyle(name='Sub',parent=styles['Normal'],fontSize=9,leading=13,textColor=HexColor('#657487'),alignment=TA_CENTER,spaceAfter=18))
styles.add(ParagraphStyle(name='H',parent=styles['Heading2'],fontSize=13,leading=17,textColor=navy,spaceBefore=12,spaceAfter=6))
styles.add(ParagraphStyle(name='Body2',parent=styles['BodyText'],fontSize=10,leading=15,textColor=ink,spaceAfter=6))
styles.add(ParagraphStyle(name='Eq',parent=styles['BodyText'],fontName='Helvetica',fontSize=11,leading=17,textColor=ink,leftIndent=12,spaceAfter=5))
styles.add(ParagraphStyle(name='Final',parent=styles['BodyText'],fontName='Helvetica-Bold',fontSize=14,leading=20,textColor=navy,alignment=TA_CENTER))
story=[]
story += [Paragraph('ÁLGEBRA LINEAL',styles['MainTitle']),Paragraph('Programación lineal · Problema de maximización',styles['Sub'])]
story.append(Paragraph('1. Enunciado original',styles['H']))
story.append(Paragraph('Maximice la función objetivo:',styles['Body2']))
story.append(Paragraph('<b>Z = x1 + 2x2 − x3 + 5x4</b>',styles['Eq']))
story.append(Paragraph('Sujeto a:',styles['Body2']))
for s in ['2x1 + 3x2 + x3 − x4 ≤ 8','3x1 + x2 − 4x3 + 5x4 ≤ 9','x1 ≥ 0, x2 ≥ 0, x3 ≥ 0, x4 ≥ 0']:
    story.append(Paragraph(s,styles['Eq']))
story.append(Paragraph('2. Desarrollo de la solución',styles['H']))
story.append(Paragraph('Tomamos inicialmente x1 = 0 y x2 = 0. Igualamos las restricciones:',styles['Body2']))
for s in ['x3 − x4 = 8','−4x3 + 5x4 = 9']:
    story.append(Paragraph(s,styles['Eq']))
story.append(Paragraph('Despejamos la primera ecuación:',styles['Body2']))
story.append(Paragraph('x3 = 8 + x4',styles['Eq']))
story.append(Paragraph('Sustituimos en la segunda ecuación:',styles['Body2']))
for s in ['−4(8 + x4) + 5x4 = 9','−32 − 4x4 + 5x4 = 9','x4 = 41']:
    story.append(Paragraph(s,styles['Eq']))
story.append(Paragraph('Ahora reemplazamos:',styles['Body2']))
for s in ['x3 = 8 + 41','x3 = 49']:
    story.append(Paragraph(s,styles['Eq']))
story.append(Paragraph('Por tanto, la solución candidata es:',styles['Body2']))
story.append(Paragraph('<b>(x1, x2, x3, x4) = (0, 0, 49, 41)</b>',styles['Eq']))
story.append(Paragraph('3. Sustitución en la función objetivo',styles['H']))
for s in ['Z = x1 + 2x2 − x3 + 5x4','Z = 0 + 2(0) − 49 + 5(41)','Z = −49 + 205','Z = 156']:
    story.append(Paragraph(s,styles['Eq']))
story.append(Paragraph('4. Comprobación de las restricciones',styles['H']))
story.append(Paragraph('<b>Primera restricción:</b> 2(0) + 3(0) + 49 − 41 = 8 ≤ 8. Se cumple.',styles['Body2']))
story.append(Paragraph('<b>Segunda restricción:</b> 3(0) + 0 − 4(49) + 5(41) = 9 ≤ 9. Se cumple.',styles['Body2']))
story.append(Paragraph('Además, x1, x2, x3 y x4 son no negativos.',styles['Body2']))
story.append(Paragraph('5. Demostración de optimalidad global',styles['H']))
story.append(Paragraph('Multiplicamos la primera restricción por 15 y la segunda por 4, y sumamos:',styles['Body2']))
story.append(Paragraph('15(2x1 + 3x2 + x3 − x4) + 4(3x1 + x2 − 4x3 + 5x4) ≤ 15(8) + 4(9)',styles['Eq']))
story.append(Paragraph('42x1 + 49x2 − x3 + 5x4 ≤ 156',styles['Eq']))
story.append(Paragraph('Como x1 ≥ 0 y x2 ≥ 0, se tiene:',styles['Body2']))
story.append(Paragraph('Z = (42x1 + 49x2 − x3 + 5x4) − 41x1 − 47x2 ≤ 156',styles['Eq']))
story.append(Paragraph('Por lo tanto, Z ≤ 156 para toda solución factible. La solución (0, 0, 49, 41) satisface las restricciones y alcanza Z = 156; en consecuencia, es óptima global.',styles['Body2']))
summary=Table([[Paragraph('<font color="#E87924"><b>RESULTADO ÓPTIMO</b></font><br/><font size="19" color="#17365D"><b>Z máximo = 156</b></font><br/>x1 = 0 &nbsp;&nbsp; x2 = 0 &nbsp;&nbsp; x3 = 49 &nbsp;&nbsp; x4 = 41',styles['Final'])]],colWidths=[16.5*cm])
summary.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),pale),('BOX',(0,0),(-1,-1),1,HexColor('#DCE4ED')),('TOPPADDING',(0,0),(-1,-1),14),('BOTTOMPADDING',(0,0),(-1,-1),14)]))
story += [Spacer(1,10),summary]
def footer(canvas,doc):
    canvas.saveState(); canvas.setStrokeColor(HexColor('#DCE4ED')); canvas.line(2*cm,1.35*cm,A4[0]-2*cm,1.35*cm)
    canvas.setFont('Helvetica',8); canvas.setFillColor(HexColor('#718094')); canvas.drawString(2*cm,0.95*cm,'Aula Matemática · Álgebra Lineal')
    canvas.drawRightString(A4[0]-2*cm,0.95*cm,f'Página {doc.page}'); canvas.restoreState()
doc.build(story,onFirstPage=footer,onLaterPages=footer)
