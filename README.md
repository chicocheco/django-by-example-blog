# django-by-example-blog

## First to third chapter of the book Django 3 by Example

Commits were made after adding an important feature for future reference.
Also, this Django project was dockerized and the secrets are stored in .env file (not committed).

### Installing trigram extension in postgres database:
0) right click on db container in PyCharm - create terminal
1) Log into postgres:
```psql -U <DB_USERNAME>```
(username, password and database name are 'postgres' by default)

2) After you are connected, switch to the DB you want to install the extension for:
```\c <DB_NAME>```

3) Then install the extension as answered previously:
```CREATE EXTENSION pg_trgm;```

### Iproved tag system explained:
```from taggit.models import Tag
from .models import Post


post = Post.published.get(id=1)
post_tags_ids = post.tags.values_list('id', flat=True)
```
1) create a list of similar posts
```
Post.published.get(id=1).tags.values_list()
<QuerySet [(1, 'jazz', 'jazz'), (2, 'django', 'django'), (3, 'music', 'music')]>
Post.published.get(id=1).tags.values_list('id')
<QuerySet [(1,), (2,), (3,)]>
Post.published.get(id=1).tags.values_list('id', flat=True)
<QuerySet [1, 2, 3]>
    
Post.published.filter(tags__in=post_tags_ids)
<QuerySet [<Post: Music on Wikipedia>, <Post: What is Django framework>, <Post: Who was Django Reinhardt?>, <Post: Who was Django Reinhardt?>, <Post: Who was Django Reinhardt?>]>
```
2) this shows you any post that has tags of the current post, but we want to exclude the current post
```
similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
```
3) count the number of tags in each similar post

### Difference between agregate and annotate:
- The output of the annotate() clause is a QuerySet
- aggregate() is a terminal clause for a QuerySet that, when invoked, returns a dictionary of name-value pairs
```
from django.db.models import Count

similar_posts.annotate(same_tags=Count('tags'))
<QuerySet [<Post: What is Django framework>, <Post: Music on Wikipedia>]>

similar_posts.aggregate(same_tags=Count('tags'))
{'same_tags': 2}
```
1) order the results to put higher number of tags and more recent to the top
```
similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')
```
2) limit to 4 results
```
similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
```
### List of commits:

- switch to search with trigram similarity
- add weight to search vectors and filter results by rank 0.3+
- add stemming and ranking search results
- build full text search view/form/template, switch to remote interpreter
- switch to postgres db using docker, move secrets to .env, add requirements.txt
- dockerize project (still with sqlite)
- add RSS feed
- add sitemap.xml
- add markdown filter using markdown library
- add custom another simple_tag for sidebar (3 in total)
- add custom simple_tag and inclusion_tag in blog
- add similar posts feature (extended use of tags)
- add tags implementation using post_list function-based view again (taggit lib)
- extend post_detail by comment form logic, add comments counter, comments and form to detail template
- add model, admin and form for comments
- add share form (form, view, urlpath, templates)
- change function-based post_list view to class-based PostListView
- add function-based pagination to post_list
- fix get_absolute_url of Post, add project-wise static and templates folder, fix blog/ url path, add first html and css
- add get_absolute_url using reverse in Post model
- add root url route to blog app
- add url routes for blog app
- add post_detail view
- add post_list view
- add PublishedManager
- first commit
