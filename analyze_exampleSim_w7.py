from simtools.Analysis.AnalyzeManager import AnalyzeManager
from simtools.SetupParser import SetupParser

from analyzer_collection import *

# This block will be used unless overridden on the command-line
SetupParser.default_block = 'HPC'

user = os.getlogin()  # user initials
expt_name = f'{user}_FE_2022_example_w7'
expt_id = '5f72432c-ded2-ec11-a9f8-b88303911bc1'  ## change expt_id
working_dir = os.path.join('simulation_outputs')

if __name__ == "__main__":
    SetupParser.init()

    sweep_variables = ['itn_coverage', 'Run_Number']
    event_list = ['Received_Treatment', 'Received_ITN', 'Received_SMC']

    # analyzers to run
    analyzers = [
        MonthlyPfPRAnalyzerU5(expt_name=expt_name,
                              working_dir=working_dir,
                              start_year=2010,
                              end_year=2012,
                              sweep_variables=sweep_variables),
    ]
    am = AnalyzeManager(expt_id, analyzers=analyzers)
    am.analyze()
