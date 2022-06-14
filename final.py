from bottle import route,run,template,post,get,request,static_file
import sqlite3
con=sqlite3.connect('JobSearch.db')
cur=con.cursor()

form_style='''<style>/* Basic Grey */
.basic-grey {
    margin-left:auto;
    margin-right:auto;
    max-width: 500px;
    background: #F7F7F7;
    padding: 25px 15px 25px 10px;
    font: 12px Georgia, "Times New Roman", Times, serif;
    color: #888;
    text-shadow: 1px 1px 1px #FFF;
    border:1px solid #E4E4E4;
}
.basic-grey h1 {
    font-size: 25px;
    padding: 0px 0px 10px 40px;
    display: block;
    border-bottom:1px solid #E4E4E4;
    margin: -10px -15px 30px -10px;;
    color: #888;
}
.basic-grey h1>span {
display: block;
font-size: 11px;
}
.basic-grey label {
display: block;
margin: 0px;
}
.basic-grey label>span {
float: left;
width: 20%;
text-align: right;
padding-right: 10px;
 margin-top: 10px;
color: #888;

}
.basic-grey input[type="text"], .basic-grey input[type="email"], .basic-grey textarea, .basic-grey select {
border: 1px solid #DADADA;
color: #888;
height: 30px;
 margin-bottom: 16px;
 margin-right: 6px;
 margin-top: 2px;
 outline: 0 none;
 padding: 3px 3px 3px 5px;
 width: 70%;
 font-size: 12px;
 line-height:15px;
 box-shadow: inset 0px 1px 4px #ECECEC;
 -moz-box-shadow: inset 0px 1px 4px #ECECEC;
 -webkit-box-shadow: inset 0px 1px 4px #ECECEC;
}
 .basic-grey textarea{
 padding: 5px 3px 3px 5px;
 }
.basic-grey select {
background: #FFF no-repeat right;
appearance:none;
-webkit-appearance:none;
-moz-appearance: none;
 text-indent: 0.01px;
 text-overflow: '';
 width: 70%;
 height: 35px;
 line-height: 25px;
 }
 .basic-grey textarea{
 height:100px;
 }
 .basic-grey .button {
 background: #E27575;
 border: none;
 padding: 10px 25px 10px 25px;
 color: #FFF;
 box-shadow: 1px 1px 5px #B6B6B6;
 border-radius: 3px;
 text-shadow: 1px 1px 1px #9E3F3F;
 cursor: pointer;
 }
 .basic-grey .button:hover {
 background: #CF7A7A
 }</style>'''

table_style='''
        <style>
        #table-2 thead, #table-2 tr {
        border-top-width: 2px;
        border-top-style: solid;
        border-top-color: #a8bfde;
        }
        #table-2 {
        border-bottom-width: 2px;
        border-bottom-style: solid;
        border-bottom-color: #a8bfde;
        }

        /* Padding and font style */
        #table-2 td, #table-2 th {
        padding: 3px 3px;
        font-size: 13px;
        font-family: Verdana;
        color: #5b7da3;
        }
        /* Alternating background colors */
        #table-2 tr:nth-child(even) {
        background: #d3dfed
        }
        #table-2 tr:nth-child(odd) {
        background: #FFF
        }
        </style>
        '''

# RelationX: Applicants
# RelationY: Resumes

@route('/')
def initialPage():
    return static_file("initialPage.html",root="pages/")

@route('/mainPage')
def mainPage():
    return static_file("mainPage.html",root="pages/")

