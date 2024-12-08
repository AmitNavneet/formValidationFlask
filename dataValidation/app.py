from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate')
def validate():
    nameFrm=request.args['studName']
    rollFrm=request.args.get('studRoll')
    scoreFrm=request.args['studScore']
    cgpaFrm=request.args['cgpa']
    if nameFrm=='' or rollFrm=="" or scoreFrm=="" or cgpaFrm=='':
        errMessage="All fields are mandatory"
        return render_template('index.html',errMessage=errMessage)
    #return request.args
    nameError=""
    rollError=""
    scoreError=''
    cgpaError=''
    isError=False
   
    
    welcomeMessage=""
    if nameFrm.isalpha():
        welcomeMessage+=f"Hi {nameFrm}!<br>"
    else:
        isError=True
        nameError="Please enter valid name!"
        
    
    if rollFrm.isdigit():
        welcomeMessage+=f"Your Roll Number is {rollFrm}"
    else:
        isError=True
        rollError="Please enter valid Roll Number"

    if scoreFrm.isnumeric():
        welcomeMessage+=f"<br>Your Score is {scoreFrm}"
    else:
        isError=True
        scoreError="Please enter valid Score"
    
    try:

        cgpaFrm=float(cgpaFrm)
        welcomeMessage+=f"<br>Your CGPA is {cgpaFrm}"
    except:
        isError=True
        cgpaError="Please enter valid CGPA"


    if isError:
        formData={'nameFrm':nameFrm}
        formData.update({'rollFrm':rollFrm})
        formData.update({'scoreFrm':scoreFrm})
        formData.update({'cgpaFrm':cgpaFrm})
        return render_template('index.html',nameError=nameError,rollError=rollError,scoreError=scoreError,cgpaError=cgpaError,formData=formData)
    else:
        welcomeMessage+="<br><a href='/'>Go to Home URL</a>"
        return f"<h1>{welcomeMessage}</h1>"

        




if __name__=="__main__":
    app.run(debug=True)

