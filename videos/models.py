from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image

from work.models import Work

class Video(models.Model):
    name = models.CharField(max_length=75)
    link = models.TextField(max_length=100000)
    info_nl = models.TextField(max_length=50000, null=True, blank=True)
    info_en = models.TextField(max_length=50000, null=True, blank=True)
    is_published = models.BooleanField()
    work = models.OneToOneField(Work, on_delete=models.DO_NOTHING, null=True, help_text="Type meermaals de eerste letter van het werk dat je zoekt om het sneller te vinden.")

    def get_video_frame(self):
        if "youtube" in self.link or "youtu.be" in self.link:
            link = self.link
            if not "embed" in link: link = self.get_yt_embed_link()
            return """<iframe height="315" src="{}" 
                        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                        allowfullscreen></iframe>""".format(link)
        else: # insta
            link = self.get_insta_embed_link()
            return """<iframe class="video" src="{}embed/" height="710" frameborder="0" 
                        scrolling="no" allowtransparency="true"></iframe>""".format(link)

    def get_yt_embed_link(self):
        parts = self.link.split("/")
        if "=" in self.link: parts = self.link.split("=")
        id = parts[len(parts) - 1]
        return "https://www.youtube.com/embed/{}".format(id)

    def get_insta_embed_link(self):
        link = self.link
        if "?" in self.link:
            parts = self.link.split("?")
            link = parts[0]
        if not link.endswith("/"): link = "{}/".format(link)
        return link 
