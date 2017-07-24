#!/usr/bin/env python3

from mongoengine import Document, Stringfield, ListField, IntField, DateTimeField


class Index(Document):
    """Replay Index"""
    pid = IntField(db_field="pid", required=True)
    
    replay_id = StringField(db_field="replayId", required=True)
    
    url = StringField(db_field="url", required=True)
    
    file_url = StringField(db_field="fileUrl", required=True)
    
    fps = IntField(db_field="fps", required=True)
    
    num_frames = IntField(db_field="numFrames", required=True)
    
    map_name = StringField(db_field="mapName", required=True)
    
    match_type = StringField(db_field="matchType", required=True)
    
    season = IntField(db_field="season", required=True)
    
    excitement_factor = IntField(db_field="excitementFactor")
    
    average_rating = IntField(db_field="averageRating")
    
    shot_data = StringField(db_field="shotData")
    
    date_created = DateTimeField(db_field="dateCreated", required=True)
    