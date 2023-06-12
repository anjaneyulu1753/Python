from flask import Flask, render_template, request
app=Flask(__name__)

contact=[]
@app.route('/', methods=["GET","POST"])

def index():
    if request.method=="POST":
        name=request.form["fullname"]
        mobile=request.form["mobile"]
        email=request.form["email"]
        l=len(name)+len(mobile)+len(email)
        if l < 1:
            return render_template("index.html", users=contact, message="Empty values not taken")
        else:
            user={"name": name, "mobile": mobile, "email": email}
            contact.append(user)

    return render_template("index.html",users=contact)

if __name__=="__main__":
    app.run(debug=True)

print(contact)