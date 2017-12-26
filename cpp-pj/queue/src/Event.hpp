#ifndef Event_hpp
#define Event_hpp

#include "Random.hpp"
#define RANDOM_PARAMETER 100

struct Event
{
  int occur_time;		// -1 represents arrival, >=0 means diposal and the number represents service window.
  int event_type;

  Event *next;

  Event (int occur_time = Random::uniform (RANDOM_PARAMETER), int event_type = -1):occur_time (occur_time), event_type (event_type),
    next
    (NULL)
  {
}};
#endif
