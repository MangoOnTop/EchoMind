#contains structure of agent's memory
memory_schema = {
    #system and session metadata
    #Tracks lifecycle metrics without cluttering personal data
    "metadata":{ 
        "version" : "1.0",
        "create-time" : "2026-08-25",
        "latest-update-time" : None,
        "session_count" : 0,
        "last_saved" : None,
        "session_start_time": None,
    },
    #identity and long term 
    #Holds persistent facts that remembers across restarts
    "user_profile" : {
        "username" : None,
        "location" : None,
        "living" : None,
        "fav_hobby" : None,
        "fav_game" : None,
        "important_fact" : [],        
    },
    #short term memory
    #Working memory for immediate turn-by-turn context
    "conversation_history": [],
}