from django.db import models

class PostReactions(models.Model):

    rare_user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE)
    post = models.ForeignKey("Posts", on_delete=models.CASCADE)