from data.tools import Control
from data.states import init, run

fuck = Control()
fuck.setup_states({'Init': init.Init(),
                   'Run': run.Run(),
                   },'Init')
fuck.main()
