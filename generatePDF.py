from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER

print(LETTER)
canvas = Canvas("report.pdf", pagesize=LETTER)

# create and save the pdf report from the dicts, dataResultsCSV, dataResultsJSON

def generatePDFReport ( title, subtitle, dataResultsCSV, dataResultsJSON ):
    # values to use for margin/formatting:
    centerPageWidth = 305
    centerPageHeight = 395
    marginTopBottom = 40
    marginLeftRight = 20
    lineSpacing = 20
    maxLenOfLine = 99

    currentFontSize = 16
    currentLine = 750

    if dataResultsCSV is None and dataResultsJSON is None:
        return False
    if len(dataResultsCSV) == 0 and len(dataResultsJSON) == 0:
        return False

    # test fields:
    # title = "Test PDF Generation"
    # subtitle = "This is a report of suspected bias in your dataset"
    # dataResults = { "Sex assignment at birth": ["male 50", "female 40", "intersex 5", "unknown 5"], "Ethincity": ["African-American 30.6", "Asian-American 10.5", "Caucasian-American 50.8%", "Native-American/Indigenous 1.8%"] }
    
    if title is None or title == "":
        title = "Analysis of your Data"
    if subtitle is None or subtitle == "":

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

    canvas.drawString(marginLeftRight, currentLine, "IMPORTANT: This report does not gaurantee that your data is unbiased. This report is not an")
    currentLine = currentLine - lineSpacing
    canvas.drawString(marginLeftRight, currentLine, "analysis of you model, you must perform separate analyis to test your model for bias. Use this")
    currentLine = currentLine - lineSpacing
    canvas.drawString(marginLeftRight, currentLine, "report as a starting point to help you understand how your data might be biased.")
    currentLine = currentLine - ( lineSpacing * 1.5 )

    if dataResultsCSV is not None or len(dataResultsCSV) == 0:

        if currentLine < marginTopBottom+20:
                        canvas.showPage()
                        currentLine = 730
        for var in dataResultsCSV: # var is the category
            canvas.drawString(marginLeftRight, currentLine, var)
            canvas.line( marginLeftRight, currentLine-3, centerPageWidth, currentLine-4)
            currentLine = currentLine - lineSpacing
            if isinstance(dataResultsCSV.get(var), dict):
                for v in dataResultsCSV.get(var):
                    print(dataResultsCSV.get(var)[v])
                    if currentLine < marginTopBottom:
                        canvas.showPage()
                        currentLine = 730
                    try:
                        isNumber = float(dataResultsCSV.get(var)[v])
                        canvas.drawString(marginLeftRight*2, currentLine, "Count: " + v + " is " + str(dataResultsCSV.get(var)[v]))
                        currentLine = currentLine - lineSpacing 
                    except:
                        canvas.drawString(marginLeftRight*2, currentLine, v + " " + str(dataResultsCSV.get(var)[v]))
                        currentLine = currentLine - lineSpacing 
                    
            else:
                for v in dataResultsCSV.get(var): # v is the data/results in a specific category 
                    if currentLine < marginTopBottom:
                            canvas.showPage()
                            currentLine = 730
                    if(len(v) == 1):
                        canvas.drawString(marginLeftRight*2, currentLine, v)
                        currentLine = currentLine - lineSpacing
                    if(len(v) == 0):
                        break
                    else:
                        for i in v:
                            if isinstance(i, list):
                                print(i)
                            else:
                                canvas.drawString(marginLeftRight*2, currentLine, v)
                                currentLine = currentLine - lineSpacing 
                                break
            
    # TODO: need to check if current line runs off the page. If is does, need to make a new page

        

    if dataResultsJSON is not None or len(dataResultsJSON) == 0:

        for var in dataResultsJSON: # var is the category
            if len(dataResultsJSON.get(var)) > 1: 
                if currentLine < marginTopBottom + 20:
                        canvas.showPage()
                        currentLine = 730
                canvas.drawString(marginLeftRight, currentLine, var)
                canvas.line( marginLeftRight, currentLine-3, centerPageWidth, currentLine-4)
                currentLine = currentLine - lineSpacing
                
                for v in dataResultsJSON.get(var): # v is the data/results in a specific category 
                    if currentLine < marginTopBottom:
                        canvas.showPage()
                        currentLine = 730
                    if(len(v) == 1):
                        canvas.drawString(marginLeftRight*2, currentLine, v+  ", " + str(dataResultsJSON.get(var)[v]))
                        currentLine = currentLine - lineSpacing
                    if(len(v) == 0):
                        break
                    else:
                        for i in v:
                            if isinstance(i, list):
                                print(i)
                            else:
                                canvas.drawString(marginLeftRight*2, currentLine, v +  ", " + str(dataResultsJSON.get(var)[v]))
                                currentLine = currentLine - lineSpacing 
                                break
            
    # TODO: need to check if current line runs off the page. If is does, need to make a new page

        # save the pdf as report.pdf and return
    try:
        canvas.save() # save the pdf as report.pdf and return
        return True
    except: 
        return False
    
