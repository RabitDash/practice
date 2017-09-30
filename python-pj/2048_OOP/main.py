from data.tools import Control
from data.states import init, run, halt

fuck = Control()
fuck.setup_states({'Init': init.Init(),
                   'Run': run.Run(),
                   'Halt': halt.Halt()
                   },'Init')
fuck.main()