@post('/search')
def search():
    email = request.forms.get('searchEmail')
    country = request.forms.get('country')
    # print(email=='')
    # print(country=='None')
    html = table_style
    html += '''
            <h2>applicants searched by email and country<br />
            <span>
            Go back to <a href=/mainPage>search edge</a> 
            </span>
            </h2> <br /> 
            <table id="table-2">
            <tr>
                <td>email</td>
                <td>name</td>
                <td>birthday</td>
                <td>country</td>
                <td>major</td>
             </tr>
        '''

    if email != '' and country != 'None':
        for row in cur.execute(f'select * from applicants where email LIKE \'%{email}%\' and country=\'{country}\' LIMIT 20'):
            html += "<tr>"
            for cell in row:
                html += "<td>" + str(cell) + "</td>"
            html += "<td><a href=\"/deleteap/" + row[0] + "\">delete me</a> </td> "
            html += "<td><a href=\"/update/" + row[0] + "\">update me</a> </td>"
            html += "<td><a href=\"/search/" + row[0] + "\">show resume</a> </td> "
            html += "<td><a href=\"/create/" + row[0] + "\">create resume</a> </td>   </tr> "
        html += "</table>"

    elif email != '' and country == 'None':
        for row in cur.execute(f'select * from applicants where email LIKE \'%{email}%\' LIMIT 20'):
            html += "<tr>"
            for cell in row:
                html += "<td>" + str(cell) + "</td>"
            html += "<td><a href=\"/deleteap/" + row[0] + "\">delete me</a> </td> "
            html += "<td><a href=\"/update/" + row[0] + "\">update me</a> </td>"
            html += "<td><a href=\"/search/" + row[0] + "\">show resume</a> </td> "
            html += "<td><a href=\"/create/" + row[0] + "\">create resume</a> </td>   </tr> "
        html += "</table>"

    elif email == '' and country != 'None':
        for row in cur.execute(f'select * from applicants where country=\'{country}\' LIMIT 20'):
            html += "<tr>"
            for cell in row:
                html += "<td>" + str(cell) + "</td>"
            html += "<td><a href=\"/deleteap/" + row[0] + "\">delete me</a> </td> "
            html += "<td><a href=\"/update/" + row[0] + "\">update me</a> </td>"
            html += "<td><a href=\"/search/" + row[0] + "\">show resume</a> </td> "
            html += "<td><a href=\"/create/" + row[0] + "\">create resume</a> </td>   </tr> "
        html += "</table>"

    else:
        for row in cur.execute(f'select * from applicants LIMIT 20'):
            html += "<tr>"
            for cell in row:
                html += "<td>" + str(cell) + "</td>"
            html += "<td><a href=\"/deleteap/" + row[0] + "\">delete me</a> </td> "
            html += "<td><a href=\"/update/" + row[0] + "\">update me</a> </td>"
            html += "<td><a href=\"/search/" + row[0] + "\">show resume</a> </td> "
            html += "<td><a href=\"/create/" + row[0] + "\">create resume</a> </td>   </tr> "
        html += "</table>"

    return html

@route('/deleteap/<email>')
def delete(email):
    cur.execute("delete from applicants where email = '" + email + "'")
    con.commit()
    cur.execute("delete from resumes where applicant_email ='" + email+"'")
    con.commit()
    return email + " deleted "+"Resume for" + email + " is also deleted </br> return to <a href = \"/mainPage\">search page</a>"



# this function use to get form information from user and send to updated page
@route('/update/<email>')
def update(email):
    html=form_style
    html+=f'<form action = "/updated/{email}" method = "post" class="basic-grey">' \
         f'<h3> You are updating user: {email} </h4>'
    html+='''
    <label>
    <span>name:</span>
    <input name = "name" type="text" />
    </label>
    
    <label>
    <span>birthday:</span>
    <input name = "birthday" type="text" />
    </label>
    
    <label>
    <span>country:</span>
    <input name = "country" type="text" />
    </label>
    
    <label>
    <span>major:</span>
    <input name = "major" type="text" />
    </label>
    
    <label>
        <span>&nbsp;</span>
        <input type="submit" class="button" value="Update" />
    </label>
    </form>
    '''
    return html

# this function can excute SQL update
@post('/updated/<email>')
def updated(email):
    email = email
    name = request.forms.get('name')
    birthday = request.forms.get('birthday')
    country = request.forms.get('country')
    major = request.forms.get('major')
    statement=f'''
    UPDATE applicants 
    SET name='{name}',
        birthday='{birthday}',
        country='{country}',
        major='{major}'
    WHERE email='{email}';
    '''

    print(statement)
    cur.execute(statement)
    con.commit()
    return email + " updated </br> return to <a href = \"/mainPage\">search page</a>"

@post('/insert')
def insert():
    email = request.forms.get('email')
    name = request.forms.get('name')
    birthday = request.forms.get('birthday')
    country = request.forms.get('country')
    major = request.forms.get('major')
    # print(runnername, age, yearsrunning, favrace)
    cur.execute("insert into applicants values ('{0}', '{1}', '{2}', '{3}', '{4}')".format(email, name, birthday,country,major))
    con.commit()
    return email + " inserted </br> return to <a href = \"/mainPage\">search page</a>"

