from commands.generate_legislator_support_oppose_count_command import \
    GenerateLegislatorSupportOpposeCountCommand
from dtos.legislator_support_oppose_count_dto import LegislatorSupportOpposeCountDto
from infrastructure.csv_writer import CsvWrite


class GenerateLegislatorSupportOpposeCountCommandHandler:

    def __init__(self):
        pass

    def handle(self, command: GenerateLegislatorSupportOpposeCountCommand):
        legislators_by_id_map = {legislator.id: legislator for legislator in
                                 command.legislators}

        legislator_dto_by_id_map = {}

        for vote_result in command.vote_results:
            legislator = legislators_by_id_map.get(vote_result.legislator_id)

            if legislator.id in legislator_dto_by_id_map:
                legislator_dto = legislator_dto_by_id_map[legislator.id]
                legislator_dto.update_votes(vote_result)
            else:
                legislator_dto_by_id_map[legislator.id] = LegislatorSupportOpposeCountDto(legislator, vote_result)

        CsvWrite().write(list(legislator_dto_by_id_map.values()), 'legislators-support-oppose-count.csv')

