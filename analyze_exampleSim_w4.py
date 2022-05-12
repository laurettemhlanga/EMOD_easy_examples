from simtools.Analysis.AnalyzeManager import AnalyzeManager
from simtools.SetupParser import SetupParser

from analyzer_collection import *

# This block will be used unless overridden on the command-line
SetupParser.default_block = 'LOCAL'

user = os.getlogin()  # user initials
expt_name = f'{user}_FE_2022_example_w4'
expt_id = '2022_05_12_22_38_57_447769'  ## change expt_id
working_dir = os.path.join('simulation_outputs')


if __name__ == "__main__":
    SetupParser.init()

    sweep_variables = ['cm_cov_U5', 'Run_Number']
    event_list = ['Received_Treatment', 'Received_ITN', 'Received_SMC']

    # analyzers to run
    analyzers = [
        TransmissionReport(expt_name=expt_name,
                           working_dir=working_dir,
                           sweep_variables=sweep_variables,
                           monthly_report=True,
                           start_year=2024),
        MonthlyPfPRAnalyzerU5(expt_name=expt_name,
                              working_dir=working_dir,
                              start_year=2022,
                              end_year=2024,
                              sweep_variables=sweep_variables),
        IndividualEventsAnalyzer(expt_name=expt_name,
                                 working_dir=working_dir,
                                 start_year=2022,
                                 selected_year=None,
                                 sweep_variables=sweep_variables),
    ]
    am = AnalyzeManager(expt_id, analyzers=analyzers)
    am.analyze()
