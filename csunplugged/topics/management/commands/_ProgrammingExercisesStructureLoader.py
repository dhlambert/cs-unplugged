import os.path
from django.db import transaction

from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import ProgrammingExerciseLanguage, ProgrammingExerciseDifficulty


class ProgrammingExercisesStructureLoader(BaseLoader):
    '''Loader for programming exercises difficulties'''

    def __init__(self, structure_file, BASE_PATH):
        '''Initiates the loader for programming exercises difficulties

        Args:
            structure_file: file path (string)
        '''
        super().__init__(BASE_PATH)
        self.structure_file = structure_file
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])

    @transaction.atomic
    def load(self):
        '''Load the content for programming exerises difficulties

        Raises:
            MissingRequiredFieldError:
        '''
        structure = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.structure_file
            )
        )

        try:
            languages = structure['languages']
            difficulty_levels = structure['difficulties']
        except:
            raise MissingRequiredFieldError()

        for language in languages:
            language_data = languages[language]

            # Check for required fields
            try:
                language_name = language_data['name']
            except:
                raise MissingRequiredFieldError()

            # Check if icon is given
            if 'icon' in language_data:
                language_icon = language_data['icon']
            else:
                language_icon = None

            new_language = ProgrammingExerciseLanguage(
                slug=language,
                name=language_name,
                icon=language_icon
            )

            new_language.save()

            self.log('Added Langauge: {}'.format(new_language.__str__()))

        for difficulty in difficulty_levels:
            try:
                difficulty_level = difficulty['level']
                difficulty_name = difficulty['name']
            except:
                raise MissingRequiredFieldError()

            new_difficulty = ProgrammingExerciseDifficulty(
                level=difficulty_level,
                name=difficulty_name
            )
            new_difficulty.save()

            self.log('Added Difficulty Level: {}'.format(new_difficulty.__str__()))

        # Print log output
        self.print_load_log()
