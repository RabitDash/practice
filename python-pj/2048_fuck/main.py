from data.tools import Control
from data.states import init
import curses

fuck = Control()
fuck.setup_states({'Init': init.Init()},'Init')
fuck.main()