from django.core.management import BaseCommand
from emessages import console as emc
from tips import console as tc


class Command(BaseCommand):
    @staticmethod
    def populate():
        # user = User.objects.create_superuser(
        #     username="yonim",
        #     email='yonim@gmail.com',
        #     password='123456789')
        # user.full_clean()
        # user.save()
        # user = User.objects.create_superuser(
        #     username="yuval",
        #     email='yuval@gmail.com',
        #     password='123456789')
        # user.full_clean()
        # user.save()
        emc.save_emessages(emc.get_wiki_http_errors())
        tc.save_tips(tc.load_tips_from_dlsv())





    def handle(self, *args, **options):
        self.populate()
