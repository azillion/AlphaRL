#!/usr/bin/env python3
from mongoengine import Document, EmbeddedDocumentField, StringField, BooleanField, IntField, DateTimeField


class Replay(Document):
    """Replay Index"""
    pid = IntField(db_field="pid", required=True, unique=True)
    
    replay_id = StringField(db_field="replayId", required=True, unique=True)
    
    fps = IntField(db_field="fps", required=True)
    
    num_frames = IntField(db_field="numFrames", required=True)
    
    map_name = StringField(db_field="mapName")
    
    match_type = StringField(db_field="matchType")
    
    season = IntField(db_field="season")
    
    excitement_factor = IntField(db_field="excitementFactor")
    
    average_rating = IntField(db_field="averageRating")
    
    shot_data = StringField(db_field="shotData")
    
    date_created = DateTimeField(db_field="dateCreated")

    downloaded = BooleanField(db_field="downloaded", default=False)
    
    encoded_file_path = StringField(db_field="encodedFilePath")
    
    parsed_file_path = StringField(db_field="parsedFilePath")

    converted = BooleanField(db_field="converted", default=False)