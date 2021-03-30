from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER

print(LETTER)
canvas = Canvas("report.pdf", pagesize=LETTER)




def generatePDFReport ( title, subtitle, dataResults ):
    # values to use for margin/formatting:
    centerPageWidth = 305
    centerPageHeight = 395
    marginTopBottom = 40
    marginLeftRight = 20
    lineSpacing = 20

    currentFontSize = 16
    currentLine = 750

    if dataResults is None:
        return False
    # test fields:
    # title = "Test PDF Generation"
    # subtitle = "This is a report of suspected bias in your dataset"
    # dataResults = { "Sex assignment at birth": ["male 50", "female 40", "intersex 5", "unknown 5"], "Ethincity": ["African-American 30.6", "Asian-American 10.5", "Caucasian-American 50.8%", "Native-American/Indigenous 1.8%"] }
    
    if title is None:
        title = "Analysis of your Data"
    if subtitle is None:
        subtitle = "A report of possible bias in your dataset"

    canvas.setAuthor("Made by UnbiasData") # or whatever we name this project
    canvas.setFont('Helvetica-Bold', currentFontSize) 

    canvas.drawString((centerPageWidth - len(title)*(currentFontSize/4)), currentLine, title) # set title in page

    currentLine = currentLine - lineSpacing  # reset font and move down one line
    currentFontSize = 13
    canvas.setFont('Helvetica', currentFontSize)

     
    canvas.drawString((centerPageWidth - (len(subtitle)*(currentFontSize/4.5))), currentLine, subtitle) # set subtitle in page
    
    currentLine = currentLine - ( lineSpacing * 1.5 )
    canvas.setFont('Helvetica', currentFontSize-1)

    for var in dataResults: # var is the category
        canvas.drawString(marginLeftRight, currentLine, var)
        canvas.line( marginLeftRight, currentLine-3, centerPageWidth, currentLine-4)
        currentLine = currentLine - lineSpacing
        
        for v in dataResults.get(var): # v is the data/results in a specific category 
            canvas.drawString(marginLeftRight*2, currentLine, v)
            currentLine = currentLine - lineSpacing
        


    canvas.save() # save the pdf as report.pdf and return