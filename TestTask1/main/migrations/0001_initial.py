# encoding: utf-8
from south.db import db
from south.v2 import SchemaMigration

class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table('main_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ))
        db.send_create_signal('main', ['Request'])

        # Adding model 'Person'
        db.create_table('main_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ))
        db.send_create_signal('main', ['Person'])

        # Adding model 'SignalInfo'
        db.create_table('main_signalinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ))
        db.send_create_signal('main', ['SignalInfo'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table('main_request')

        # Deleting model 'Person'
        db.delete_table('main_person')

        # Deleting model 'SignalInfo'
        db.delete_table('main_signalinfo')


    models = {
        'main.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'main.request': {
            'Meta': {'ordering': "['priority', 'time']", 'object_name': 'Request'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'main.signalinfo': {
            'Meta': {'object_name': 'SignalInfo'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
