from django.db import models

class Favorite(models.Model):
    id = models.IntegerField(primary_key=True)
    member = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)
    r_code = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='r_code', blank=True, null=True)

    class Meta:
        db_table = 'favorite'


class Img(models.Model):
    img = models.CharField(max_length=200, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    r_code = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='r_code', blank=True, null=True)

    class Meta:
        db_table = 'img'


class Like(models.Model):
    like_dislike = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    r_code = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='r_code', blank=True, null=True)
    member = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'like'


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    real_id = models.CharField(max_length=20)
    pw = models.CharField(max_length=20, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    pi = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'member'


class Menu(models.Model):
    menu_name = models.CharField(max_length=200, blank=True, null=True)
    r_code = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='r_code', blank=True, null=True)

    class Meta:
        db_table = 'menu'


class Recommend(models.Model):
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    r_code = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='r_code', blank=True, null=True)

    class Meta:
        db_table = 'recommend'


class Restaurant(models.Model):
    r_code = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=200, blank=True, null=True)
    r_kind = models.CharField(max_length=30, blank=True, null=True)
    r_img = models.CharField(max_length=200, blank=True, null=True)
    des = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_road = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(blank=True, null=True)
    closetime = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'restaurant'


class Review(models.Model):
    comment = models.CharField(max_length=200, blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    r_code = models.ForeignKey(Restaurant, models.DO_NOTHING, db_column='r_code', blank=True, null=True)
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'review'


class Setting(models.Model):
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'setting'

