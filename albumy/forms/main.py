# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,MultipleFileField,SelectMultipleField
from wtforms.validators import DataRequired, Optional, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class DescriptionForm(FlaskForm):
    description = TextAreaField('Description', validators=[Optional(), Length(0, 500)])
    submit = SubmitField()


class TagForm(FlaskForm):
    tag = StringField('Add Tag (use space to separate)', validators=[Optional(), Length(0, 64)])
    submit = SubmitField()


class CommentForm(FlaskForm):
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField()


class PointForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 60)])
    body = TextAreaField('正文', validators=[DataRequired()])
    photo = FileField('选择图片')
    submit = SubmitField('提交一篇文章')


class RouteForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 60)])
    body = TextAreaField('正文', validators=[DataRequired()])
    points = SelectMultipleField('选择点形成路线',coerce = int)
    submit = SubmitField('提交一条路线')
