from datetime import datetime

print(datetime.today())


# @app.route("/transfer")
# def transfer():
#     cursor.execute("Select * from StellePaint.swatches")
#     b = cursor
#     for row in b:
#         a = swatches(Image=row["Image"],ImageSrc=row["ImageSrc"],P_ID=row["P_ID"])
#         db.session.add(a)
#         db.session.commit()
#     # tables = ["brand","admin"]
#     # for i in tables:
#     #     a = i.__table__.columns.keys()
#     #     print(a)    
#     return render_template("index.html",banners=b)


# @app.route("/transfer")
# def transfer():
#     clientdata = client.query.all()
#     for c in clientdata:
#         c.client_id=c.id+2
#         print(c.client_id)
#         db.session.commit()
#     clientdata1 = client.query.all()
#     for i in clientdata1:
#         print(i.client_id)
#     return "Done"