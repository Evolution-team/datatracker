import datetime
import factory


from ietf.ipr.models import (
    IprDisclosureBase, HolderIprDisclosure, ThirdPartyIprDisclosure, NonDocSpecificIprDisclosure,
    GenericIprDisclosure, IprDocRel
)

def _fake_patent_info():
    return "Date: %s\nNotes: %s\nTitle: %s\nNumber: %s\nInventor: %s\n" % (
        (datetime.datetime.today()-datetime.timedelta(days=365)).strftime("%Y-%m-%d"),
        factory.Faker('sentence').generate({}),
        factory.Faker('sentence').generate({}),
        'US9999999',
        factory.Faker('name').generate({}),
    )

class IprDisclosureBaseFactory(factory.DjangoModelFactory):
    class Meta:
        model = IprDisclosureBase

    by = factory.SubFactory('ietf.person.factories.PersonFactory')
    compliant = True
    holder_legal_name = factory.Faker('name')
    state_id='posted'
    submitter_name = factory.Faker('name')
    submitter_email = factory.Faker('email') 
    title = factory.Faker('sentence')
    
    @factory.post_generation
    def docs(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for doc in extracted:
                IprDocRel.objects.create(disclosure=self,document=doc.docalias_set.first())


class HolderIprDisclosureFactory(IprDisclosureBaseFactory):
    class Meta:
        model = HolderIprDisclosure

    holder_contact_email = factory.Faker('email')
    holder_contact_name = factory.Faker('name')
    licensing_id = 'reasonable'
    patent_info = _fake_patent_info()


class ThirdPartyIprDisclosureFactory(IprDisclosureBaseFactory):
    class Meta:
        model = ThirdPartyIprDisclosure

    ietfer_name = factory.Faker('name')
    ietfer_contact_email = factory.Faker('email')
    patent_info = _fake_patent_info()


class NonDocSpecificIprDisclosureFactory(IprDisclosureBaseFactory):
    class Meta:
        model = NonDocSpecificIprDisclosure

    holder_contact_email = factory.Faker('email')
    holder_contact_name = factory.Faker('name')
    patent_info = _fake_patent_info()

class GenericIprDisclosureFactory(IprDisclosureBaseFactory):
    class Meta:
        model = GenericIprDisclosure

    holder_contact_email = factory.Faker('email')
    holder_contact_name = factory.Faker('name')
    