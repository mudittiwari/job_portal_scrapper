# features i want in the app
# 1. user login/signup
# 2. user can search for job by title,location,state,can directly apply to the job,experience level
# 3. user can search for jobs by company name,location,state,can directly apply to the job,experience level
# 4. user can subscribe to mulitple companies so that whenever a new job is posted by that company user will get a notification
# 5. automatically send mails to users when a new job is posted by the company they have subscribed to
# 6. automatically add new jobs in the portal homepage every 24 hours(latest)
# 7. users can save the job link for later applications
# 8. make a user profile database
# 9. sort the jobs by the number of applications

# find jobs according to experience level
# under 24 hours, experience level,title(return the jobs)(homepage)
# under 24 hours, experience level,title,company(return the jobs)(email notification)


from flask import Flask, request, jsonify
from main import *
app=Flask(__name__)



@app.route('/getAllJobs',methods=['GET'])
def getalljobs():
    form=request.json
    # print(form)

    if request.method=="GET":
        jobs=getAllJobs(form['job_title'],form['state'],form['country'],form['experience'])
        return jsonify({'jobs':jobs})
    return jsonify({'jobs':[]})

@app.route('/getAllJobsByCompany',methods=['GET'])
def getalljobsbycompany():
    form = request.json
    # print(form)
    if request.method == "GET":
        jobs = getAllJobsByComapny(form['company'], form['country'], form['experience'])
        return jsonify({'jobs': jobs})



if __name__ == '__main__':
    app.run(debug=True)