@route('/applicants/listall')
def listApplicants():
    html = table_style
    html += '''<h2> all applicants</h2> <br /> <table id="table-2"><tr>
                <td>email</td>
                <td>name</td>
                <td>birthday</td>
                <td>country</td>
                <td>major</td>
             </tr>'''
    for row in cur.execute('select * from applicants'):
        html += "<tr>"
        for cell in row:
            html += "<td>" + str(cell) + "</td>"
        html += "<td><a href=\"/deleteap/" + row[0] + "\">delete me</a> </td> "
        html += "<td><a href=\"/update/" + row[0] + "\">update me</a> </td>"
        html += "<td><a href=\"/search/" + row[0] + "\">show resume</a> </td> "
        html += "<td><a href=\"/create/" + row[0] + "\">create resume</a> </td>   </tr> "
    html += "</table>"
    return html

# about relation Y
@route('/resumes/listall')
def listResumes():
    html = table_style
    html += '''<h2> all resumes</h2> <br /> <table id="table-2"><tr>
                <td>id</td>
                <td>version</td>
                <td>major</td>
                <td>email</td>
             </tr>'''
    for row in cur.execute('select * from resumes'):
        html += "<tr>"
        for cell in row:
            html += "<td>" + str(cell) + "</td>"
        html += "<td><a href=\"/delete/" + str(row[0]) + "\">delete me</a> </td> </tr> "
    html += "</table>"
    return html

@route('/delete/<resume_id>')
def delete(resume_id):
    cur.execute("delete from resumes where resume_id = " + resume_id)
    con.commit()
    return "Resume:"+ resume_id + " deleted </br> return to <a href = \"/resumes/listall\">resume page</a>"

@route('/search/<applicant_email>')
def searchResumeByApplicant(applicant_email):
    html = table_style
    html += '''<h2> all resumes</h2> <br /> <table id="table-2"><tr>
                    <td>id</td>
                    <td>version</td>
                    <td>interest</td>
                    <td>email</td>
                 </tr>'''
    for row in cur.execute(f'select * from resumes WHERE applicant_email=\'{applicant_email}\''):
        html += "<tr>"
        for cell in row:
            html += "<td>" + str(cell) + "</td>"
        html += "<td><a href=\"/delete/" + str(row[0]) + "\">delete me</a> </td> </tr> "
    html += "</table>"
    return html

@route('/create/<applicant_email>')
def create(applicant_email):
    html = form_style
    html +=f'<form action = "/created/{applicant_email}" method = "post" class="basic-grey">'
    html += f'''<h2>You are creating Resume For Applicant:{applicant_email}</h2>
                <span> Make Sure Your ID >10099 and never duplicat</span>'''
    html += '''
        <label>
        <span>resume_id:</span>
        <input name = "resume_id" type="text" />
        </label>

        <label>
        <span>version:</span>
        <input name = "version" type="text" placeholder="Must Be Integer"/>
        </label>

        <label>
        <span>interest:</span>
        <input name = "interest" type="text" />
        </label>

        <label>
            <span>&nbsp;</span>
            <input type="submit" class="button" value="Create" />
        </label>
        </form>
        '''


    # html=f'''
    #
    # '''
    # html += f'''
    #         <form action = "/created/{applicant_email}" method = "post">
    #             resume_id: <input name = "resume_id" type="text" />
    #             version: <input name = "version" type="text" placeholder="Integer" />
    #             interest: <input name = "interest" type="text" />
    #             <input value = "Insert!" type = "submit" />
    #         </form>'''

    return html

@post('/created/<applicant_email>')
def create(applicant_email):
    applicant_email = applicant_email
    resume_ID = request.forms.get('resume_id')
    version=request.forms.get('version')
    interest = request.forms.get('interest')
    statement = f'''
        INSERT INTO resumes
        VALUES ('{resume_ID}','{version}','{interest}','{applicant_email}');
        '''
    print(statement)
    cur.execute(statement)
    con.commit()
    return "Resume"+str(resume_ID)+"for applicant "+str(applicant_email) \
           + " created </br> return to <a href = \"/resumes/listall\">resume page</a>"


run(host='localhost', port=8081, debug = True)


