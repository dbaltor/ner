import unittest
from ner_client import NamedEntityClient
from test.test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):
    """
    Return type:
    { ents: [{...}],
      html: "<span>..."}
    """

    def test_get_ents_returns_dict_given_empty_string_causes_empty_spacy_doc_ents(self):
        # Given
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        # When
        ents = ner.get_ents("")
        # Then
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        # Given
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        # When
        ents = ner.get_ents("Lisbon is a city in Portugal")
        # Then
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serialises_to_Person(self):
        # Given
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Denis Baltor', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        # When
        result = ner.get_ents('...')
        # Then
        expected_results = {'ents': [{'ent': 'Denis Baltor', 'label': 'Person'}] }
        self.assertListEqual(result['ents'], expected_results['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serialises_to_Group(self):
        # Given
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Portuguese', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        # When
        result = ner.get_ents('...')
        # Then
        expected_results = {'ents': [{'ent': 'Portuguese', 'label': 'Group'}] }
        self.assertListEqual(result['ents'], expected_results['ents'])


    def test_get_ents_given_spacy_LOC_is_returned_serialises_to_Location(self):
        # Given
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'the ocean', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        # When
        result = ner.get_ents('...')
        # Then
        expected_results = {'ents': [{'ent': 'the ocean', 'label': 'Location'}] }
        self.assertListEqual(result['ents'], expected_results['ents'])


    def test_get_ents_given_spacy_LANGUAGE_is_returned_serialises_to_Language(self):
        # Given
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        # When
        result = ner.get_ents('...')
        # Then
        expected_results = {'ents': [{'ent': 'ASL', 'label': 'Language'}] }
        self.assertListEqual(result['ents'], expected_results['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_serialises_to_Location(self):
        # Given
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Portugal', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        # When
        result = ner.get_ents('...')
        # Then
        expected_results = {'ents': [{'ent': 'Portugal', 'label': 'Location'}] }
        self.assertListEqual(result['ents'], expected_results['ents'])

    def test_page_has_ner_table(self):
        # Given
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Portugal', 'label_': 'GPE'}, {'text': 'Denis Baltor', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        # When
        result = ner.get_ents('...')
        # Then
        expected_results = {'ents': [{'ent': 'Portugal', 'label': 'Location'},
                                     {'ent': 'Denis Baltor','label': 'Person'}] }
        self.assertListEqual(result['ents'], expected_results['ents'])
