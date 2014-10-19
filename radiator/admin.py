from django import forms
from django.contrib import admin

# Register your models here.
from radiator.models import Alarm

class AlarmForm(forms.ModelForm):
    pass
    #if conf.TWITTER_ACCESS_TOKEN and conf.TWITTER_ACCESS_SECRET:
    #    post_to_twitter = forms.BooleanField(required=False, label="Post to Twitter", help_text="This will send a tweet with a brief summary, the permalink to the event (if BASE_URL is defined), and the hashtag of #status for EACH update you add below.")

    #class Meta:
    #    model = AlarmUpdate

class AlarmAdmin(admin.ModelAdmin):
    #form = AlarmForm
    #list_display = ('date_created', 'description', 'status', 'date_updated')
    search_fields = ('description', 'message')
    #list_filter = ('services',)
    #inlines = [AlarmUpdateInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save()
        if 'post_to_twitter' in form.cleaned_data and form.cleaned_data['post_to_twitter']:
            for obj in instances:
                obj.event.post_to_twitter(obj.get_message())

#admin.site.register(Alarm, AlarmAdmin)
admin.site.register(Alarm)
