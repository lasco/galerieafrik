# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Categorie_habit'
        db.create_table('afrikimage_categorie_habit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_habit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('afrikimage', ['Categorie_habit'])

        # Adding model 'Categorie_personne'
        db.create_table('afrikimage_categorie_personne', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('az', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('afrikimage', ['Categorie_personne'])

        # Adding model 'Categorie_objet'
        db.create_table('afrikimage_categorie_objet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_objet', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('afrikimage', ['Categorie_objet'])

        # Deleting field 'Personne.prise_de_vue'
        db.delete_column('afrikimage_personne', 'prise_de_vue')

        # Deleting field 'Personne.nombre_personne'
        db.delete_column('afrikimage_personne', 'nombre_personne')

        # Deleting field 'Personne.position'
        db.delete_column('afrikimage_personne', 'position')

        # Deleting field 'Personne.categorie_dage'
        db.delete_column('afrikimage_personne', 'categorie_dage')

        # Deleting field 'Personne.pose'
        db.delete_column('afrikimage_personne', 'pose')

        # Deleting field 'Personne.sexe'
        db.delete_column('afrikimage_personne', 'sexe')

        # Adding M2M table for field sexe on 'Personne'
        db.create_table('afrikimage_personne_sexe', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['afrikimage.personne'], null=False)),
            ('categorie_personne', models.ForeignKey(orm['afrikimage.categorie_personne'], null=False))
        ))
        db.create_unique('afrikimage_personne_sexe', ['personne_id', 'categorie_personne_id'])

        # Adding M2M table for field categorie_dage on 'Personne'
        db.create_table('afrikimage_personne_categorie_dage', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['afrikimage.personne'], null=False)),
            ('categorie_personne', models.ForeignKey(orm['afrikimage.categorie_personne'], null=False))
        ))
        db.create_unique('afrikimage_personne_categorie_dage', ['personne_id', 'categorie_personne_id'])

        # Adding M2M table for field nombre_personne on 'Personne'
        db.create_table('afrikimage_personne_nombre_personne', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['afrikimage.personne'], null=False)),
            ('categorie_personne', models.ForeignKey(orm['afrikimage.categorie_personne'], null=False))
        ))
        db.create_unique('afrikimage_personne_nombre_personne', ['personne_id', 'categorie_personne_id'])

        # Adding M2M table for field prise_de_vue on 'Personne'
        db.create_table('afrikimage_personne_prise_de_vue', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['afrikimage.personne'], null=False)),
            ('categorie_personne', models.ForeignKey(orm['afrikimage.categorie_personne'], null=False))
        ))
        db.create_unique('afrikimage_personne_prise_de_vue', ['personne_id', 'categorie_personne_id'])

        # Adding M2M table for field pose on 'Personne'
        db.create_table('afrikimage_personne_pose', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['afrikimage.personne'], null=False)),
            ('categorie_personne', models.ForeignKey(orm['afrikimage.categorie_personne'], null=False))
        ))
        db.create_unique('afrikimage_personne_pose', ['personne_id', 'categorie_personne_id'])

        # Adding M2M table for field position on 'Personne'
        db.create_table('afrikimage_personne_position', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('personne', models.ForeignKey(orm['afrikimage.personne'], null=False)),
            ('categorie_personne', models.ForeignKey(orm['afrikimage.categorie_personne'], null=False))
        ))
        db.create_unique('afrikimage_personne_position', ['personne_id', 'categorie_personne_id'])

        # Deleting field 'Objet.objet_travail'
        db.delete_column('afrikimage_objet', 'objet_travail')

        # Deleting field 'Objet.vehicule'
        db.delete_column('afrikimage_objet', 'vehicule')

        # Deleting field 'Objet.objet_decoratif'
        db.delete_column('afrikimage_objet', 'objet_decoratif')

        # Deleting field 'Objet.objet_fabrique'
        db.delete_column('afrikimage_objet', 'objet_fabrique')

        # Deleting field 'Objet.objet_domestique'
        db.delete_column('afrikimage_objet', 'objet_domestique')

        # Deleting field 'Objet.objet_naturel'
        db.delete_column('afrikimage_objet', 'objet_naturel')

        # Deleting field 'Objet.objet_loisir'
        db.delete_column('afrikimage_objet', 'objet_loisir')

        # Adding M2M table for field objet_naturel on 'Objet'
        db.create_table('afrikimage_objet_objet_naturel', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('objet', models.ForeignKey(orm['afrikimage.objet'], null=False)),
            ('categorie_objet', models.ForeignKey(orm['afrikimage.categorie_objet'], null=False))
        ))
        db.create_unique('afrikimage_objet_objet_naturel', ['objet_id', 'categorie_objet_id'])

        # Adding M2M table for field objet_fabrique on 'Objet'
        db.create_table('afrikimage_objet_objet_fabrique', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('objet', models.ForeignKey(orm['afrikimage.objet'], null=False)),
            ('categorie_objet', models.ForeignKey(orm['afrikimage.categorie_objet'], null=False))
        ))
        db.create_unique('afrikimage_objet_objet_fabrique', ['objet_id', 'categorie_objet_id'])

        # Adding M2M table for field objet_domestique on 'Objet'
        db.create_table('afrikimage_objet_objet_domestique', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('objet', models.ForeignKey(orm['afrikimage.objet'], null=False)),
            ('categorie_objet', models.ForeignKey(orm['afrikimage.categorie_objet'], null=False))
        ))
        db.create_unique('afrikimage_objet_objet_domestique', ['objet_id', 'categorie_objet_id'])

        # Adding M2M table for field objet_travail on 'Objet'
        db.create_table('afrikimage_objet_objet_travail', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('objet', models.ForeignKey(orm['afrikimage.objet'], null=False)),
            ('categorie_objet', models.ForeignKey(orm['afrikimage.categorie_objet'], null=False))
        ))
        db.create_unique('afrikimage_objet_objet_travail', ['objet_id', 'categorie_objet_id'])

        # Adding M2M table for field vehicule on 'Objet'
        db.create_table('afrikimage_objet_vehicule', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('objet', models.ForeignKey(orm['afrikimage.objet'], null=False)),
            ('categorie_objet', models.ForeignKey(orm['afrikimage.categorie_objet'], null=False))
        ))
        db.create_unique('afrikimage_objet_vehicule', ['objet_id', 'categorie_objet_id'])

        # Adding M2M table for field objet_loisir on 'Objet'
        db.create_table('afrikimage_objet_objet_loisir', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('objet', models.ForeignKey(orm['afrikimage.objet'], null=False)),
            ('categorie_objet', models.ForeignKey(orm['afrikimage.categorie_objet'], null=False))
        ))
        db.create_unique('afrikimage_objet_objet_loisir', ['objet_id', 'categorie_objet_id'])

        # Adding M2M table for field objet_decoratif on 'Objet'
        db.create_table('afrikimage_objet_objet_decoratif', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('objet', models.ForeignKey(orm['afrikimage.objet'], null=False)),
            ('categorie_objet', models.ForeignKey(orm['afrikimage.categorie_objet'], null=False))
        ))
        db.create_unique('afrikimage_objet_objet_decoratif', ['objet_id', 'categorie_objet_id'])

        # Deleting field 'Habillement_bijoux.habillement'
        db.delete_column('afrikimage_habillement_bijoux', 'habillement')

        # Deleting field 'Habillement_bijoux.chaussures'
        db.delete_column('afrikimage_habillement_bijoux', 'chaussures')

        # Deleting field 'Habillement_bijoux.type_habillement'
        db.delete_column('afrikimage_habillement_bijoux', 'type_habillement')

        # Deleting field 'Habillement_bijoux.accessoire'
        db.delete_column('afrikimage_habillement_bijoux', 'accessoire')

        # Deleting field 'Habillement_bijoux.coiffe'
        db.delete_column('afrikimage_habillement_bijoux', 'coiffe')

        # Deleting field 'Habillement_bijoux.Vetement'
        db.delete_column('afrikimage_habillement_bijoux', 'Vetement')

        # Deleting field 'Habillement_bijoux.bijoux'
        db.delete_column('afrikimage_habillement_bijoux', 'bijoux')

        # Adding M2M table for field habillement on 'Habillement_bijoux'
        db.create_table('afrikimage_habillement_bijoux_habillement', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('habillement_bijoux', models.ForeignKey(orm['afrikimage.habillement_bijoux'], null=False)),
            ('categorie_habit', models.ForeignKey(orm['afrikimage.categorie_habit'], null=False))
        ))
        db.create_unique('afrikimage_habillement_bijoux_habillement', ['habillement_bijoux_id', 'categorie_habit_id'])

        # Adding M2M table for field type_habillement on 'Habillement_bijoux'
        db.create_table('afrikimage_habillement_bijoux_type_habillement', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('habillement_bijoux', models.ForeignKey(orm['afrikimage.habillement_bijoux'], null=False)),
            ('categorie_habit', models.ForeignKey(orm['afrikimage.categorie_habit'], null=False))
        ))
        db.create_unique('afrikimage_habillement_bijoux_type_habillement', ['habillement_bijoux_id', 'categorie_habit_id'])

        # Adding M2M table for field Vetement on 'Habillement_bijoux'
        db.create_table('afrikimage_habillement_bijoux_Vetement', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('habillement_bijoux', models.ForeignKey(orm['afrikimage.habillement_bijoux'], null=False)),
            ('categorie_habit', models.ForeignKey(orm['afrikimage.categorie_habit'], null=False))
        ))
        db.create_unique('afrikimage_habillement_bijoux_Vetement', ['habillement_bijoux_id', 'categorie_habit_id'])

        # Adding M2M table for field chaussures on 'Habillement_bijoux'
        db.create_table('afrikimage_habillement_bijoux_chaussures', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('habillement_bijoux', models.ForeignKey(orm['afrikimage.habillement_bijoux'], null=False)),
            ('categorie_habit', models.ForeignKey(orm['afrikimage.categorie_habit'], null=False))
        ))
        db.create_unique('afrikimage_habillement_bijoux_chaussures', ['habillement_bijoux_id', 'categorie_habit_id'])

        # Adding M2M table for field bijoux on 'Habillement_bijoux'
        db.create_table('afrikimage_habillement_bijoux_bijoux', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('habillement_bijoux', models.ForeignKey(orm['afrikimage.habillement_bijoux'], null=False)),
            ('categorie_habit', models.ForeignKey(orm['afrikimage.categorie_habit'], null=False))
        ))
        db.create_unique('afrikimage_habillement_bijoux_bijoux', ['habillement_bijoux_id', 'categorie_habit_id'])

        # Adding M2M table for field coiffe on 'Habillement_bijoux'
        db.create_table('afrikimage_habillement_bijoux_coiffe', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('habillement_bijoux', models.ForeignKey(orm['afrikimage.habillement_bijoux'], null=False)),
            ('categorie_habit', models.ForeignKey(orm['afrikimage.categorie_habit'], null=False))
        ))
        db.create_unique('afrikimage_habillement_bijoux_coiffe', ['habillement_bijoux_id', 'categorie_habit_id'])


    def backwards(self, orm):
        
        # Deleting model 'Categorie_habit'
        db.delete_table('afrikimage_categorie_habit')

        # Deleting model 'Categorie_personne'
        db.delete_table('afrikimage_categorie_personne')

        # Deleting model 'Categorie_objet'
        db.delete_table('afrikimage_categorie_objet')

        # We cannot add back in field 'Personne.prise_de_vue'
        raise RuntimeError(
            "Cannot reverse this migration. 'Personne.prise_de_vue' and its values cannot be restored.")

        # We cannot add back in field 'Personne.nombre_personne'
        raise RuntimeError(
            "Cannot reverse this migration. 'Personne.nombre_personne' and its values cannot be restored.")

        # We cannot add back in field 'Personne.position'
        raise RuntimeError(
            "Cannot reverse this migration. 'Personne.position' and its values cannot be restored.")

        # We cannot add back in field 'Personne.categorie_dage'
        raise RuntimeError(
            "Cannot reverse this migration. 'Personne.categorie_dage' and its values cannot be restored.")

        # We cannot add back in field 'Personne.pose'
        raise RuntimeError(
            "Cannot reverse this migration. 'Personne.pose' and its values cannot be restored.")

        # We cannot add back in field 'Personne.sexe'
        raise RuntimeError(
            "Cannot reverse this migration. 'Personne.sexe' and its values cannot be restored.")

        # Removing M2M table for field sexe on 'Personne'
        db.delete_table('afrikimage_personne_sexe')

        # Removing M2M table for field categorie_dage on 'Personne'
        db.delete_table('afrikimage_personne_categorie_dage')

        # Removing M2M table for field nombre_personne on 'Personne'
        db.delete_table('afrikimage_personne_nombre_personne')

        # Removing M2M table for field prise_de_vue on 'Personne'
        db.delete_table('afrikimage_personne_prise_de_vue')

        # Removing M2M table for field pose on 'Personne'
        db.delete_table('afrikimage_personne_pose')

        # Removing M2M table for field position on 'Personne'
        db.delete_table('afrikimage_personne_position')

        # We cannot add back in field 'Objet.objet_travail'
        raise RuntimeError(
            "Cannot reverse this migration. 'Objet.objet_travail' and its values cannot be restored.")

        # We cannot add back in field 'Objet.vehicule'
        raise RuntimeError(
            "Cannot reverse this migration. 'Objet.vehicule' and its values cannot be restored.")

        # We cannot add back in field 'Objet.objet_decoratif'
        raise RuntimeError(
            "Cannot reverse this migration. 'Objet.objet_decoratif' and its values cannot be restored.")

        # We cannot add back in field 'Objet.objet_fabrique'
        raise RuntimeError(
            "Cannot reverse this migration. 'Objet.objet_fabrique' and its values cannot be restored.")

        # We cannot add back in field 'Objet.objet_domestique'
        raise RuntimeError(
            "Cannot reverse this migration. 'Objet.objet_domestique' and its values cannot be restored.")

        # We cannot add back in field 'Objet.objet_naturel'
        raise RuntimeError(
            "Cannot reverse this migration. 'Objet.objet_naturel' and its values cannot be restored.")

        # We cannot add back in field 'Objet.objet_loisir'
        raise RuntimeError(
            "Cannot reverse this migration. 'Objet.objet_loisir' and its values cannot be restored.")

        # Removing M2M table for field objet_naturel on 'Objet'
        db.delete_table('afrikimage_objet_objet_naturel')

        # Removing M2M table for field objet_fabrique on 'Objet'
        db.delete_table('afrikimage_objet_objet_fabrique')

        # Removing M2M table for field objet_domestique on 'Objet'
        db.delete_table('afrikimage_objet_objet_domestique')

        # Removing M2M table for field objet_travail on 'Objet'
        db.delete_table('afrikimage_objet_objet_travail')

        # Removing M2M table for field vehicule on 'Objet'
        db.delete_table('afrikimage_objet_vehicule')

        # Removing M2M table for field objet_loisir on 'Objet'
        db.delete_table('afrikimage_objet_objet_loisir')

        # Removing M2M table for field objet_decoratif on 'Objet'
        db.delete_table('afrikimage_objet_objet_decoratif')

        # We cannot add back in field 'Habillement_bijoux.habillement'
        raise RuntimeError(
            "Cannot reverse this migration. 'Habillement_bijoux.habillement' and its values cannot be restored.")

        # We cannot add back in field 'Habillement_bijoux.chaussures'
        raise RuntimeError(
            "Cannot reverse this migration. 'Habillement_bijoux.chaussures' and its values cannot be restored.")

        # We cannot add back in field 'Habillement_bijoux.type_habillement'
        raise RuntimeError(
            "Cannot reverse this migration. 'Habillement_bijoux.type_habillement' and its values cannot be restored.")

        # We cannot add back in field 'Habillement_bijoux.accessoire'
        raise RuntimeError(
            "Cannot reverse this migration. 'Habillement_bijoux.accessoire' and its values cannot be restored.")

        # We cannot add back in field 'Habillement_bijoux.coiffe'
        raise RuntimeError(
            "Cannot reverse this migration. 'Habillement_bijoux.coiffe' and its values cannot be restored.")

        # We cannot add back in field 'Habillement_bijoux.Vetement'
        raise RuntimeError(
            "Cannot reverse this migration. 'Habillement_bijoux.Vetement' and its values cannot be restored.")

        # We cannot add back in field 'Habillement_bijoux.bijoux'
        raise RuntimeError(
            "Cannot reverse this migration. 'Habillement_bijoux.bijoux' and its values cannot be restored.")

        # Removing M2M table for field habillement on 'Habillement_bijoux'
        db.delete_table('afrikimage_habillement_bijoux_habillement')

        # Removing M2M table for field type_habillement on 'Habillement_bijoux'
        db.delete_table('afrikimage_habillement_bijoux_type_habillement')

        # Removing M2M table for field Vetement on 'Habillement_bijoux'
        db.delete_table('afrikimage_habillement_bijoux_Vetement')

        # Removing M2M table for field chaussures on 'Habillement_bijoux'
        db.delete_table('afrikimage_habillement_bijoux_chaussures')

        # Removing M2M table for field bijoux on 'Habillement_bijoux'
        db.delete_table('afrikimage_habillement_bijoux_bijoux')

        # Removing M2M table for field coiffe on 'Habillement_bijoux'
        db.delete_table('afrikimage_habillement_bijoux_coiffe')


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
        'afrikimage.categorie_habit': {
            'Meta': {'object_name': 'Categorie_habit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_habit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'afrikimage.categorie_objet': {
            'Meta': {'object_name': 'Categorie_objet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_objet': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'afrikimage.categorie_personne': {
            'Meta': {'object_name': 'Categorie_personne'},
            'az': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'afrikimage.habillement_bijoux': {
            'Meta': {'object_name': 'Habillement_bijoux'},
            'Vetement': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Vetement'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_habit']"}),
            'bijoux': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'bijoux'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_habit']"}),
            'chaussures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'chaussures'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_habit']"}),
            'coiffe': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'coiffe'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_habit']"}),
            'habillement': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'habillement'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_habit']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_habillement': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'type_habillement'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_habit']"})
        },
        'afrikimage.image_p': {
            'Meta': {'object_name': 'Image_p'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'serie': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
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
            'objet_decoratif': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'objet_decoratif'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_objet']"}),
            'objet_domestique': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'objet_domestique'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_objet']"}),
            'objet_fabrique': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'objet_fabrique'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_objet']"}),
            'objet_loisir': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'objet_loisir'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_objet']"}),
            'objet_naturel': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'objet_naturel'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_objet']"}),
            'objet_travail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'objet_travail'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_objet']"}),
            'vehicule': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'vehicule'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_objet']"})
        },
        'afrikimage.personne': {
            'Meta': {'object_name': 'Personne'},
            'categorie_dage': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'categorie_dage'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_personne']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_personne': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'nombre_personne'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_personne']"}),
            'pose': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'pose'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_personne']"}),
            'position': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'position'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_personne']"}),
            'prise_de_vue': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'prise_de_vue'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_personne']"}),
            'sexe': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'sexe'", 'blank': 'True', 'to': "orm['afrikimage.Categorie_personne']"})
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
