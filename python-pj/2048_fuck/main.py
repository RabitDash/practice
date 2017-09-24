from data.tools import Control
from data.states import init, run
import curses

fuck = Control()
fuck.setup_states({'Init': init.Init(),
                   'Run': run.Run(),
                   },'Init')
fuck.main()
