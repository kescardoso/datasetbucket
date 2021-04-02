from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER

print(LETTER)
canvas = Canvas("report.pdf", pagesize=LETTER)




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
    if dataResultsCSV is not None:
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

        
    if dataResultsJSON is not None:
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

        #canvas.save() # save the pdf as report.pdf and return
    canvas.save() # save the pdf as report.pdf and return