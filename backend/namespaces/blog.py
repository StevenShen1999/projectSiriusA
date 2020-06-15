from flask_restplus import Resource, abort, Namespace

api = Namespace("blogs", description="APIs to handle all blogs related queries")

from app import db
from flask import jsonify
from schemas.blogSchemas import BlogCreationSchema, BlogPollingSchema
from models.blogs import Blogs
from models.blogsModel import blogCreationDetails
from util.validation import validate_with, validate_with_args
from flask import request

@api.route("")
class GeneralNotes(Resource):
    @api.response(200, "{'message': 'Success', 'blogID': 'uuid4 hexstring'}")
    @api.response(400, "Invalid Parametres")
    @api.response(403, "Missing Parametres")
    @api.expect(blogCreationDetails)
    @api.doc(description="Not going to do any security checks \
        for this webapp, no auth system implemented")
    @validate_with(BlogCreationSchema)
    def post(self, data):
        db.session.add(data)
        db.session.commit()
        return jsonify({"message": "Success", "blogID": data.id})

    @api.response(200, "{'message': 'Success', 'notes': \
        [{'id': '', 'createdOn': '', 'title': '', 'content': ''}, {}]")
    @api.response(400, "Invalid Parametres")
    @api.response(403, "Missing Parametres")
    @api.doc(description="Not going to do any security checks \
        for this webapp, no auth system implemented (STUB API)")
    #@validate_with_args(BlogPollingSchema)
    def get(self):
        print(request.args)
        return jsonify(Blogs.query.filter_by(id=request.args['id']).first().jsonifySelf())

@api.route("/all")
class AllNotes(Resource):
    def get(self):
        return jsonify([blog.jsonifySelf() for blog in Blogs.query.all()])