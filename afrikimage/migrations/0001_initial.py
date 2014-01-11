# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Auteur'
        db.create_table('afrikimage_auteur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nationalite', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date1', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('adresse', self.gf('django.db.models.fields.TextField')(max_length=90, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('experience', self.gf('django.db.models.fields.TextField')(max_length=80, blank=True)),
        ))
        db.send_create_signal('afrikimage', ['Auteur'])

        # Adding model 'Theme'
        db.create_table('afrikimage_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('afrikimage', ['Theme'])

        # Adding model 'Categorie'
        db.create_table('afrikimage_categorie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Theme'])),
            ('categorie', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('afrikimage', ['Categorie'])

        # Adding model 'Personne'
        db.create_table('afrikimage_personne', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexe', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('categorie_dage', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('nombre_personne', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('prise_de_vue', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('pose', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('afrikimage', ['Personne'])

        # Adding model 'Lieux'
        db.create_table('afrikimage_lieux', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cadre', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('saison', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('type_in', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('type_ex', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('moment', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('pays', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('afrikimage', ['Lieux'])

        # Adding model 'Action'
        db.create_table('afrikimage_action', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_personnage', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('type_pose', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Cadre_action', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('afrikimage', ['Action'])

        # Adding model 'Objet'
        db.create_table('afrikimage_objet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objet_naturel', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('objet_fabrique', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('objet_domestique', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('objet_travail', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('vehicule', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('objet_loisir', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('objet_decoratif', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('afrikimage', ['Objet'])

        # Adding model 'Habillement_bijoux'
        db.create_table('afrikimage_habillement_bijoux', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('habillement', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('type_habillement', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('Vetement', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('chaussures', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('bijoux', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('coiffe', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('accessoire', self.gf('django.db.models.fields.CharField')(max_length=24, blank=True)),
        ))
        db.send_create_signal('afrikimage', ['Habillement_bijoux'])

        # Adding model 'Image_p'
        db.create_table('afrikimage_image_p', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('serie', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('afrikimage', ['Image_p'])

        # Adding model 'Photo'
        db.create_table('afrikimage_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photographe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Auteur'])),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Categorie'])),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('mode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('type_p', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('personne', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Personne'])),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Action'])),
            ('habillement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Habillement_bijoux'])),
            ('objet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Objet'])),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Image_p'])),
            ('lieux', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['afrikimage.Lieux'])),
            ('appareil', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('sens', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=70, blank=True)),
        ))
        db.send_create_signal('afrikimage', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'Auteur'
        db.delete_table('afrikimage_auteur')

        # Deleting model 'Theme'
        db.delete_table('afrikimage_theme')

        # Deleting model 'Categorie'
        db.delete_table('afrikimage_categorie')

        # Deleting model 'Personne'
        db.delete_table('afrikimage_personne')

        # Deleting model 'Lieux'
        db.delete_table('afrikimage_lieux')

        # Deleting model 'Action'
        db.delete_table('afrikimage_action')

        # Deleting model 'Objet'
        db.delete_table('afrikimage_objet')

        # Deleting model 'Habillement_bijoux'
        db.delete_table('afrikimage_habillement_bijoux')

        # Deleting model 'Image_p'
        db.delete_table('afrikimage_image_p')

        # Deleting model 'Photo'
        db.delete_table('afrikimage_photo')


    models = {
        'afrikimage.action': {
            'Cadre_action': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'Meta': {'object_name': 'Action'},
            'action_personnage': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_pose': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'afrikimage.auteur': {
            'Meta': {'object_name': 'Auteur'},
            'adresse': ('django.db.models.fields.TextField', [], {'max_length': '90', 'blank': 'True'}),
            'date1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'experience': ('django.db.models.fields.TextField', [], {'max_length': '80', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationalite': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'afrikimage.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'categorie': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Theme']"})
        },
        'afrikimage.habillement_bijoux': {
            'Meta': {'object_name': 'Habillement_bijoux'},
            'Vetement': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'accessoire': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'bijoux': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'chaussures': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'coiffe': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'habillement': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_habillement': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'afrikimage.image_p': {
            'Meta': {'object_name': 'Image_p'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'serie': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'afrikimage.lieux': {
            'Meta': {'object_name': 'Lieux'},
            'cadre': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moment': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'saison': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'type_ex': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'type_in': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'afrikimage.objet': {
            'Meta': {'object_name': 'Objet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objet_decoratif': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'objet_domestique': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'objet_fabrique': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'objet_loisir': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'objet_naturel': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'objet_travail': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'vehicule': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'afrikimage.personne': {
            'Meta': {'object_name': 'Personne'},
            'categorie_dage': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_personne': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'pose': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'prise_de_vue': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'sexe': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        'afrikimage.photo': {
            'Meta': {'object_name': 'Photo'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Action']"}),
            'appareil': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '70', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'habillement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Habillement_bijoux']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieux': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Lieux']"}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'objet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Objet']"}),
            'personne': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Personne']"}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Image_p']"}),
            'photographe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Auteur']"}),
            'sens': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['afrikimage.Categorie']"}),
            'type_p': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'afrikimage.theme': {
            'Meta': {'object_name': 'Theme'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['afrikimage']
