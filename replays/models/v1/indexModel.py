#!/usr/bin/env python3
from mongoengine import Document, StringField, ListField, IntField, DateTimeField


class Index(Document):
    """Replay Index"""
    pid = IntField(db_field="pid", required=True, unique=True)
    
    replay_id = StringField(db_field="replayId", required=True, unique=True)
    
    url = StringField(db_field="url", required=True, unique=True)
    
    file_url = StringField(db_field="fileUrl", required=True, unique=True)
    
    fps = IntField(db_field="fps", required=True)
    
    num_frames = IntField(db_field="numFrames")
    
    map_name = StringField(db_field="mapName")
    
    match_type = StringField(db_field="matchType")
    
    season = IntField(db_field="season")
    
    excitement_factor = IntField(db_field="excitementFactor")
    
    average_rating = IntField(db_field="averageRating")
    
    shot_data = StringField(db_field="shotData")
    
    date_created = DateTimeField(db_field="dateCreated")
    