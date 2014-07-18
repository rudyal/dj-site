# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table('polls_poll', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('polls', ['Poll'])

        # Adding model 'Choice'
        db.create_table('polls_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Poll'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('polls', ['Choice'])

        # Adding model 'PictureObject'
        db.create_table('polls_pictureobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('tags1', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('picture', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('polls', ['PictureObject'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table('polls_poll')

        # Deleting model 'Choice'
        db.delete_table('polls_choice')

        # Deleting model 'PictureObject'
        db.delete_table('polls_pictureobject')


    models = {
        'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polls.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'polls.pictureobject': {
            'Meta': {'object_name': 'PictureObject'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'tags1': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['polls']