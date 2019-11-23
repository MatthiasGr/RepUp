# API Concept
This document tries to create a structured overview of our rest api

## /api/user

### POST /api/user/login
Parameters:
 - string token: A permanent access token for the YouTrack api.
 - bool remember: Weather to keep the session cookie for a longer period of time.
Returns: `"OK"` or an error message
 
### POST /api/user/logout
Parameters: none
Returns: `"OK"` or an error message.

### GET /api/user/info
Get some information about the user.
Parameters: id or `"me"`
Returns:
 - From the jetbrains api
    - fullName
    - email
    - role?
    - avatarUrl
 - Added by our api
    - Points
    - Achievement list
    - Position in the leaderboard
    
