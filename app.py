from datetime import datetime
from operator import add
import re
from flask import Flask, render_template, request,redirect,session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_ckeditor import CKEditor
from werkzeug.utils import secure_filename
from flask_session import Session


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///StellePaint.sqlite3'
app.config['STATIC_FOLDER'] = "static"
db = SQLAlchemy(app)
# app.config['CKEDITOR_PKG_TYPE'] = 'standard-all'
ckeditor = CKEditor(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

class accessories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Image = db.Column(db.String(100), nullable=False)
    ImageSrc = db.Column(db.String(100), nullable=False)

class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Firstname = db.Column(db.String(100), nullable=False)
    Lastname = db.Column(db.String(100), nullable=False)
    Role = db.Column(db.String(100), nullable=False)

class application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Image = db.Column(db.String(100), nullable=True)
    ImageSrc = db.Column(db.String(100), nullable=True)
    P_ID = db.Column(db.Integer)

class banners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=True)
    B_Image = db.Column(db.String(100), nullable=True)
    DateTime = db.Column(db.String(100), nullable=True)

class brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=True)
    Image = db.Column(db.String(100), nullable=True)

class client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=True)
    Description = db.Column(db.String(100), nullable=True)
    Logo = db.Column(db.String(100), nullable=True)
    client_id = db.Column(db.Integer)


class dealer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=True)
    Surname = db.Column(db.String(100), nullable=True)
    Address = db.Column(db.String(100), nullable=True)
    City = db.Column(db.String(100), nullable=True)
    Pincode = db.Column(db.String(100), nullable=True)
    Country = db.Column(db.String(100), nullable=True)
    Company_name = db.Column(db.String(100), nullable=True)
    Job_title = db.Column(db.String(100), nullable=True)
    Email_id = db.Column(db.String(100), nullable=True)
    Tel_no = db.Column(db.String(100), nullable=True)
    Mobile_no = db.Column(db.String(100), nullable=True)
    Vat_no = db.Column(db.String(100), nullable=True)
    Type_of_activity = db.Column(db.String(100), nullable=True)
    Product_handled = db.Column(db.String(100), nullable=True)

class enquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=True)
    Email = db.Column(db.String(100), nullable=True)
    Company = db.Column(db.String(100), nullable=True)
    Phone = db.Column(db.String(100), nullable=True)
    Message = db.Column(db.String(100), nullable=True)

class event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    EventTitle = db.Column(db.String(100), nullable=True)
    STitle = db.Column(db.String(100), nullable=True)
    Description = db.Column(db.String(100), nullable=True)
    Logo = db.Column(db.String(100), nullable=True)
    DateTime = db.Column(db.String(100), nullable=True)

class gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Image = db.Column(db.String(100), nullable=True)
    ImageSrc = db.Column(db.String(100), nullable=True)
    E_ID = db.Column(db.Integer)

class generalimages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Image = db.Column(db.String(100), nullable=True)
    ImageSrc = db.Column(db.String(100), nullable=True)
    LinkId = db.Column(db.Integer)


class generallinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Link = db.Column(db.String(100), nullable=True)


class portfolio_gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ClientId = db.Column(db.Integer)
    ImageName = db.Column(db.String(100), nullable=True)
    Img = db.Column(db.String(100), nullable=True)
    DateTime = db.Column(db.String(100), nullable=True)

class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Integer)
    Short_Desc = db.Column(db.String(100), nullable=True)
    Det_Desc = db.Column(db.String(100), nullable=True)
    Product_Img1 = db.Column(db.String(100), nullable=True)
    Product_Img2 = db.Column(db.String(100), nullable=True)
    DateTime = db.Column(db.String(100), nullable=True)
    Video = db.Column(db.String(100), nullable=True)
    BrandID = db.Column(db.Integer)

class stencils(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Image = db.Column(db.String(100), nullable=True)
    ImageSrc = db.Column(db.String(100), nullable=True)

class swatches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Image = db.Column(db.String(100), nullable=True)
    ImageSrc = db.Column(db.String(100), nullable=True)
    P_ID = db.Column(db.Integer)


class traditional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Image = db.Column(db.String(100), nullable=True)
    ImageSrc = db.Column(db.String(100), nullable=True)


class Aboutus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    data = db.Column(db.String, nullable=True)

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    facebook = db.Column(db.String, nullable=True)
    twitter = db.Column(db.String, nullable=True)
    youtube = db.Column(db.String, nullable=True)
    instagram = db.Column(db.String, nullable=True)
    maplink = db.Column(db.String, nullable=True)
    
    



@app.route("/")
def hello_world():
    try:
        banner = banners.query.all()
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("index.html",banners=banner,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/brand")
def brandsDisplay():
    try:
        brands = brand.query.all()
        return render_template("brand.html",brands=brands)
    except Exception as e:
        return render_template("404.html")

@app.route("/products")
def productsDisplay():
    try:
        products = product.query.all()
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("products.html",products=products,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/productDetails")
def productDetails():
    try:
        pid = request.args['id']
        products = product.query.filter_by(id=pid).all()
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("product_details.html",products=products,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/companyoverview")
def companyoverview():
    try:
        aboutus = Aboutus.query.all()
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("companyoverview.html",aboutus=aboutus,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/eventsandexhibit")
def eventsandexhibit():
    try:
        events = event.query.all()
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("eventsandexhibit.html",events=events,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/portfolio")
def portfolio():
    try:
        portfolios = client.query.all()
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("portfolio.html",portfolios=portfolios,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/portfoliodetails")
def portfoliodetails():
    try:
        client_id = request.args['cid']
        clientdata = client.query.filter_by(client_id=client_id).first()
        portfolio_gal = portfolio_gallery.query.filter_by(ClientId=client_id).all() 
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("portfolio_details.html",portfolio_gal=portfolio_gal,clientdata=clientdata,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/contactus")
def contactus():
    try:
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("contact.html",setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route("/becomeadealer" ,methods=['GET','POST'])
def becomeadealer():
    try:
        if request.method=='POST':
            fname = request.form['fname']
            lname = request.form['lname']
            address = request.form['address']
            city = request.form['city']
            pincode = request.form['pincode']
            country = request.form['country']
            cname = request.form['cname']
            jtitle= request.form['jtitle']
            email = request.form['email']
            telephone = request.form['telephone']
            mobile = request.form['mobile']
            vatno = request.form['vatno']
            typeofactivity = request.form['typeofactivity']
            producthandled = request.form['producthandled']
            setting_count = Settings.query.count()
            setting_data = Settings.query.filter_by(id=setting_count).first()
            # print(fname,lname,address,city,pincode,country,cname,jtitle,email,telephone,mobile,vatno,typeofactivity,producthandled)
            return render_template("becomeadealer.html",success_message=1,setting_data=setting_data)
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("becomeadealer.html",success_message=0,setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

@app.route('/admin')
def Admin():
    try:
        return render_template('adminpanel.html')
    except Exception as e:
        return render_template("404.html")

@app.route('/login',methods=['GET','POST'])
def login():
    try:
        if request.method=='POST':
            if request.form['uname'] == '' or request.form['pass']=='':
                return redirect("/login")
            creds = admin.query.filter_by(Username = request.form['uname'],Password=request.form['pass']).first()
            print(creds)
            if creds == None:
                return redirect("/login")
            else:
                session["name"] = request.form['uname']
                return redirect("/admin")
            
        return render_template("login.html")
    except Exception as e:
        print(e)

@app.route("/logout",methods=['GET','POST'])
def logout():
    try:
        session.clear()
        return redirect("/login")
    except Exception as e:
        print(e)



@app.route('/bannerpanel',methods=['GET','POST'])
def bannerPanel():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method == 'POST':
            banner_count = banners.query.count()
            file = request.files['imgfile']
            file.seek(0, os.SEEK_END)
            if file.tell() == 0:
                pass
            file.seek(0)
            fname= 'static/Images/Banner/'+str(banner_count+1)+'_'+secure_filename(file.filename)
            file.save(fname)
            newbanner = banners(Name=str(banner_count)+'_'+secure_filename(file.filename),B_Image= 'Images/Banner/'+str(banner_count+1)+'_'+secure_filename(file.filename),DateTime=str(datetime.today()))
            db.session.add(newbanner)
            db.session.commit()
        banner = banners.query.all()
        return render_template("bannerPanel.html",banners=banner)
    except Exception as e:
        return render_template("404.html")

@app.route('/deletebanner',methods=['GET','POST'])
def deletebanner():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        bannerid = request.args['id']
        removebanner = banners.query.filter_by(id=bannerid).first()
        db.session.delete(removebanner)
        db.session.commit()
        return redirect("/bannerpanel")
    except Exception as e:
        return render_template("404.html")

@app.route('/portfoliogallerypanel',methods=['GET','POST'])
def portfoliogallerypanel():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method == 'POST':
            p_img_count = portfolio_gallery.query.count()
            client_id = request.form['client_id']
            file = request.files['imgfile']
            file.seek(0, os.SEEK_END)
            if file.tell() == 0:
                pass
            file.seek(0)
            fname= 'static/Images/Portfolio_Gallery/'+str(p_img_count+1)+'_'+secure_filename(file.filename)
            file.save(fname)
            fname= 'Images/Portfolio_Gallery/'+str(p_img_count+1)+'_'+secure_filename(file.filename)
            newportfolio = portfolio_gallery(ClientId=client_id,ImageName=str(p_img_count+1)+'_'+secure_filename(file.filename),Img= fname,DateTime=str(datetime.today()))
            db.session.add(newportfolio)
            db.session.commit()
        clients = client.query.all()
        portfolio_gallerys = portfolio_gallery.query.all()
        return render_template("portfolio_gallery_panel.html",portfolio_gallerys=portfolio_gallerys,clients=clients)
    except Exception as e:
        return render_template("404.html")

@app.route('/deleteportfolioimage',methods=['GET','POST'])
def deleteportfolioimage():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        bannerid = request.args['id']
        rmpi = portfolio_gallery.query.filter_by(id=bannerid).first()
        db.session.delete(rmpi)
        db.session.commit()
        return redirect("/portfoliogallerypanel")
    except Exception as e:
        return render_template("404.html")


@app.route('/portfoliopanel',methods=['GET','POST'])
def portfoliopanel():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method=='POST':
            c_name = request.form['Name']
            c_desc = request.form['desc']
            c_count = client.query.count()
            file = request.files['client_image']
            file.seek(0, os.SEEK_END)
            if file.tell() == 0:
                pass
            file.seek(0)
            fname= 'static/Images/ClientLogo/'+str(c_count+1)+'_'+secure_filename(file.filename)
            file.save(fname)
            fname= 'Images/ClientLogo/'+str(c_count+1)+'_'+secure_filename(file.filename)
            clientadd = client(Name=c_name,Description=c_desc,Logo=fname,client_id=c_count+3)
            db.session.add(clientadd)
            db.session.commit()
        
        clients = client.query.all()
        return render_template('portfoliopanel.html',clients=clients)
    except Exception as e:
        return render_template("404.html")

@app.route('/deleteclient',methods=['GET','POST'])
def deleteclient():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        client_id = request.args['id']
        clientrm = client.query.filter_by(id=client_id).first()
        db.session.delete(clientrm)
        db.session.commit()
        return redirect("/portfoliopanel")
    except Exception as e:
        return render_template("404.html")


@app.route('/aboutuspanel')
def aboutuspanel():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        aboutus = Aboutus.query.all()
        return render_template('aboutuspanel.html',aboutus=aboutus)
    except Exception as e:
        return render_template("404.html")

@app.route('/addaboutustitle',methods=['GET','POST'])
def addaboutustitle():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method=='POST':
            about_title = request.form['abouttitle']
            aboutus = Aboutus(title=about_title)
            db.session.add(aboutus)
            db.session.commit()
        aboutus = Aboutus.query.all()
        return render_template('aboutuspanel.html',aboutus=aboutus)
    except Exception as e:
        return render_template("404.html")

@app.route('/editaboutus',methods=['GET','POST'])
def editaboutus():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method=='POST':
            title_id = request.form['titleid']
            edittitle = request.form['edittitle']
            editbody= request.form['ckeditor']
            aboutus = Aboutus.query.filter_by(id=title_id).first()
            aboutus.title = edittitle
            aboutus.data = editbody
            db.session.commit()
        aboutus = Aboutus.query.all()
        return render_template('aboutuspanel.html',aboutus=aboutus)
    except Exception as e:
        return render_template("404.html")

@app.route('/deleteaboutus',methods=['GET','POST'])
def deleteaboutus():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        title_id = request.args['titleid']
        aboutus = Aboutus.query.filter_by(id=title_id).first()
        db.session.delete(aboutus)
        db.session.commit()
        return redirect("/aboutuspanel")
    except Exception as e:
        return render_template("404.html")

@app.route('/eventpanel',methods=['GET','POST'])
def eventpanel():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method == 'POST':
            EventTitle = request.form['EventTitle']
            STitle = request.form['STitle']
            Description = request.form['Description']
            event_count = event.query.count()
            file = request.files['imgfile']
            file.seek(0, os.SEEK_END)
            if file.tell() == 0:
                pass
            file.seek(0)
            fname= 'static/Images/Event/'+str(event_count+1)+'_'+secure_filename(file.filename)
            file.save(fname)
            newevent = event(EventTitle=EventTitle,STitle=STitle,Description=Description,Logo= 'Images/Event/'+str(event_count+1)+'_'+secure_filename(file.filename),DateTime=str(datetime.today()))
            db.session.add(newevent)
            db.session.commit()
        events = event.query.all()
        return render_template("eventpanel.html",events=events)
    except Exception as e:
        return render_template("404.html")

@app.route('/deleteevent',methods=['GET','POST'])
def deleteevent():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        eventid = request.args['id']
        removeevent = event.query.filter_by(id=eventid).first()
        db.session.delete(removeevent)
        db.session.commit()
        return redirect("/eventpanel")
    except Exception as e:
        return render_template("404.html")

@app.route('/editevent',methods=['GET','POST'])
def editevent():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method == 'POST':
            e_id=request.form['eventid']
            EventTitle = request.form['EventTitle']
            STitle = request.form['STitle']
            Description = request.form['Description']
            event_count = event.query.count()
            eventdata = event.query.filter_by(id=e_id).first()
            file = request.files['Logo']
            file.seek(0, os.SEEK_END)
            eventdata.EventTitle = EventTitle
            eventdata.STitle = STitle
            eventdata.Description = Description

            if file.tell() == 0:
                pass
            else:
                file.seek(0)
                fname= 'static/Images/Event/'+str(event_count+1)+'_'+secure_filename(file.filename)
                file.save(fname)
                eventdata.Logo='Images/Event/'+str(event_count+1)+'_'+secure_filename(file.filename)
            db.session.commit()
        return redirect("/eventpanel")
    except Exception as e:
        return render_template("404.html")

@app.route('/productpanel',methods=['GET','POST'])
def productpanel():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method == 'POST':
            productid = request.form['productid']
            product_name = request.form['Name']
            Short_Desc = request.form['Short_Desc']
            Det_Desc = request.form['Det_Desc']
            Product_Img1 = request.files['Product_Img1']
            Product_Img2 = request.files['Product_Img2']
            Video = request.files['Video']
            product_count = product.query.count()
            Product_Img1.seek(0, os.SEEK_END)
            if Product_Img1.tell() == 0:
                pass
            else:
                Product_Img1.seek(0)
                p1name= 'static/Images/Product_img1/'+str(product_count+1)+'_'+secure_filename(Product_Img1.filename)
                Product_Img1.save(p1name)
                p1name= 'Images/Product_img1/'+str(product_count+1)+'_'+secure_filename(Product_Img1.filename)

            Product_Img2.seek(0, os.SEEK_END)
            if Product_Img2.tell() == 0:
                pass
            else:
                Product_Img2.seek(0)
                p2name= 'static/Images/Product_Img2/'+str(product_count+1)+'_'+secure_filename(Product_Img2.filename)
                Product_Img2.save(p2name)
                p2name= 'Images/Product_Img2/'+str(product_count+1)+'_'+secure_filename(Product_Img2.filename)


            Video.seek(0, os.SEEK_END)
            if Video.tell() == 0:
                pass
            else:
                Video.seek(0)
                vname= 'static/Videos/'+str(product_count+1)+'_'+secure_filename(Video.filename)
                Video.save(vname)
                vname= 'Videos/'+str(product_count+1)+'_'+secure_filename(Video.filename)
            
            productadd= product(Name=product_name,Short_Desc=Short_Desc,Det_Desc=Det_Desc,Product_Img1=p1name,Product_Img2=p2name,Video=vname,BrandID=14,DateTime=str(datetime.today()))
            db.session.add(productadd)
            db.session.commit()
        products = product.query.all()
        return render_template("productpanel.html",products=products)
    except Exception as e:
        return render_template("404.html")

@app.route('/editproduct',methods=['GET','POST'])
def editproduct():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        if request.method == 'POST':
            productid = request.form['productid']
            product_name = request.form['Name']
            Short_Desc = request.form['Short_Desc']
            Det_Desc = request.form['Det_Desc']
            Product_Img1 = request.files['Product_Img1']
            Product_Img2 = request.files['Product_Img2']
            Video = request.files['Video']
            product_count = product.query.count()
            Product_Img1.seek(0, os.SEEK_END)
            if Product_Img1.tell() == 0:
                pass
            else:
                Product_Img1.seek(0)
                p1name= 'static/Images/Product_img1/'+str(product_count+1)+'_'+secure_filename(Product_Img1.filename)
                Product_Img1.save(p1name)
                p1name= 'Images/Product_img1/'+str(product_count+1)+'_'+secure_filename(Product_Img1.filename)

            Product_Img2.seek(0, os.SEEK_END)
            if Product_Img2.tell() == 0:
                pass
            else:
                Product_Img2.seek(0)
                p2name= 'static/Images/Product_Img2/'+str(product_count+1)+'_'+secure_filename(Product_Img2.filename)
                Product_Img2.save(p2name)
                p2name= 'Images/Product_Img2/'+str(product_count+1)+'_'+secure_filename(Product_Img2.filename)


            Video.seek(0, os.SEEK_END)
            if Video.tell() == 0:
                pass
            else:
                Video.seek(0)
                vname= 'static/Videos/'+str(product_count+1)+'_'+secure_filename(Video.filename)
                Video.save(vname)
                vname= 'Videos/'+str(product_count+1)+'_'+secure_filename(Video.filename)

            productedit = product.query.filter_by(id=productid).first()
            productedit.Name = product_name
            productedit.Short_Desc = Short_Desc
            productedit.Det_Desc = Det_Desc
            productedit.Product_Img1 = p1name
            productedit.Product_Img2 = p2name
            productedit.Video = vname
            db.session.commit()
        return redirect("/productpanel")
    except Exception as e:
        return render_template("404.html")

@app.route('/deleteproduct',methods=['GET','POST'])
def deleteproduct():
    try:
        if not session.get("name"):
            # if not there in the session then redirect to the login page
            return redirect("/login")
        productid = request.args['id']
        removeproduct = product.query.filter_by(id=productid).first()
        db.session.delete(removeproduct)
        db.session.commit()
        return redirect("/productpanel")
    except Exception as e:
        return render_template("404.html")

@app.route('/settings',methods=['GET','POST'])
def settings():
    try:
        if request.method=='POST':
            setting_count = Settings.query.count()
            if setting_count == 0:
                addsetting = Settings(address=request.form['address'],email=request.form['email'],phone_number=request.form['phone_number'],facebook=request.form['facebook'],twitter=request.form['twitter'],youtube=request.form['youtube'],instagram=request.form['instagram'],maplink=request.form['maplink'])
                db.session.add(addsetting)
                db.session.commit()
                return redirect("/settings")
            setting_data = Settings.query.filter_by(id=setting_count).first()
            setting_data.address = request.form['address']
            setting_data.email = request.form['email']
            setting_data.phone_number = request.form['phone_number']
            setting_data.facebook = request.form['facebook']
            setting_data.twitter = request.form['twitter']
            setting_data.youtube = request.form['youtube']
            setting_data.instagram = request.form['instagram']
            setting_data.maplink = request.form['maplink']
            db.session.commit()
        setting_count = Settings.query.count()
        setting_data = Settings.query.filter_by(id=setting_count).first()
        return render_template("settings.html",setting_data=setting_data)
    except Exception as e:
        return render_template("404.html")

if __name__ == '__main__':
   app.run(debug=True)